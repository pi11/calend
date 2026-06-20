from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):

    """User profile """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to='photos/%Y/%m/%d', max_length=512, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def resend_confirmation(self):
        self.email_active = False
        self.save()


class EmailConfirm(models.Model):

    """Temporary table used to confirm users emails"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, blank=True, null=True, default="")
    publication_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class EmailTemplate(models.Model):

    """Email templates.
    Use {{ body }} tag for semantic part.

    # required templates:
      "email_confimation"
    """
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    template = models.TextField()

    def __unicode__(self):
        """Unicode method"""
        return self.name
