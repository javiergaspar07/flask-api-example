from datetime import timedelta
from flask import Flask

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    JWT_SECRET_KEY = "5791628bb0b13ce0c676dfde280ba245"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

class APIRouter:
    def __init__(self, api: Flask = None):
        self.api = api
    
    def init_app(self, api: Flask):
        self.api = api
        self.add_resources()

    def add_resources(self):
        if not self.api:
            raise Exception("Api instance needed to add resources.")
        
        resources = self.get_resources()
        for resource in resources:
            if not len(resource) == 2:
                raise Exception("Resources register must have 2 arguments (url and view)")
            
            self.api.add_url_rule(resource[0], view_func=resource[1])
    
    def get_resources(self):
        from backend.users.routes import url_patterns as user_urls
        from backend.stores.routes import url_patterns as store_urls
        resources = store_urls + user_urls
        return resources