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

    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, '/tmp/')
        name = archive_path[9:-4]
        t_name = name + ".tgz"
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(t_name, name))
        run("rm /tmp/{}".format(t_name))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name))
        run("rm -rf /data/web_static/current")
        run("ln -nsf /data/web_static/releases/{} /data/web_static/current"
            .format(name))
        return True
    except BaseException:
        return False
