from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

# from django.db import models

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **other_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    
    # choices variables for 'state'
    # state_choices = (
    #     ('1', 'DC'),
    #     ('2', 'VA'),
    #     ('3', 'MD')
    # )


    # User fields
    email = models.EmailField('email', unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    street_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True) # add choices=state_choices to enable dropdown menu in admin area user edit. But this cause problem getting value from website user registration
    zip_code = models.CharField(max_length=5, blank=True)
    is_driver = models.BooleanField(default=False)
    
    # location = models.PointField(geography=True, default=Point(0.0, 0.0))
    location = models.PointField(geography=True, blank=True, null=True)
    # address = u'%s %s %s %s %s %s' % (self.a2, self.a3, 
    
    def save(self, *args, **kwargs):
        """
            Create Model field (i.e. location) based on other fields
            Source: https://stackoverflow.com/questions/22157437/model-field-based-on-other-fields
            Source if using Google API: https://stackoverflow.com/questions/58468346/geocoding-with-geopy-and-importexport-in-django
        """


        address = ", ".join([self.street_address, self.city, self.state, self.zip_code])
        print(address)

        # Prepare geocoder API
        nominatim_obj = Nominatim(user_agent = 'gwcarpool')
        geocode_obj = nominatim_obj.geocode(address)

        # Get Coordinate from address
        if geocode_obj:
            latitude = geocode_obj.latitude
            longitude = geocode_obj.longitude
            self.location = Point(longitude, latitude)
            print(self.location)
        # geocoder = RateLimiter(nominatim_obj.geocode, min_delay_seconds=1)

        super(Account, self).save(*args, **kwargs) # Call the "real" save() method.

    # User fields: Get latitude & longitude using address
    # address = ", ".join([street_address, city, state, zip_code])
    # location = geocoder.geocode(address)
    # lat = location.latitude
    # long = location.longitude


    # Required fields for django custom form
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()

    def __str__(self):
        return str(self.pk)

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, password=None, **other_fields):
#         """ Creates and saves a User """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#             first_name = first_name,
#             last_name = last_name,
#             **other_fields
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, first_name, last_name, password=None, **other_fields):
#         """ Creates and saves a superuser """
#         user = self.create_user(
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#             password=password,
#         )
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class Account(AbstractBaseUser):
#     #user: models.ForeignKey(User, on_delete=models.CASCADE) # models.CASCADE = delete all schedule related to the deleted User
#     email = models.EmailField(verbose_name='email', unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)

#     # Required fields for django custom form
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     objects = MyAccountManager()

#     def __str__(self):
#         # This is what shows as each row's name when you look from django admin db
#         return str(self.email)

#     def has_perm(self, perm, obj=None):
#         return self.is_staff

#     def has_module_perms(self, app_label: str) -> bool:
#         return True
