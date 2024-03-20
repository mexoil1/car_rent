import pytest
from cars.models import Brand, CarModel

from tests.factories.cars import BrandFactory, CarModelFactory


@pytest.fixture()
def setup(db):
    BrandFactory(title='BMW')
    BrandFactory(title='AUDI')
    CarModelFactory(title='A5')
    CarModelFactory(title='320i')

    yield

    CarModel.objects.all().delete()
    Brand.objects.all().delete()
