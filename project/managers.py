# Create your models here.
from django.contrib.auth.base_user import BaseUserManager

class MyAccountManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users should have an email")

        user = self.model(
            email=self.normalize_email(email),
            # normalize means it will convert all the characters in email to lowercase

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self ,email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            # normalize means it will convert all the characters in email to lowercase
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

