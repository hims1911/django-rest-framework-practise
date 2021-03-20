from django_seed import Seed

seeder = Seed.seeder()


from core.models import User

seeder.add_entity(User, 1, {'is_superuser' : True})
obj = User.objects.latest('id')
print("Super User Email is :", obj.email)
print("Super User Password is :", obj.password)



inserted_pks = seeder.execute()