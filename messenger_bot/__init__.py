import pkg_resources  # part of setuptools
import pyfiglet


def create_app():
    version = pkg_resources.require("messenger-bot-library")[0].version
    print("{}version - {}".format(pyfiglet.figlet_format("basement", font="roman"), version))
