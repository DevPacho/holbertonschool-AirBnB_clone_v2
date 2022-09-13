#!/usr/bin/python3
"""Fabric script that distributes an archive to
web servers, using the function 'do_deploy' """

import os.path
from os.path import exists
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


env.hosts = ["54.234.162.16", "54.227.109.16"]
env.user = "ubuntu"
env.key = "~/.ssh/school"


def do_deploy(archive_path):
    """Deployment process (distributing an archive to the web server"""

    if not exists(archive_path):
        return False

    try:
        file_formatted = archive_path.split(".")[0].split("/")[1]
        folder = "/data/web_static/releases/"
        final_path = "{}{}".format(folder, file_formatted)

        put(archive_path, "/tmp/{}.tgz".format(file_formatted))
        run("mkdir -p {}/".format(final_path))
        run("tar -xzf /tmp/{}.tgz -C {}/".format(file_formatted, final_path))
        run("rm /tmp/{}.tgz".format(file_formatted))
        run("mv {}/web_static/* {}".format(final_path, final_path))
        run("rm -rf {}/web_static".format(final_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(final_path))
        return True

    except Exception:
        return False
