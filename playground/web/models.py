from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class AppUser(AbstractUser):
    OFFER_FIELD_CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    offerer = models.BooleanField(choices=OFFER_FIELD_CHOICES, default=False)
    company_name = models.CharField(max_length=255, blank=True)
    company_address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='app_users',
        related_query_name='app_user',
    )



    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='app_users',
        related_query_name='app_user',
    )



    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    picture_url = models.URLField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    preferred_sport = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.email

    @property
    def email(self):
        return self.user.email

    @property
    def company_name(self):
        return self.user.company_name

    @property
    def phone(self):
        return self.user.phone

class Field(models.Model):
    DAYS_OF_WEEK_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]

    HOURS_CHOICES = [
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
    ]

    name = models.CharField(max_length=100)
    image_url = models.URLField()
    description = models.TextField()
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK_CHOICES)
    working_time = models.CharField(max_length=5, choices=HOURS_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

