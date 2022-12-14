from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(verbose_name='имя', max_length=50, blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=30, blank=True)
    object_name = models.CharField(verbose_name='Наименование объекта', max_length=50, blank=True)
    date = models.DateField(verbose_name='Дата', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    class Meta:
        ordering = ['-created']
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email
