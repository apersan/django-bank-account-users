from django.db import models
from localflavor.generic.models import IBANField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User as AdminUser


class User(models.Model):

    nameRegex = RegexValidator(
        regex=r'^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.\'-]+$',
        message='Only characters from A to Z are allowed.'
    )

    creator = models.ForeignKey(AdminUser, on_delete=models.CASCADE)

    firstName = models.CharField(
        max_length=35,
        verbose_name='First Name',
        help_text='First Name',
        validators=[nameRegex],
        blank=False
    )

    lastName = models.CharField(
        max_length=50,
        verbose_name='Last Name',
        help_text="Last Name",
        validators=[nameRegex],
        blank=False
    )

    iban = IBANField(unique=True)

    def __str__(self):
        return 'First Name: {0}, Last Name: {1}'.format(self.firstName, self.lastName)
