Settings
========

These are the settings that can be set in the Django project ``settings.py`` file.

.. note::
    Defaults are shown.

Set whether an ``All`` option is shown in list in sidebar.

``FILTERVIEW_SHOW_ALL = True``

Set whether filters with no matches are shown in sidebar.

``FILTERVIEW_SHOW_UNUSED_FILTERS = True``

Set parameter in URL for page.

``FILTERVIEW_PAGE_VAR = 'page'``

Set parameter in URL for search.

``FILTERVIEW_SEARCH_VAR = 'search'``

Set parameter in URL for errors.

``FILTERVIEW_ERROR_VAR = 'error'``

Add extra parameters to be ignored by filtering as a list.

``FILTERVIEW_EXTRA_IGNORED_PARAMS = None``

*Example:*

::

    FILTERVIEW_EXTRA_IGNORED_PARAMS = [
        'foo',
        'bar',
    ]
