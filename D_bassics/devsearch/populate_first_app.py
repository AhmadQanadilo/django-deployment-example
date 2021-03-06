import os
from unicodedata import name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')

import django
django.setup()

import random
from projects.models import AccessRecord, topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Serach', 'Social', 'Marketplace','News', 'Games' ]

def add_topic():
    t = topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_company = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url = fake_url, name = fake_company)[0]
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]


if __name__ == '__main__':
    print('populating scripts')
    populate(20)
    print("pop complete")