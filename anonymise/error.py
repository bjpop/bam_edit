from __future__ import print_function
import sys
from  program_name import PROGRAM_NAME

ERROR_MAKE_DIR = 1
ERROR_JSON_SCHEMA_DEFINE = 2
ERROR_JSON_SCHEMA_OPEN = 3
ERROR_JSON_SCHEMA_INVALID = 4
ERROR_INVALID_APPLICATION = 5
ERROR_INCOMPATIBLE_REQUEST = 6
ERROR_RANDOM_ID_ITERATIONS = 7

def print_error(message):
    print("{}: ERROR: {}".format(PROGRAM_NAME, message), file=sys.stderr)

