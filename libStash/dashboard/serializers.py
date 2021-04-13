from dashboard.models import Warehouse, WarehouseBook

from rest_framework.serializers import ModelSerializer, SlugRelatedField


class WarehouseSerializer(ModelSerializer):
    """
    Serializer for the Warehouse model.
    """

    class Meta:
        model = Warehouse
        fields = ["unique_id", "address", "phone"]


class WarehouseBookSerializer(ModelSerializer):
    """
    Serializer for the WarehouseBook model.
    """

    book = SlugRelatedField(slug_field="unique_id", read_only=True)

    class Meta:
        model = WarehouseBook
        fields = [
            "unique_id",
            "warehouse",
            "book",
            "count",
        ]
