Mi Seguro Virtual
=================

Plataforma de venta de seguros virtuales

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Getting Up and Running Locally With Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The steps below will get you up and running with a local development environment. All of these commands assume you are in the root of your generated project.


Prerequisites
^^^^^^^^^^^^^

* Docker; if you don’t have it yet, follow the `installation instructions`_;
* Docker Compose; refer to the official documentation for the `installation guide`_.

.. _installation instructions: https://docs.docker.com/install/#supported-platforms
.. _installation guide: https://docs.docker.com/compose/install/

Build the Stack
^^^^^^^^^^^^^^^

* This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f local.yml build

* Generally, if you want to emulate production environment use production.yml instead. And this is true for any other actions you might need to perform: whenever a switch is required, just do it!

Run the Stack
^^^^^^^^^^^^^

* This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

* Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml up

* For connecting into a docker container, exec a command like this::

    $ docker exec -it <<container_name || container_id>> sh

* you can see containers info with this command::

    $ docker ps

* More info `docker cookiecutter instructions`_

.. _docker cookiecutter instructions: https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd MiSeguroVirtualBackend
    celery -A MiSeguroVirtualBackend.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog



Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



