import operator
operators = {
    "gt": operator.gt,
    "ge": operator.ge,
    "lt": operator.lt,
    "le": operator.le
}

class Filter:
    def __init__(self, view, request):
        self.model = view.model
        self.request = request
        self.filter_fields = self.get_filter_fields(view)
        self.allowed_filter_params = self.get_allowed_filter_params()
        self.ordering_fields = self.get_ordering_fields(view)
        self.ordering_param = self.get_ordering_params()
        self.pagination_params = self.get_pagination_params()

    def get_filter_fields(self, view):
        if not hasattr(view, "filter_fields"):
            return []
        return view.filter_fields

    def get_allowed_filter_params(self):
        params = {
            key: value
            for key, value in self.request.values.items()
            if key in self.filter_fields
        }
        return params

    def get_filter(self, query_filter):
        splitted_query_filter = query_filter.split('__')
        attr = splitted_query_filter[0]
        if len(splitted_query_filter)==2:
            op = operators.get(splitted_query_filter[1])
        else:
            op = operator.eq
        return attr, op

    def apply_filter(self, query):
        for query_filter, value in self.allowed_filter_params.items():
            attr, op = self.get_filter(query_filter)
            model_attr = getattr(self.model, attr)
            query = query.filter(op(model_attr, value))
        return query
    
    def get_ordering_params(self):
        order = {
            key: value
            for key, value in self.request.values.items()
            if key == "order_by"
            and value in self.ordering_fields
        }
        return order.get('order_by')
    
    def get_ordering_fields(self, view):
        if not hasattr(view, "order_fields"):
            return []
        
        return view.order_fields
    
    def order(self, query):
        if not self.ordering_param:
            return query

        if self.ordering_param[0] == '-':
            param = self.ordering_param[1:]
            attr = getattr(self.model, param)
            return query.order_by(attr.desc())
        else:
            param = self.ordering_param
            attr = getattr(self.model, param)
            return query.order_by(attr)
    
    def get_pagination_params(self):
        params = {
            key: int(value)
            for key, value in self.request.values.items()
            if key in ['page', 'per_page']
        }
        return params
    
    def paginate(self, query):
        if not self.pagination_params:
            return query
        return query.paginate(**self.pagination_params)