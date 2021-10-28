from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

'''
class UserManager(BaseUserManager):
    def _create_user(self, username, password):
        user = self.model(
            username = username,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, password=None):
        return self._create_user(username,password)

    def create_superuser(self, username, password=None):
        return self._create_user(username,password)
'''

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    id        = models.BigAutoField(primary_key=True)
    username  = models.CharField('Username',max_length = 255, unique = True)
    password  = models.CharField('Password', max_length = 256)
    is_staff  = models.BooleanField(default = True)
    is_admin  = models.BooleanField(default= True)
    is_active = models.BooleanField(default = True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    
    USERNAME_FIELD = 'username' 