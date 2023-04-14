from datetime import datetime, timedelta, timezone
import os
import uuid
#from backend import mail
from .models import User
from backend.utilities import Hasher, DbController#, TokenController
from flask import url_for
from flask_mail import Message

class UserDbController(DbController):
    def __init__(self):
        self.model = User
        super(UserDbController, self).__init__()

    def create(self, signup_request):
        user = self.model(
            id=str(uuid.uuid4()),
            first_name=signup_request.first_name,
            last_name=signup_request.last_name,
            email=signup_request.email,
            password=Hasher.get_password_hash(signup_request.password)
        )
        return self.create_object(user)
    
    
"""class AccountController:
    def _get_reset_token(self, user_id: int):
        payload = {
            "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=10),
            "user_id": user_id
        }
        return TokenController.encode(payload)

    def verify_reset_token(self, token):
        try:
            payload = TokenController.decode(token)
        except:
            return None
        user_id = payload.get('user_id')
        return UserDbController().get(id=user_id).first()
    
    def send_reset_email(self, user_instance):
        token = self._get_reset_token(user_instance.id)
        url = url_for('reset_token', token=token, _external=True)
        msg = Message(
            'Password Reset Request',
            sender=os.getenv('SENDER_EMAIL'),
            recipients=[user_instance.email]
        )
        msg.body = f'''To reset your password, visit the following link:
        {url}
        If you did not make this request then simply ignore this email and no changes will be made.
        '''
        mail.send(msg)"""