# -*- coding=utf-8 -*-
import pytest

from src.calculator import calculator

calculator = calculator()


@pytest.fixture(scope="session")
def build_object():
    print("Calculator initialize")
    return 