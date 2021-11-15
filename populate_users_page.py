import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","playground.settings")

import django
django.setup()

from users_page.models import Users
from faker import Faker
fakegen = Faker()
def populate(N=5):  #En este caso estamos metiendo datos random en la base de datos
                    #Pero se podria hacer esto mismo con un excel gigante de datos posta
    for entry in range(N):

        #create the fake data for the entry
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()
        #Create new webpage entry
        uss = Users.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_email)[0]


if __name__ == "__main__":
    print("populating script!")
    populate(20)
    print("populating complete")
