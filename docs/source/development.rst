.. _development:


Setup development environment
=============================


Source Code
-----------

::

	$ git clone https://github.com/eduardocerqueira/cd2cloud.git


Installation
------------

Option 1: Start it on RPM
`````````````````````````

For development purposes, install following dependencies:

* python = 2.7
* python-pip

* Run the following ::

    $ cd cd2cloud
    $ pip install -r requirements/devel.txt
    $ pip install -r requirements/production.txt


Option 2: Start it on Docker
````````````````````````````
**in progress**

* Install Docker: see the `official installation
  guide <https://docs.docker.com/installation/>`_ for details. Generally, it
  might be enough to run install it with ``yum`` and the run it. ::

    $ sudo yum install docker-engine
    $ sudo service docker start

* for OS with SELINUX capabilities remember to setenforce 0 before start your docker service

* Use this command to build a new image ::

    $ sudo docker build -t <YOUR_NAME>/cd2cloud <the directory your Dockerfile is located>

* Run the container ::

    $ docker run -it -d -P <YOUR_NAME>/cd2cloud /bin/bash
    $ cd2cloud --help

