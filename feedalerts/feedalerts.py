#! /usr/bin/python
# Configurable liferea feed alerts
# Because not all feeds are equal

import sys
import os
import gi
import re
gi.require_version('Notify', '0.7')
from gi.repository import GObject, Peas, PeasGtk, Gtk, Liferea, Notify
from configparser import ConfigParser

class FeedalertsConfig(ConfigParser):
    """ Plugin configuration: Enter the search text """

    def __init__(self):
        ConfigParser.__init__(self)
        self.path = os.path.expanduser('~/.local/share/liferea/plugins/')
        self.conf_file = 'feedalerts.conf'

    def load_config(self):
        self.read(self.path + self.conf_file)

class FeedalertsPlugin(GObject.Object, Liferea.ShellActivatable):
    __gtype_name__ = 'FeedalertsPlugin'

    object = GObject.property(type=GObject.Object)
    shell = GObject.property(type=Liferea.Shell)

    _shell = None

    def do_activate(self):
        self._handler_id = self.shell.props.feed_list.connect("node-updated", self.on_node_updated)

    def do_deactivate(self):
        self.shell.props.feed_list.disconnect(self._handler_id)

    def on_node_updated(self, widget, nodeTitle):
        config = FeedalertsConfig()
        config.load_config()
        searchtext=(config['Main']['Search'])
        pattern=re.compile(searchtext)
        if pattern.search(nodeTitle) != None:
            Notify.init('Liferea')
            notification = Notify.Notification.new(nodeTitle, "was updated", "face-cool")
            notification.show()
