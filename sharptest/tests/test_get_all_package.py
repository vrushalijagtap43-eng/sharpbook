import pytest
from decimal import Decimal
# By default, pytest only discovers test files whose names start with test_ or end with _test.py.
@pytest.mark.django_db
def test_get_all_package(api_client,package):
    response = api_client.get("/package/")
    assert response.status_code==200
    assert len(response.data)==1

    data = response.data[0]

    assert data["name"] == package.name
    assert data["description"] == package.description
    # assert data["price"] == package.price
    assert Decimal(data["price"]) == package.price
    assert Decimal(data["discount_percentage"]) == package.discount_percentage
    assert data["image"] == package.image
    assert data["brand"] == package.brand.id






