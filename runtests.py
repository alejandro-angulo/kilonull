import os
import sys
import django
import pytest

PYTEST_ARGS = ['--cov-report', 'html', '--cov', 'kilonull',
               'tests', '--tb=short', '-s', '-rw']


def runtests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.conftest'
    django.setup()

    """
    Try to remove any existing data in the database.
    This operation fails with a ValueError if some table (or the entire database) does not exist.
    """
    try:
        django.core.management.call_command('flush', '--noinput')
    except ValueError as e:
        print("Encountered a problem while flushing the database: {error}".format(error=e))
        print("Continuing anyway...")

    django.core.management.call_command('migrate')
    sys.exit(pytest.main(PYTEST_ARGS))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        PYTEST_ARGS = ['-k', sys.argv[1]] + PYTEST_ARGS
    runtests()
