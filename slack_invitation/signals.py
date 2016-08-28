from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.models import User
from .slack import SlackInvitationClient, SlackInvitationException


def invite_to_slack(sender, instance, created, update_fields={}, **kwargs):
    update_fields = kwargs.get('update_fields', {})
    is_active = update_fields.get('is_active', False)
    if created or is_active:
        try:
            team = getattr(settings, 'DJANGO_SLACK_INVITATION_TEAM', None)
            token = getattr(settings, 'DJANGO_SLACK_INVITATION_TOKEN', None)
            if not team or not token:
                raise ImproperlyConfigured('Both DJANGO_SLACK_INVITATION_TEAM and DJANGO_SLACK_INVITATION_TOKEN must be set')
            client = SlackInvitationClient(team, token)
            client.invite(instance.email)
        except ImproperlyConfigured:
            pass
        except SlackInvitationException:
            pass
