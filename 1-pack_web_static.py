#!/usr/bin/python3
""" This is a fabric script to generates a .tgz archive"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """ This method will make the archive """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
