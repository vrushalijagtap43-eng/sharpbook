from sharptest.models import BaseModel,Package,Brand
import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def package(brand):
    return Package.objects.create(brand = brand,
                                  name = "fff",
                                  description = "ytyg",
                                  price = 600,
                                  discount_percentage =2,
                                  image = "http://aaaa.com"

                                  )

@pytest.fixture
def brand():
    return Brand.objects.create(
        name="Nike",
        slug = "hair1_",
        logo = "http://hairsalon.com",
        descriptions = "goog",
        primary_color = "000000",
        secondary_color = "ffffff",
        contact_email = " v@gmail.com",
        contact_phone = "3212456545",
        website =" www.com"
    )



