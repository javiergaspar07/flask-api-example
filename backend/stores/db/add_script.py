def add_model_objects():
    from app import app
    from backend import db
    import uuid
    from backend.stores.db.models import Item, Store
    import random
    app.app_context().push()

    store_instance = Store(id=str(uuid.uuid4()), name="Galaxy Store IT")
    db.session.add(store_instance)
    db.session.commit()
    
    items = [
        "Table", "Samsung Tablet", "Gateway Laptop", "iPhone X",
        "Samsung J7", "Xiaomi Redmi 9A", "Xiaomi Redmi 9C", "Xiaomi Redmi 9T",
        "HP Victus Laptop", "Samsung Smart TV", "Kingston DT-50 Pendrive", "Blu-ray Sony",
    ]

    for item in items:
        item_instance = Item(
            id=str(uuid.uuid4()),
            store_id=store_instance.id,
            name=item,
            price=random.uniform(10.99, 499.99)
        )
        db.session.add(item_instance)
        db.session.commit()
    
    return store_instance