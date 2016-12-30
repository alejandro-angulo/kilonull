kilonull
========

kilonull is the Django app behind the blog on kilonull.com .

**This app requires:**
* [djangorestframework](http://www.django-rest-framework.org/)
* [django-codetalker](https://github.com/vacuus/django-codetalker)
* [django-codesnip](https://github.com/vacuus/django-codesnip)
* [django-staticprecompiler](https://django-static-precompiler.readthedocs.io/en/stable/)

Detailed documentation is in the "docs" directory.

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
