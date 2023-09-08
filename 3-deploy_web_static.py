#!/usr/bin/python3
"""
fabric script that creates and distributes
an archive to the web servers
"""
from datetime import datetime
from fabric.api import local, run, put
import os

env.hosts = ['3.83.253.154', '52.91.133.125']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """function to make .tgz archive using fabric"""

    nw = datetime.now().strftime("%Y%m%d%H%M%S")
    ar_name = "web_static_" + nw + ".tgz"
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(ar_name))
        return "/versions/{}".format(ar_name)
    except BaseException:
        return None


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
    except Exception:
        return False


def deploy():
    """function to make archive and deploy"""

    try:
        path = do_pack()
    except Exception:
        return False
    do_deploy(path)
