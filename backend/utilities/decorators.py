from functools import wraps
import pydantic

def handle_endpoint(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except pydantic.ValidationError as e:
            return e.json(), 400
        except KeyError as e:
            return {"detail": e.__repr__()}, 400
        except Exception as e:
            return {"detail": e.__str__()}, 400
    return decorator