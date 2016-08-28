#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


def run_tests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    base_dir = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(base_dir, 'slack_invitation'))
    sys.path.insert(0, os.path.join(base_dir, 'tests'))

    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests", "slack_invitation"])
    sys.exit(bool(failures))

if __name__ == "__main__":
    run_tests()
