from .base_resource import GenericListResource
from .mixins import ListObjectMixin, CreateObjectMixin

class ListResource(
    GenericListResource,
    ListObjectMixin,
    CreateObjectMixin
    ):
    pass