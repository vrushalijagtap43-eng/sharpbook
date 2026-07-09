import pytest
# By default, pytest only discovers test files whose names start with test_ or end with _test.py.
@pytest.mark.django_db
def test_get_all_package(api_client,package):
    response = api_client.get("/package/")
    assert response.status_code==200
    assert len(response.data)==1
#     In Python, assert is used to verify that a condition is True. It is commonly
#     used in testing (especially with pytest) to check whether the actual result matches the expected result






