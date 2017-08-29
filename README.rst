===============
M2R Demo Editor
===============

`M2R <https://github.com/miyakogi/m2r>`_ Demo Editor with `WDOM
<https://github.com/miyakogi/wdom>`_

M2R is a markdown to reStructuredText (reST) converter, but it enables write both
markdown and reST in a single file, **directly**.
M2R also supports sphinx as its extension.

This demo-editor is made to easily experience M2R format.

* Free software: MIT license

Installation
------------

.. code::

   pip install git+https://github.com/miyakogi/m2rdemo

Usage
-----

.. code::

   python -m m2rdemo

Then open new browser window (or tab) running m2r demo editor.
Write something on the left-side text area.
It will reflected soon on the right-side preview window.

Additional Requirements
-----------------------

If `pywebview <https://github.com/r0x0r/pywebview>`_ is installed, it would be
used instead of browser.

.. code::

   pip install "pywebview[qt5]"

Change ``qt5`` depending on your platform. Details see `pywebview's document <https://github.com/r0x0r/pywebview#installation>`_.

Screenshot
----------

.. image:: https://raw.githubusercontent.com/wiki/miyakogi/m2rdemo/images/preview.png

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
