#!/usr/bin/python3
"""
distributes an archive to web servers
web_01 : 3.83.253.154
web_02 : 52.91.133.125
"""
from datetime import datetime
from fabric.api import local, run, put, env
import os

env.hosts = ['3.83.253.154', '52.91.133.125']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """function to distribute archive to web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        if put(archive_path, '/tmp/').failed is True:
            return False
        name = archive_path[9:-4]
        t_name = name + ".tgz"
        if run("mkdir -p /data/web_static/releases/{}"
               .format(name)).failed is True:
            return False
        if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
               .format(t_name, name)).failed is True:
            return False
        if run("rm /tmp/{}".format(t_name)).failed is True:
            return False
        if run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}"
               .format(name, name)).failed is True:
            return False
        if run("rm -rf /data/web_static/releases/{}/web_static"
               .format(name)).failed is True:
            return False
        if run("rm -rf /data/web_static/current").failed is True:
            return False
        if run("ln -s /data/web_static/releases/{} /data/web_static/current"
               .format(name)).failed is True:
            return False
        print("New version deployed")
        return True
    except BaseException:
        return False
