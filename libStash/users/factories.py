import factory
from faker import Faker
from factory.django import DjangoModelFactory
from users.models import Account, Address

fake = Faker()
Faker.seed(0)


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account

    id = factory.Sequence(lambda n: n)
    firstname = factory.Faker("first_name_nonbinary")
    lastname = factory.Faker("last_name")
    email = factory.LazyAttribute(lambda obj: "%s@example.com" % obj.lastname)
    is_active = True


class AdminAccountFactory(AccountFactory):
    is_admin = True
    is_staff = True
    is_superuser = True


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    account = factory.SubFactory(AccountFactory)
    address1 = fake.address()
    zip_code = str(fake.random_number(digits=4, fix_len=True))
    city = fake.city()
    country = fake.country()