from cryptobotkit.model import Exchange
import pytest

def test_missing_attributes():
    with pytest.raises(TypeError):
        exchange = Exchange()
