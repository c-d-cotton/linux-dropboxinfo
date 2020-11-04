#!/usr/bin/env python3
# PYTHON_PREAMBLE_START_STANDARD:{{{

# Christopher David Cotton (c)
# http://www.cdcotton.com

# modules needed for preamble
import importlib
import os
from pathlib import Path
import sys

# Get full real filename
__fullrealfile__ = os.path.abspath(__file__)

# Function to get git directory containing this file
def getprojectdir(filename):
    curlevel = filename
    while curlevel is not '/':
        curlevel = os.path.dirname(curlevel)
        if os.path.exists(curlevel + '/.git/'):
            return(curlevel + '/')
    return(None)

# Directory of project
__projectdir__ = Path(getprojectdir(__fullrealfile__))

# Function to call functions from files by their absolute path.
# Imports modules if they've not already been imported
# First argument is filename, second is function name, third is dictionary containing loaded modules.
modulesdict = {}
def importattr(modulefilename, func, modulesdict = modulesdict):
    # get modulefilename as string to prevent problems in <= python3.5 with pathlib -> os
    modulefilename = str(modulefilename)
    # if function in this file
    if modulefilename == __fullrealfile__:
        return(eval(func))
    else:
        # add file to moduledict if not there already
        if modulefilename not in modulesdict:
            # check filename exists
            if not os.path.isfile(modulefilename):
                raise Exception('Module not exists: ' + modulefilename + '. Function: ' + func + '. Filename called from: ' + __fullrealfile__ + '.')
            # add directory to path
            sys.path.append(os.path.dirname(modulefilename))
            # actually add module to moduledict
            modulesdict[modulefilename] = importlib.import_module(''.join(os.path.basename(modulefilename).split('.')[: -1]))

        # get the actual function from the file and return it
        return(getattr(modulesdict[modulefilename], func))

# PYTHON_PREAMBLE_END:}}}

def dropboxcheck():
    import subprocess

    # output = subprocess.check_output(['dropbox', 'status']).decode('latin-1')
    output = subprocess.check_output('/usr/local/bin/dropbox status', shell = True).decode('latin-1')

    if output == 'Up to date\n':
        synced = True
    else:
        synced = False

    def dropboxerrormessage(date):
        if date is None:
            date = 'No record of sync'

        message = 'Dropbox not synced since: ' + str(date) + '.\n\n Current Status:\n' + output
        importattr(__projectdir__ / Path('submodules/linux-popupinfo/displaypopup_func.py'), 'genpopup')(message, title = 'Dropbox')

    hourseconds = 60 * 60
    dayseconds = 60 * 60 * 24

    importattr(__projectdir__ / Path('submodules/truefalse-interval/truefalse-interval_func.py'), 'truefalsedo')(synced, dropboxerrormessage, [1 * hourseconds, 6 * hourseconds, 12 * hourseconds, 1 * dayseconds, 2 * dayseconds, 3 * dayseconds, 4 * dayseconds, 5 * dayseconds, 6 * dayseconds], '/tmp/linux-dropboxinfo/')


