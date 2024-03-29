import factory
from cars import models
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    title = factory.LazyFunction(lambda: faker.name())


class CarModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CarModel

    title = factory.LazyFunction(lambda: faker.name())
    fuel_consumption = factory.LazyFunction(lambda: faker.random_number(
        digits=3) + faker.random_number(digits=1, fix_len=False) * 0.1)
    hp = factory.LazyFunction(lambda: faker.random_int(min=5, max=15))
    brand = factory.SubFactory(BrandFactory)
