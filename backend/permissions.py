from flask_jwt_extended import verify_jwt_in_request

def refresh_token_needed(
    self,
    optional: bool = False,
    fresh: bool = False,
    refresh: bool = True,
    locations = None,
    verify_type: bool = True,
    *args,
    **kwargs
):
    verify_jwt_in_request(optional, fresh, refresh, locations, verify_type)

def is_authenticated(
    self,
    optional: bool = False,
    fresh: bool = False,
    refresh: bool = False,
    locations = None,
    verify_type: bool = True,
    *args,
    **kwargs
):
    verify_jwt_in_request(optional, fresh, refresh, locations, verify_type)