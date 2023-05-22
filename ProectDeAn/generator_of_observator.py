from faker import Faker
import random

fake = Faker(locale='ro_RO')
nume_generare = [fake.first_name() for _ in range(5)]

# for nume in nume_generare:
#     print(nume)
#     print()