#!/usr/bin/python3
"""Script that generates a '.tgz' archive from the contents
of the 'web_static' project"""

import os.path
from fabric.api import *
from datetime import datetime


def do_pack():
    """Generating a '.tgz' archive"""

    date = datetime.now()
    format = "%Y%m%d%H%M%S"

    if not os.path.isdir("versions"):
        local("mkdir versions")

    compress = local("tar -cvzf versions/web_static_{}.tgz web_static".format(
        date.strftime(format)))
    if compress.succeeded:
        return "versions/web_static_{}.tgz".format(date.strftime(format))
    else:
        return None
