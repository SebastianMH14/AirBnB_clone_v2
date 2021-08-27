#!/usr/bin/python3
"""creates and distributes an archive to your
web servers, using the function deploy"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['35.231.166.132', '3.85.92.97']
env.user = "ubuntu"


def deploy():
    """final function do_pack and do_deploy"""
    pack = do_pack()
    if pack is None:
        return False
    dep = do_deploy(pack)
    return dep


def do_pack():
    """generates a tar archive"""

    try:
        name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
        path = "versions/" + name

        local("mkdir -p versions")

        local("tar -czvf " + path + " web_static")

        return path
    except:
        return None


def do_deploy(archive_path):
    """do deploy"""

    if not os.path.isfile(archive_path):
        return(False)
    try:
        name_file = archive_path.split("/")
        rm_tgz = name_file[1].split(".")

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(rm_tgz[0]))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            name_file[1], rm_tgz[0]))

        run("rm /tmp/{}".format(name_file[1]))

        run("rm -rf /data/web_static/releases/{}/web_static".format(rm_tgz[0]))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(rm_tgz[0]))

        return True
    except:
        return False
