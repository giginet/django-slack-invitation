from unittest import TestCase
from django.conf import settings
from ..slack import SlackInvitationClient, SlackInvitationException
from .compatibility import Mock, patch


class SlackInvitationClientTest(TestCase):
    def setUp(self):
        self.client = SlackInvitationClient('teamname', 'dummytoken')

    def test_invite(self):
        response = Mock()
        response.json.side_effect = lambda: {'ok': True}
        response.status_code = 200

        with patch('requests.post', return_value=response) as post:
            self.assertTrue(self.client.invite(email='django-slack-invitation@kawaz.org'))

            post.assert_called_with('https://teamname.slack.com/api/users.admin.invite', data={
                'email': 'django-slack-invitation@kawaz.org',
                'token': 'dummytoken',
                'set_active': True,
            })

    def test_invite_failure(self):
        response = Mock()
        response.json.side_effect = lambda: {'ok': False, 'error': 'already_in_team'}
        response.status_code = 200

        with patch('requests.post', return_value=response) as post:
            self.assertRaises(SlackInvitationException, self.client.invite, email='django-slack-invitation@kawaz.org')

            post.assert_called_with('https://teamname.slack.com/api/users.admin.invite', data={
                'email': 'django-slack-invitation@kawaz.org',
                'token': 'dummytoken',
                'set_active': True,
            })
