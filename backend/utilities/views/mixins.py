import uuid
from ..base_db_controller import DbController
from flask import make_response, request


class DetailObjectMixin:
    def get(self, *args, **kwargs):
        object = self.get_object()
        schema = self.get_schema_class()
        response_object = schema.from_orm(object)
        return make_response(response_object.dict(), 200)

class UpdateObjectMixin:
    def put(self, *args, **kwargs):
        object = self.get_object()
        schema = self.get_update_schema_class()
        request_obj = schema(id=object.id, **request.json)
        response_object = self.update_object(request_obj, object)
        response_schema = self.get_schema_class()
        response = response_schema.from_orm(response_object)
        return make_response(response.dict(), 200)

class DestroyObjectMixin:
    def delete(self, *args, **kwargs):
        object = self.get_object()
        DbController().delete_object(object)
        return make_response({}, 204)

class ListObjectMixin:
    def get(self, *args, **kwargs):
        request.view_args.update(dict(request.values))
        objects = self.get_list()
        schema = self.get_schema_class()
        parsed_objects = []
        for object in objects:
            parsed_objects.append(schema.from_orm(object).dict())
        return make_response({"data": parsed_objects}, 200)

class CreateObjectMixin:
    def post(self, *args, **kwargs):
        schema = self.get_schema_class()
        object_data = schema(id=uuid.uuid4(), **request.get_json())
        response_data = self.perform_create(object_data)
        return make_response(response_data, 201)