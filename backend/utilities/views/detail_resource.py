from .base_resource import GenericDetailResource
from .mixins import DetailObjectMixin, UpdateObjectMixin, DestroyObjectMixin


class DetailResource(
    GenericDetailResource,
    DetailObjectMixin,
    UpdateObjectMixin,
    DestroyObjectMixin
    ):
    pass