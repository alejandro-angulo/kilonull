import os
import sys
import django
import pytest

from django.conf import settings
from django.test.utils import get_runner

PYTEST_ARGS = ['--cov-report', 'html', '--cov', 'kilonull',
               'tests', '--tb=short', '-s', '-rw']


def runtests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.conftest'
    django.setup()
    sys.exit(pytest.main(PYTEST_ARGS))


if __name__ == '__main__':
    runtests()
