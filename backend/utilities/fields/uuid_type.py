import uuid

class UUIDType(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, uuid.UUID):
            try:
                uuid.UUID(v)
            except:
                raise ValueError(f"{v} is not a valid UUID")
        return str(v)