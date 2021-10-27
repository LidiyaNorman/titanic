# this is how we import API functions
from research import component_api_func

# this is how we import internal functions
from research.script_example import component_inner_func


def test_api_func():
    component_api_func("API")


def test_inner_func():
    component_inner_func("Inner function.")

