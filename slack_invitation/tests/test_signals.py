from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from slack_invitation import register_slack_invitation
from .compatibility import Mock, patch


class SlackInvitationSignalTest(TestCase):
    def setUp(self):
        register_slack_invitation()

    @override_settings(DJANGO_SLACK_INVITATION_TEAM='teamname', DJANGO_SLACK_INVITATION_TOKEN='dummytoken')
    def test_user_is_activated(self):
        response = Mock()
        response.json.side_effect = lambda: {'ok': True}
        response.status_code = 200

        with patch('requests.post', return_value=response) as post:
            user = User.objects.create_user('John', 'django-slack-invitation@kawaz.org', 'password')
            self.assertTrue(user.is_active)

            post.assert_called_with('https://teamname.slack.com/api/users.admin.invite', data={
                'email': 'django-slack-invitation@kawaz.org',
                'token': 'dummytoken',
                'set_active': True,
            })

    @override_settings(DJANGO_SLACK_INVITATION_TEAM=None, DJANGO_SLACK_INVITATION_TOKEN=None)
    def test_token_is_not_set(self):
        response = Mock()
        response.json.side_effect = lambda: {'ok': True}
        response.status_code = 200

        with patch('requests.post', return_value=response) as post:
            User.objects.create_user('John', 'django-slack-invitation@kawaz.org', 'password')

            post.assert_not_called()
