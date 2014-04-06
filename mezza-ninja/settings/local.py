##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.

# By default we assume you are a developer
from dev import *

# DATABASES = {
#     "default": {
#         # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
#         "ENGINE": "django.db.backends.sqlite3",
#         # DB name or path to database file if using sqlite3.
#         "NAME": "dev.db",
#         # Not used with sqlite3.
#         "USER": "",
#         # Not used with sqlite3.
#         "PASSWORD": "",
#         # Set to empty string for localhost. Not used with sqlite3.
#         "HOST": "",
#         # Set to empty string for default. Not used with sqlite3.
#         "PORT": "",
#     }
# }
LESS_EXECUTABLE=""

run_checkers(globals())
