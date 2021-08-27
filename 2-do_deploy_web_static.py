#!/usr/bin/python3
"""distributes an archive to your web servers"""

from fabric.api import *
import os


env.hosts = ['35.231.166.132', '3.85.92.97']
env.user = "ubuntu"


def do_deploy(archive_path):
    """do deploy"""

    if os.path.isfile(archive_path):
        return(False)
    try:
        name_file = archive_path.split("/")
        rm_tgz = name_file[1].split(".")

        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(rm_tgz[0]))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            name_file[1], rm_tgz[0]))

        run("rm /tmp/{}".format(name_file[1]))

        run("mv /data/web_static/releases/{}/web_static/*\
             /data/web_static/releases/{}".format(rm_tgz[0], rm_tgz[0]))

        run("rm -rf /data/web_static/releases/{}/web_static".format(rm_tgz[0]))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(rm_tgz[0]))

        return True
    except:
        return False
