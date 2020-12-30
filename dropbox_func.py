#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

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
        sys.path.append(str(__projectdir__ / Path('submodules/linux-popupinfo/')))
        from displaypopup_func import genpopup
        genpopup(message, title = 'Dropbox')

    hourseconds = 60 * 60
    dayseconds = 60 * 60 * 24

    sys.path.append(str(__projectdir__ / Path('submodules/truefalse-interval/')))
    from truefalse-interval_func import truefalsedo
    truefalsedo(synced, dropboxerrormessage, [1 * hourseconds, 6 * hourseconds, 12 * hourseconds, 1 * dayseconds, 2 * dayseconds, 3 * dayseconds, 4 * dayseconds, 5 * dayseconds, 6 * dayseconds], '/tmp/linux-dropboxinfo/')


