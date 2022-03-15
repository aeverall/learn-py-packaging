from learn_py_packaging import toy_module

def test_power():
    assert toy_module.power(3,4) == 81
    assert toy_module.power(2,10) == 1024
