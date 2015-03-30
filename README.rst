****************************
Sample Ecommerce Website
****************************

============
Pre Install
============

.. code:: bash

    cd ecommerce-demo
    pip install -r requirements.txt


=========
Install
=========

.. code:: bash

    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py generate
    ./manage.py runserver


===============
Running Tests
===============

.. code:: bash

    python setup.py test


================
Deployment
================

.. code:: bash
    
    ssh user@example.com
    apt-get update
    apt-get install git python-pip sqlite apache2 libapache2-mod-wsgi
    easy_install --upgrade pip
    pip install virtualenv
    cd /var/www
    git clone git@github.com:brady-vitrano/ecommerce-demo.git website
    cd website
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py generate
    chown -R www-data:www-data .


Verify the website
------------------
Before you continue, I highly suggest you verify the site is working by running it manually.
``./manage.py runserver 0.0.0.0:8000`` and visit the url on port ``8000``


Generate new auth information
-----------------------------
Change the following in ``settings.py``

.. code:: bash

    AUTH_TOKEN = "some random string"
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ["example.com"]

Change Django Secret Key
------------------------
``secret.txt``


Edit Apache VirtualHost
-----------------------

.. code:: bash

    vim /etc/apache2/sites-available/000-default.conf

VirtualHost Settings
--------------------

.. code:: xml

    <VirtualHost *:80>
        ServerAdmin webmaster@localhost

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        Alias /static/ /var/www/website/website/static/

        <Directory /var/www/website/website/static>
            Require all granted
        </Directory>
        WSGIScriptAlias / /var/www/website/website/wsgi.py
        WSGIDaemonProcess example.com python-path=/var/www/website:/var/www/website/env/lib/python2.7/site-packages
        WSGIProcessGroup example.com
        <Directory /var/www/website/website>
           <Files wsgi.py>
               Require all granted
           </Files>
       </Directory>
    </VirtualHost>

Restart Apache
--------------

.. code:: bash

    service apache2 restart

