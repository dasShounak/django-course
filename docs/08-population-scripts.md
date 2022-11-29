# Django

## 8/ Populating Websites with Fake Data

---

### 8.1 Install Faker library

```bash
pip install Faker
```

Faker doc: https://faker.readthedocs.io

### 8.2 Create the populating script

1. Make a new file `populate_first_app.py`, preferably in the root directory of the project

2. First we need to tell the application which settings to use when running the s. 

   ```python
   import os
   os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
   ```

   This sets the value of the environment variable `DJANGO_SETTINGS_MODULE` to the `settings.py` file of the project.

3. Setup django

   ```python
   import django
   django.setup()
   ```

4. First, import the libraries.

   ```py
   import random
   from first_app.models import AccessRecord,Webpage,Topic
   from faker import Faker
   ```

   Now, create a Faker object

   ```py
   fake = Faker()
   ```

5. Define a function to generate some topics

   ```py
   topics = ['Search', 'Social', 'News', 'Games', 'Sports', 'Marketplace']
   
   def add_topic():
   	t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
   	t.save()
   	return t
   ```

   The `get_or_create()` looks up an object with the given arguments and creates one if necessary. It returns a tuple `(object, created)` where `object` is the retrieved or created object and `created` is a boolean specifying whether a new object was created or not.

6. Define the population function

   ```py
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
   ```

   The `[0]` is necessary since we only need the object.

7. Call the function

   ```py
   if __name__ == '__main__':
   	print("populating...")
   	populate(20)
   	print("population complete!")
   ```

8. Run the script.

   ```bash
   python populate_first_app.py
   ```

   Login to the django admin to see the fake data generated.