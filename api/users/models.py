from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.views.decorators.debug import sensitive_variables
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    @sensitive_variables('password')
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        if len(password) < 8:
            raise ValidationError('Passwords must be at least 8 characters long')
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    @sensitive_variables('password')
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        max_length=255, unique=True,
        verbose_name=_('Email'),
        help_text=_("The user's email address acts as the username."))

    name = models.CharField(
        max_length=255, blank=True,
        verbose_name=_('Name'),
        help_text=_("A full name"),
        error_messages={
            'unique': _("A user with this username already exists.")
        })

    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Has Admin Access?'),
        help_text=_("True if the user has access to the admin page."))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return "/users/{}/".format(self.id)

    def __str__(self):
        return str(self.name) or "(Anonymous Member #{})".format(self.id)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ('email',)