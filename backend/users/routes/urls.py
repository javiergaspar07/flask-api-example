from .auth_routes import (
    Signup,
    Login,
    RefreshToken
)

url_patterns = [
    ("/auth/signup", Signup.as_view("signup")),
    ("/auth/login", Login.as_view("login")),

    ("/token/refresh", RefreshToken.as_view("token-refresh"))
]