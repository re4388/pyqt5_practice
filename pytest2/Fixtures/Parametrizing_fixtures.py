@pytest.mark.parametrize(
    "serializer_class",
    [JSONSerializer, XMLSerializer, YAMLSerializer],
)
class Test:

    def test_quantity(self, serializer_class):
        serializer = serializer_class()
        quantity = Quantity(10, "m")
        data = serializer.serialize_quantity(quantity)
        new_quantity = serializer.deserialize_quantity(data)
        assert new_quantity == quantity

    def test_pipe(self, serializer_class):
        serializer = serializer_class()
        pipe = Pipe(
            length=Quantity(1000, "m"), diameter=Quantity(35, "cm")
        )
        data = serializer.serialize_pipe(pipe)
        new_pipe = serializer.deserialize_pipe(data)
        assert new_pipe == pipe


####################################################################################

class Test:

    @pytest.fixture(params=[JSONSerializer, XMLSerializer,
                            YAMLSerializer])
    def serializer(self, request):
        return request.param()

    def test_quantity(self, serializer):
        quantity = Quantity(10, "m")
        data = serializer.serialize_quantity(quantity)
        new_quantity = serializer.deserialize_quantity(data)
        assert new_quantity == quantity

    def test_pipe(self, serializer):
        pipe = Pipe(
            length=Quantity(1000, "m"), diameter=Quantity(35, "cm")
            )
        data = serializer.serialize_pipe(pipe)
        new_pipe = serializer.deserialize_pipe(data)
        assert new_pipe == pipe