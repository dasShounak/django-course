import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from faker import Faker
from appTwo.models import User

fake = Faker()

def populate(N=5):
	for entry in range(N):

		# create fake data
		fake_fname = fake.first_name()
		fake_lname = fake.last_name()
		fake_email = fake.ascii_free_email()

		# create user
		user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]

if __name__=='__main__':
	print('Population in progress...')
	populate(40)
	print('Population complete!')