from types import SimpleNamespace

import pytest

from api.controllers import Delivery


@pytest.mark.parametrize(
    ("quantities", "distance", "expected_fee"),
    [
        ([2, 2], 3, 3.50),       # Default fee
        ([2, 2, 2], 4, 5.00),    # Medium order and distance
        ([5, 5, 1], 6, 7.50),    # Large order and distance
        ([5, 5], 6, 5.00),       # Exactly 10 items does not qualify for high fee
        ([2, 2, 2], 3, 3.50),    # Distance must be greater than 3 for medium fee
    ],
)
def test_delivery_fee(quantities, distance, expected_fee):
    order = [SimpleNamespace(quantity=quantity) for quantity in quantities]

    assert Delivery.calculate(order, distance) == expected_fee
