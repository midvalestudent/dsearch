# Example python project

This package contains a pattern for a python 3 project.  The 
example project has several features:

* the top-level package has a ``__main__.py`` which supplies
a CLI
* features in the top-level ``__init__.py`` install a default
settings file which can be overridden by the ``--settings`` flag
in the CLI
* logging is included, and is configured by the default settings
file
* example protobuf messages, specified by a ``.proto`` file, can
be built using a docker container
* the package has tests
