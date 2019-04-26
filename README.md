=================
Sennder
=================

-----------------
Development setup
-----------------

Install required system packages:

.. code-block:: bash

    $ sudo apt-get install python3-pip
    $ sudo apt-get install python-dev
    $ sudo apt-get install libpq-dev

Create www directory where project sites and environment dir

.. code-block:: bash

    $ mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin
    
Install virtualenvwrapper

.. code-block:: bash

    $ sudo pip3 install virtualenvwrapper
    $ sudo pip3 install --upgrade virtualenv
    
Add these to your bashrc virutualenvwrapper work

.. code-block:: bash

    export WORKON_HOME=/var/envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
    export IS_LOCAL=True
    source /usr/local/bin/virtualenvwrapper.sh
    
Create virtualenv

.. code-block:: bash

    $ cd /var/envs && mkvirtualenv --python=/usr/bin/python3 sennder
    
Install requirements for a project.

.. code-block:: bash

    $ cd /var/www/sennder && pip install -r requirements.txt

Install Memcached
    
    sudo apt-get update
    sudo apt-get install memcached
    sudo apt-get install libmemcached-tools
    

Run Project
    
    python manage.py runserver
    
Run Tests

    python manage.py test