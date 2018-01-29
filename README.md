kilonull [![Build Status](https://travis-ci.org/vacuus/kilonull.svg?branch=master)](https://travis-ci.org/vacuus/kilonull)
========

kilonull is the Django app behind the blog on kilonull.com .

**This app requires:**
* [djangorestframework](http://www.django-rest-framework.org/)
* [django-staticprecompiler](https://django-static-precompiler.readthedocs.io/en/stable/)

Quick start
-----------

1.  Add "kilonull" to your INSTALLED\_APPS setting like this:
    ```python
    INSTALLED_APPS = [
        ...
        'kilonull',
    ]
    ```

2.  Run `python manage.py migrate`.

3.  Start the development server and visit http://127.0.0.1:8000/admin/ to
    manage blog posts, categories, and tags.
