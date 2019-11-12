=====
Usage
=====

To use acdh-django-netvis in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'netvis.apps.NetvisConfig',
        ...
    )

Add acdh-django-netvis's URL patterns:

.. code-block:: python

    from netvis import urls as netvis_urls


    urlpatterns = [
        ...
        url(r'^', include(netvis_urls)),
        ...
    ]
