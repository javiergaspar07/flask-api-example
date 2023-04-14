from .items_routes import ItemsDetailRoutes, ItemsRoutes
from .stores_routes import StoreDetailRoutes, StoreRoutes

url_patterns = [
    ("/stores", StoreRoutes.as_view("stores")),
    ("/stores/<string:id>", StoreDetailRoutes.as_view(f"stores-item")),

    ("/stores/<string:store_id>/items", ItemsRoutes.as_view("items")),
    ("/stores/<string:store_id>/items/<string:item_id>", ItemsDetailRoutes.as_view("items-item"))
]