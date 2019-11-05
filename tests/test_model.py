from cryptobotkit.model import Exchange, Fund
import pytest

def test_missing_attributes():
    with pytest.raises(TypeError):
        exchange = Exchange()
        fund = Fund()
