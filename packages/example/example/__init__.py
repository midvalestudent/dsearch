__all__ = ['runner']

# this __init_.py provides two important objects: settings and logger
#   settings are in default.py, and are overridden and added to by a
#   user-defined settings.py; logger is a python logger with logger.info, 
#   logger.debug, etc.


###############################################################################
# simple-settings setup
###############################################################################

# default settings module
default_settings = 'default'

# Everything below this line can be used without modification
settings_module = '.'.join([__package__, default_settings])

import os as _os
if 'SIMPLE_SETTINGS' not in _os.environ:
    _os.environ['SIMPLE_SETTINGS'] = settings_module

from simple_settings import LazySettings

# make simple_settings aware of valid command-line args
LazySettings.COMMAND_LINE_ARGS = ('--settings', '-s')

# set default settings
settings = LazySettings(settings_module)

# with no args, LazySettings first consults any files specified by
#   the command-line --settings arg, then failing that, looks for the
#   file in the SIMPLE_SETTINGS env var;
user_settings = LazySettings()

# override any settings by those in user_settings; hence, with no 
#   command-line --settings arg, the default settings will be loaded
#   twice, and the second load (to user_settings) overrides the first
settings.configure(**user_settings.as_dict())


###############################################################################
# logging setup
###############################################################################

import logging as _logging
import logging.config as _logging_config
_logging_config.dictConfig(settings.LOGGING)
logger = _logging.getLogger(__name__)
