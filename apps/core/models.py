from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

class UserManager(BaseUserManager):
    """
    Model manager for User model without username field
    """
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """
        Create a User with the given email and password
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create a SuperUser with the given email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Store a custom user
    """

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "auth_user"
    
    def __str__(self):
        return self.email


class ProxyUser(User):

    class Meta:
        app_label = "auth"
        proxy = True
        verbose_name = "User"
        verbose_name_plural = "Users"


class ProxyGroup(Group):

    class Meta:
        app_label = "auth"
        proxy = True
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class TimeStampedModel(models.Model):
    """
    Abstract base class which store a creation and modification date and time
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeStampedAuthModel(TimeStampedModel):
    """
    Abstract base class which store a creation and modification user
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
                                   related_name="%(app_label)s_%(class)s_created_by")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
                                    related_name="%(app_label)s_%(class)s_modified_by")

    class Meta:
        abstract = True

