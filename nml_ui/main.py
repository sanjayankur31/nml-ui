#!/usr/bin/env python3
"""
Main entry point for the application.

File: main.py

Copyright 2024 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


from tkinter import Tk, Menu
from tkinter import ttk
from nml_ui.app.main import file_new_callback, file_load_callback, file_exit_callback
from neuroml.utils import component_factory


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class NeuroMLGUI(object):

    """Main NeuroML GUI class"""

    def __init__(self):
        """Basic initialization"""
        # place holder object model
        self.model = component_factory("NeuroMLDocument", id="new_doc")
        self.filename = ""

        self.nmlgui = Tk()
        self.nmlgui.title("NeuroML GUI")
        self.nmlgui.option_add("*tearOff", False)

    def setup(self):
        """Setup the app"""
        # menu
        self.menubar = Menu(self.nmlgui)

        # file menu
        self.menu_file = Menu(self.menubar)
        self.menu_file.add_command(label="New", command=lambda: file_new_callback(self))
        self.menu_file.add_command(label="Load", command=lambda: file_load_callback(self))
        self.menu_file.add_command(label="Exit", command=lambda: file_exit_callback(self))

        self.menubar.add_cascade(menu=self.menu_file, label="File")
        self.nmlgui['menu'] = self.menubar

        # mainframe = ttk.Frame(nmlgui)

    def run(self):
        """Run the app.
        :returns: TODO

        """
        self.setup()
        self.nmlgui.mainloop()


def app():
    """Runner function for script end point"""
    app = NeuroMLGUI()
    app.run()
