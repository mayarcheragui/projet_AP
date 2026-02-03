from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # We use AbstractUser so we keep Django's default fields 
    pass
