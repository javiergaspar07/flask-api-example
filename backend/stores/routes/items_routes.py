from backend.utilities import (
    DetailResource,
    ListResource
)
from ..db.models import Item, Store
from ..schemas.items import (
    ItemSchema,
    ItemDetailSchema,
    ItemUpdateSchema
)
from backend.utilities.filtering import Filter
from flask import request


class ItemsRoutes(ListResource):
    model = Item
    schema = ItemSchema
    filter = Filter
    filter_fields = ('price__gt', 'price__lt', 'store_id')
    order_fields = ('price', '-price')

    def post(self, *args, **kwargs):
        request.json['store_id'] = request.view_args.get('store_id')
        return super(ItemsRoutes, self).post(self, *args, **kwargs)


class ItemsDetailRoutes(DetailResource):
    model = Item
    lookup_field = 'item_id'
    schema = ItemDetailSchema
    update_schema = ItemUpdateSchema
    
    def get_object(self):
        store_id = request.view_args.get('store_id')
        item_id = request.view_args.get('item_id')
        store_obj = Store.query.get_or_404(store_id)
        item_obj = Item.query.filter_by(
            id=item_id,
            store_id=store_obj.id
        ).first()
        if not item_obj:
            raise Exception("Not found.")
        return item_obj