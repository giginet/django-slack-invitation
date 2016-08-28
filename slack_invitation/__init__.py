def register_slack_invitation():
    from django.contrib.auth.models import User
    from .signals import invite_to_slack
    from django.db.models.signals import post_save
    post_save.connect(invite_to_slack, sender=User)


