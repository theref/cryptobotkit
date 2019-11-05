import pytest

from cryptobotkit.model import Exchange, Fund


def test_missing_attributes():
    with pytest.raises(TypeError):
        exchange = Exchange()
        fund = Fund()
