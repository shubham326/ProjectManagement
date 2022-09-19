from django.db import models
from django.conf import settings
from project.managers import MyAccountManager
from django.contrib.auth.models import AbstractBaseUser

# For Token Authentication
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Employee(AbstractBaseUser):
    username        = None
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name            = models.CharField(max_length=30, unique=True, verbose_name='Employee Name')
    date_joined     = models.DateTimeField(verbose_name="date_joined",auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last_login',auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = "email"                #at the time of login what you want the user to write (username or email?)
    REQUIRED_FIELDS = []
    objects = MyAccountManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class Department(models.Model):
    department = models.CharField(max_length= 50)
    emp_name = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='created_by', verbose_name='Employee Name')

    def __str__(self):
        return str(self.emp_name)


class Project(models.Model):
    project_name = models.CharField(max_length= 50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name= 'manager_details')
    employee = models.ManyToManyField(Department, related_name= 'employee_details')                    

    def get_employee(self):
        emp = self.employee.all()
        return ",".join([str(i) for i in emp])

