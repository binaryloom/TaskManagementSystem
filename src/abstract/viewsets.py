from rest_framework import viewsets


class ModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `list()`, `create()`, `retrieve()`, `update()`,
    `partial_update()`, and `destroy()` actions for working with a model.

    Inherits:
        viewsets.ModelViewSet

    Usage:
        Define your viewset class inheriting from this class and specify the queryset
        and serializer_class attributes.

    Example:
        class MyModelViewSet(ModelViewSet):
            queryset = MyModel.objects.all()
            serializer_class = MyModelSerializer
    """

    pass
