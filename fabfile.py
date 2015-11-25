from __future__ import with_statement

import time

from fabric.api import env, run, task, local, lcd
from fabric.network import disconnect_all

env.password = ''  # -----> Password deployer
env.port = int  # -----> Puerto de SSH
env.host = ['']  # -----> Localhost
env.user = ''  # -----> Usuario deployer
env.host_string = ''  # -----> Host app

repo = ''
timestamp = "%s" % int(time.time() * 1000)
