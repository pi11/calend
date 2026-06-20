from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):

    """User profile """

    user = models.ForeignKey(User)
    picture = models.ImageField(
        upload_to='photos/%Y/%m/%d', max_length=512, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    @models.permalink
    def get_absolute_url(self):
        return ('users.views.profile', seld.id)

    def resend_confirmation(self):
        self.email_active = False
        self.save()


class EmailConfirm(models.Model):

    """Temporary table used to confirm users emails"""
    user = models.ForeignKey(User)
    token = models.CharField(max_length=100, blank=True, null=True, default="")
    publication_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username

    @models.permalink
    def get_absolute_url(self):
        return ('users.views.confirm', [self.token])


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
