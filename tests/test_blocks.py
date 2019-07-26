import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir + "/channelexport")
from channelexport import ChannelExporter

def main():
    exporter = ChannelExporter("TEST")
    exporter._workspace_info = {
        "team": "Dummy"
    }
    exporter._user_names["U92345678"] = "Erik Kalkoken"
    exporter._channel_names = {
        "TEST-BLOCKS": "test_blocks"
    }
    exporter.run(["test_blocks"])

if __name__ == '__main__':
    main()