from backend.utilities import ListResource, DetailResource
from backend.utilities.filtering import Filter
from ..db.models import Store
from ..schemas.stores import StoreSchema, StoreUpdateSchema

class StoreRoutes(ListResource):
    model = Store
    schema = StoreSchema
    filter = Filter

class StoreDetailRoutes(DetailResource):
    model = Store
    schema = StoreSchema
    update_schema = StoreUpdateSchema