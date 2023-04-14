import json
import pydantic
from flask.views import MethodView
from flask import request, make_response
from backend.utilities import DbController


class BaseResource(MethodView):
    model = None
    schema = None
    permissions = None

    def dispatch_request(self, *args, **kwargs):
        if self.permissions:
            for permission in self.permissions:
                permission(self, *args, **kwargs)
        try:
            return super(BaseResource, self).dispatch_request(*args, **kwargs)
        except pydantic.ValidationError as e:
            return make_response(json.loads(e.json()), 400)
        except KeyError as e:
            return make_response({"detail": e.__repr__()}, 400)
        except Exception as e:
            return make_response({"detail": e.__str__()}, 400)
    
    def get_schema_class(self):
        if not self.schema:
            raise NotImplementedError()
        
        return self.schema


class GenericListResource(BaseResource):
    filter = None

    def get_list(self):
        if not self.model:
            raise NotImplementedError()
        
        request.values = dict(request.values)
        if not request.values or not self.filter:
            return self.model.query.all()
        
        query = self.model.query.filter()
        filter_obj = self.filter(self, request)
        query = filter_obj.apply_filter(query)
        query = filter_obj.order(query)
        query = filter_obj.paginate(query)

        return query
    
    def perform_create(self, object_data):
        object = self.model(**object_data.dict())
        DbController().create_object(object)
        return object_data.dict()


class GenericDetailResource(BaseResource):
    response_schema = None
    lookup_field = None
    update_schema = None

    def get_object_id(self):
        kwargs = request.view_args
        if not self.lookup_field:
            if len(kwargs.items())>1:
                raise Exception("Lookup field parameter needed.")
            ids = [value for value in kwargs.values()]
            return ids[0]
        return kwargs.get(self.lookup_field)

    def get_object(self):
        if not self.model:
            raise NotImplementedError()
        
        object_id = self.get_object_id()
        return self.model.query.get_or_404(object_id)
    
    def update_object(self, schema, object):
        object_dict = schema.dict()
        fields = [field for field in list(schema.__fields_set__) if field != 'id']
        for field in fields:
            setattr(object, field, object_dict.get(field))
        DbController.commit()
        return object
    
    def get_update_schema_class(self):
        if self.update_schema:
            return self.update_schema
        else:
            return self.get_schema_class()