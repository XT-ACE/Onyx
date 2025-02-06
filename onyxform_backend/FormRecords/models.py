from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Set 'email_address' as the USERNAME_FIELD
    USERNAME_FIELD = 'email_address'
    
    # Remove 'email_address' from REQUIRED_FIELDS as it's now the USERNAME_FIELD
    REQUIRED_FIELDS = []  

    # Make 'email_address' unique
    email_address = models.EmailField(max_length=255, unique=True, blank=False, null=False)

    # Optional: username can still be left as non-unique and nullable for regular users
    username = models.CharField(max_length=100, blank=True, null=True, unique=False)

    # Additional fields
    title = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    citizenship = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    valid_id = models.CharField(max_length=100, blank=True, null=True)
    id_no = models.CharField(max_length=100, blank=True, null=True)
    work_industry = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # New fields
    street_address = models.CharField(max_length=255, blank=True, null=True)  # New field
    city_residence = models.CharField(max_length=255, blank=True, null=True) 
    state_residence = models.CharField(max_length=255, blank=True, null=True)
    same_address = models.BooleanField(default=False)  # Checkbox to determine if addresses are the same
    permanent_street_address = models.CharField(max_length=255, blank=True, null=True)
    permanent_city = models.CharField(max_length=100, blank=True, null=True)
    permanent_state = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True) 


    # Fix related_name conflict with the default User model
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  
        blank=True
    )

    def __str__(self):
        return self.email_address if self.email_address else self.username or "Unnamed User"
