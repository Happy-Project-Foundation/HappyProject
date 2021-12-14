from django.contrib import auth
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import  PermissionsMixin
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _


# ROLES -----------------------------------------------
STUDENT, TEACHER, DEV, DONOR, GAZER, ADMIN = 1, 2, 3, 5, 4, 0
# -----------------------------------------------------


class HappyPersonManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email or not first_name or not last_name:
            raise ValueError('Please make sure all the required attributes were passed on')
        
        email = self.normalize_email(email)
        
        user = self.model(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            **extra_fields
        )
        
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(
            self, 
            email, 
            first_name,
            last_name,
            password=None,
            **extra_fields
        ):


        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 0)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, first_name, last_name, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class HappyPerson(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('email address'), blank=False, unique=True)
    first_name = models.CharField(_('first name'), max_length=200, blank=False)
    last_name = models.CharField(_('last name'), max_length=200, blank=False)
    role = models.IntegerField(_('role'), blank=False, default=4,
        help_text=_('Role of the HappyPerson'))
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_verified = models.BooleanField(
        verbose_name="Whether person is verified",
        default=False
    )

    objects = HappyPersonManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
