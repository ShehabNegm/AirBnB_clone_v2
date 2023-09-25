#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents
of web_static folder of AirBnB Clone repo
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """function to make .tgz archive using fabric"""

    nw = datetime.now().strftime("%Y%m%d%H%M%S")
    ar_name = "web_static_" + nw + ".tgz"
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(ar_name))
        return "versions/{}".format(ar_name)
    except BaseException:
        return None
