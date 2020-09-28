from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email



class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length = 200, blank = True, null = True)
    last_name = models.CharField(max_length = 220, blank = True, null = True)
    number = models.CharField(max_length = 12, blank = True, null = True)

    def __str__(self):
        return "{}, {} - {}".format(self.first_name, self.last_name, self.user.email)

@receiver(post_save, sender=CustomUser)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")