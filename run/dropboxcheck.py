#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/../')

sys.path.append(str(__projectdir__))
from dropbox_func import dropboxcheck
dropboxcheck()
