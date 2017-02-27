import os
import sys
import django
import pytest

PYTEST_ARGS = ['--cov-report', 'html', '--cov', 'kilonull',
               'tests', '--tb=short', '-s', '-rw']


def runtests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.conftest'
    django.setup()
    django.core.management.call_command('flush', '--noinput')
    django.core.management.call_command('migrate')
    sys.exit(pytest.main(PYTEST_ARGS))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        PYTEST_ARGS = ['-k', sys.argv[1]] + PYTEST_ARGS
    runtests()
