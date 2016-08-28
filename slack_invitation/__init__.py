from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .signals import invite_to_slack

def register_invite_to_slack():
    post_save.connect(invite_to_slack, sender=User)


