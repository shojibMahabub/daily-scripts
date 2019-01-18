#!/usr/bin/env python3

'''
This software is able to run vscode and lammp server
GUI in linux based system
=======================================================
Autor         : Mahabub Elahi
contact       : shojibmahabub630@gmail.com
version       : 1.0
license       : MIT
documentation :
=======================================================
'''

import os
import platform
import getpass

'''
Initializing os architecture and user name
=======================================================
'''
# detecting os architecture
pf = platform.architecture()

# getting current user name
user = getpass.getuser()

'''
Running server and vscode
=======================================================

# running vscode

running vscode in sudo mode is neccessary because
it needs to manipulate files which requiers root
permission. This can be improved.
'''
run_vscode = 'sudo code --user-data-dir="/home/{}/vscode-root/.vscode"'.format(user)
os.system(run_vscode)

# choosing right file for os architecture
if (pf[0] == '64bit'):
    var = 'manager-linux-x64.run'
else: var = 'manager-linux.run'

# running server
run_server = 'sudo /opt/lampp/{}'.format(var)
os.system(run_server)
