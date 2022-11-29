import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Fake Pop Script
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fake = Faker()
topics = ['Search', 'Social', 'News', 'Games', 'Sports', 'Marketplace']

def add_topic():
	t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):
	for entry in range(N):
		# get topic for entry
		top = add_topic()

		# create fake data
		fake_url = fake.url()
		fake_date = fake.date()
		fake_name = fake.company()

		# create webpage
		webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

		# create access records
		acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
	print("populating...")
	populate(20)
	print("population complete!")