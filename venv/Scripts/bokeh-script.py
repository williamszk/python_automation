#!c:\users\willi\documents\200313_python1\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==2.0.0','console_scripts','bokeh'
__requires__ = 'bokeh==2.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==2.0.0', 'console_scripts', 'bokeh')()
    )
