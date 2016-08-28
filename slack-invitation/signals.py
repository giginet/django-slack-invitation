from django.conf import settings
from django.core.exception import ImproperlyConfigured
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .slack import SlackInvitationClient, SlackInvitationException


@receiver(post_save)
def invite_to_slack(sender, instance, created, **kwargs):
    update_fields = kwargs.get('update_fields', {})
    is_active = update_fields.get('is_active', False)
    if not created and is_active:
        try:
            team = settings.get('DJANGO_SLACK_INVITATION_TEAM', None)
            token = settings.get('DJANGO_SLACK_INVITATION_TOKEN', None)
            if not team or not token:
                raise ImproperlyConfigured('Both DJANGO_SLACK_INVITATION_TEAM and DJANGO_SLACK_INVITATION_TOKEN must be set')
            client = SlackInvitationClient(team, token)
            client.invite(instance.email)
        except SlackInvitationException:
            pass
