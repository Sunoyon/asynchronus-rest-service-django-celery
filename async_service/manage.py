#!/usr/bin/env python
import os
import sys
from pprint import pformat

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.path.basename(os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + ".settings"))
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
