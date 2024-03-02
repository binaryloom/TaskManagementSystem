from rest_framework import serializers


class HyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    A serializer class that serializes Django models into hyperlinked representations,
    similar to ModelSerializer but with hyperlinks to related resources.

    Inherits:
        serializers.HyperlinkedModelSerializer

    Usage:
        Define your serializer class inheriting from this class and specify the
        Meta class with the model and fields.

    Example:
        class MyModelSerializer(HyperlinkedModelSerializer):
            class Meta:
                model = MyModel
                fields = ['id', 'name', 'url']
    """

    pass


class ModelSerializer(serializers.ModelSerializer):
    """
    A serializer class that serializes Django models into representations, typically
    used for API responses or request data manipulation.

    Inherits:
        serializers.ModelSerializer

    Usage:
        Define your serializer class inheriting from this class and specify the
        Meta class with the model and fields.

    Example:
        class MyModelSerializer(ModelSerializer):
            class Meta:
                model = MyModel
                fields = ['id', 'name']
    """

    pass
