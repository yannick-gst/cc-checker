==========
cc-checker
==========

**cc-checker** is a credit card validator written in Python 3.

Installation
============
**cc-checker** can be installed as a command line tool by running ``pip3 install .``, where . is the directory where the project has been checked out.
To run without installing as a package, simply run ``python3 cc_checker/main.py``.

Usage
=====
Running ``cc-checker -h`` (if installed) orr ``python2 cc_checker/main.py`` (if not installed) will display the following:

.. code-block:: console

    usage: main.py [-h] [-l LISTEN] [-p PORT]

    Run an HTTP server that validates credit card numbers

    options:
      -h, --help            show this help message and exit
      -l LISTEN, --listen LISTEN
                            Specifies the address the server should listen ono
      -p PORT, --port PORT  Specifies the port the server should listen on

The address defaults to 0.0.0.0, and the port defaults to 8080.

Example output
==============

.. code-block:: console

    curl -X GET 'http://0.0.0.0:8080/4263982640269299'
    {"Credit card number": "4263982640269299", "Valid": true, "Issuing Network": "Visa"}

Testing
=======
To run tests, one can run ``make``. This will install the required poackages and run the unit tests located in the ``./tests`` directory.