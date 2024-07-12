import datetime
from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import outdated_products


@pytest.fixture
def product_list() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 4, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 3, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "expected_result,mock_date",
    (
        (["duck"], datetime.date(2022, 2, 10)),
        (["chicken", "duck"], datetime.date(2022, 4, 10)),
        (["salmon", "chicken", "duck"], datetime.date(2022, 5, 10)),
    )
)
@mock.patch("app.main.datetime")
def test_get_product_list(
        mock_datetime: Mock,
        product_list: list[dict],
        expected_result: list[str],
        mock_date: datetime,
) -> None:
    mock_datetime.date.today.return_value = mock_date
    assert outdated_products(product_list) == expected_result
