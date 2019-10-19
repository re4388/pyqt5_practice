import pytest



@pytest.mark.slow
def test_long_computation():
    pass




@pytest.mark.timeout(10, method="thread")
def test_topology_sort():
    pass



@pytest.mark.slow
@pytest.mark.timeout(10, method="thread")
def test_topology_sort():
    pass






timeout10 = pytest.mark.timeout(10, method="thread")

@timeout10
def test_topology_sort():
    pass
@timeout10
def test_remove_duplicate_points():
    pass






from mylib.testing import timeout10


@timeout10
def test_topology_sort():
    pass

@timeout10
def test_remove_duplicate_points():
    pass



import sys
import pytest

@pytest.mark.skipif(
    sys.platform.startswith("win"),
    reason="fork not available on Windows",
)
def test_spawn_server_using_fork():
    pass


import os
import pytest
@pytest.mark.skipif(
    not hasattr(os, 'fork'), reason="os.fork not available"
)
def test_spawn_server_using_fork2():
    pass


def test_shaders():
    initialize_graphics()
    if not supports_shaders():
        pytest.skip("shades not supported in this driver")
    # rest of the test code
    ...



def test_tracers_as_arrays_manual():
    try:
        import numpy
    except ImportError:
        pytest.skip("requires numpy")
        # ...


def test_tracers_as_arrays():
    numpy = pytest.importorskip("numpy")
    # ...


def test_tracers_as_arrays_114():
    numpy = pytest.importorskip("numpy", minversion="1.14")
    # ...



def test_particle_splitting():
    initialize_physics()
    import numpy
    if numpy.__version__ < "1.13":
        pytest.xfail("split computation fails with numpy < 1.13")
        # ...



def test_formula_parsing():
    tokenizer = FormulaTokenizer()

    formula = Formula.from_string("C0 * x + 10", tokenizer)
    assert formula.eval(x=1.0, C0=2.0) == pytest.approx(12.0)

    formula = Formula.from_string("sin(x) + 2 * cos(x)", tokenizer)
    assert formula.eval(x=0.7) == pytest.approx(2.1739021)

    formula = Formula.from_string("log(x) + 3", tokenizer)
    assert formula.eval(x=2.71828182846) == pytest.approx(4.0)


def test_formula_linear():
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string("C0 * x + 10", tokenizer)
    assert formula.eval(x=1.0, C0=2.0) == pytest.approx(12.0)

def test_formula_sin_cos():
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string("sin(x) + 2 * cos(x)", tokenizer)
    assert formula.eval(x=0.7) == pytest.approx(2.1739021)

def test_formula_log():
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string("log(x) + 3", tokenizer)
    assert formula.eval(x=2.71828182846) == pytest.approx(4.0)




def test_formula_parsing2():
    values = [
            ("C0 * x + 10", dict(x=1.0, C0=2.0), 12.0),
            ("sin(x) + 2 * cos(x)", dict(x=0.7), 2.1739021),
            ("log(x) + 3", dict(x=2.71828182846), 4.0),
    ]
    tokenizer = FormulaTokenizer()
    for formula, inputs, result in values:
        formula = Formula.from_string(formula, tokenizer)
        assert formula.eval(**inputs) == pytest.approx(result)


@pytest.mark.parametrize(
    "formula, inputs, result",
        [
            ("C0 * x + 10", dict(x=1.0, C0=2.0), 12.0),
            ("sin(x) + 2 * cos(x)", dict(x=0.7), 2.1739021),
            ("log(x) + 3", dict(x=2.71828182846), 4.0),
        ],
)
def test_formula_parsing(formula, inputs, result):
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string(formula, tokenizer)
    assert formula.eval(**inputs) == pytest.approx(result)



@pytest.mark.parametrize(
    "formula, inputs, result",
        [
            ("C0 * x + 10", dict(x=1.0, C0=2.0), 12.0),
            ("sin(x) + 2 * cos(x)", dict(x=0.7), 2.1739021),
            ("log(x) + 3", dict(x=2.71828182846), 4.0),
            pytest.param(
                "hypot(x, y)", dict(x=3, y=4), 5.0,
                marks=pytest.mark.xfail(reason="not implemented: #102"),
            ),
        ],
)
def test_formula_parsing(formula, inputs, result):
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string(formula, tokenizer)
    assert formula.eval(**inputs) == pytest.approx(result)



class JSONSerializer:
    def serialize_quantity(self, quantity: Quantity) -> str:
        pass
    def deserialize_quantity(self, data: str) -> Quantity:
        pass
    def serialize_pipe(self, pipe: Pipe) -> str:
        pass
    def deserialize_pipe(self, data: str) -> Pipe:
        pass


class Test:

    def test_quantity(self):
        for serializer in [
            JSONSerializer(), XMLSerializer(), YAMLSerializer()
        ]:
            quantity = Quantity(10, "m")
            data = serializer.serialize(quantity)
            new_quantity = serializer.deserialize(data)
            assert new_quantity == quantity

    def test_pipe(self):
        for serializer in [
            JSONSerializer(), XMLSerializer(), YAMLSerializer()
        ]:
            pipe = Pipe(
                length=Quantity(1000, "m"), diameter=Quantity(35, "cm")
            )
            data = serializer.serialize(pipe)
            new_pipe = serializer.deserialize(data)
            assert new_pipe == pipe



@pytest.mark.parametrize(
    "serializer_class",
    [JSONSerializer, XMLSerializer, YAMLSerializer],
)
class Test:
    def test_quantity(self, serializer_class):
        serializer = serializer_class()
        quantity = Quantity(10, "m")
        data = serializer.serialize(quantity)
        new_quantity = serializer.deserialize(data)
        assert new_quantity == quantity
    def test_pipe(self, serializer_class):
        serializer = serializer_class()
        pipe = Pipe(
            length=Quantity(1000, "m"), diameter=Quantity(35, "cm")
            )
        data = serializer.serialize(pipe)
        new_pipe = serializer.deserialize(data)
        assert new_pipe == pipe