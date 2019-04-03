import pkg_resources  # part of setuptools
import pyfiglet


def create_app():
    version = pkg_resources.require("bizarro")[0].version
    _ = pyfiglet.figlet_format("bizarro", font="roman")
    print("{}version - {}".format(_, version))
