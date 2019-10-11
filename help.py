#!/usr/bin/env python
"""
Usage: %(scriptName)s

This describes the script.
"""

import sys
if len(sys.argv) < 2:
   print(__doc__ % {'scriptName' : sys.argv[0].split("/")[-1]})
   sys.exit(0)
