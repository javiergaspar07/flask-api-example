from backend.utilities import BaseResource
from backend import permissions
from ..accounts import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    unset_jwt_cookies,
    current_user,
    user_identity_lookup,
    user_lookup_callback
)
from ..db.db_controllers import UserDbController
from ..schemas import SignupRequest, SignupResponse, LoginRequest, LoginResponse
from flask import request, make_response


class RefreshToken(BaseResource):
    permissions = [permissions.refresh_token_needed]

    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return make_response({"access_token": access_token}, 200)


class Signup(BaseResource):
    def post(self):
        request_obj = SignupRequest(**request.json)
        user = UserDbController().create(request_obj)
        response = SignupResponse.from_orm(user)
        return make_response(response.dict(), 201)


class Login(BaseResource):
    def post(self):
        request_obj = LoginRequest(**request.json)
        user = request_obj.context.get('user')
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        response = LoginResponse(access_token=access_token, refresh_token=refresh_token)
        return make_response(response.dict(), 200)