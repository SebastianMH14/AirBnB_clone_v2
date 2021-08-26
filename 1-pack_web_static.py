#!/usr/bin/python3
"""Fabric script that generates
a .tgz archive from the contents
of the web_static"""

from fabric.api import local
from datetime import datetime


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
