import pkg_resources  # part of setuptools


def create_app():
    version = pkg_resources.require("bizarro")[0].version
    print("bizarro - {}".format(version))
