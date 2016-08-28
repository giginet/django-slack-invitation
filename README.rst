django-slack-invitation
=======================

.. image:: https://travis-ci.org/giginet/django-slack-invitation.svg?branch=master
    :target: https://travis-ci.org/giginet/django-slack-invitation
.. image:: https://coveralls.io/repos/github/giginet/django-slack-invitation/badge.svg?branch=master
    :target: https://coveralls.io/github/giginet/django-slack-invitation?branch=master

``django-slack-invitation`` invites users to Slack automatically when Django users are registered.


Supported python versions
    2.7, 3.3, 3.4, 3.5
Supported django versions
    1.7 - 1.10


Installation
-------------------

Install using pip

.. code:: sh

  pip install django-slack-invitation

Usage
------------------

Add ``slack_invitation`` into ``INSTALL_APPS`` in ``settings.py`` file

.. code:: python

  INSTALLED_APPS += (
      'slack_invitation',
  )

Execute ``register_slack_invitation`` on ``models.py`` or ``urls.py``.


.. code:: python

  from slack_invitation import register_slack_invitation

  register_slack_invitation()

When Django users are registered, invitation mail will send automatically.

Author
-------------------

giginet <giginet.net@gmail.com>

LICENSE
-------------------------

MIT License
