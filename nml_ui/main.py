#!/usr/bin/env python3
"""
Main entry point for the application.

File: main.py

Copyright 2024 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


from tkinter import Tk, Menu, Frame
from tkinter import ttk
from nml_ui.app.main import (file_new_callback, file_load_callback,
                             file_exit_callback, help_chat_callback,
                             help_docs_callback)
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

        self.tab_headings = ["Simulation", "Model", "Network", "Cells", "Inputs", "Channels", "Synapses"]

        self.nmlgui = Tk()
        self.nmlgui.title("NeuroML GUI")
        self.nmlgui.option_add("*tearOff", False)

    def setup(self):
        """Setup the app"""
        self.create_menus()
        self.create_tabs()

    def create_menus(self):
        """Create menus"""
        # menu
        self.menubar = Menu(self.nmlgui)

        # file menu
        self.menu_file = Menu(self.menubar)
        self.menu_file.add_command(label="New", command=lambda: file_new_callback(self))
        self.menu_file.add_command(label="Load", command=lambda: file_load_callback(self))
        self.menu_file.add_command(label="Exit", command=lambda: file_exit_callback(self))

        # help menu
        self.menu_help = Menu(self.menubar)
        self.menu_help.add_command(label="Docs", command=lambda: help_docs_callback(self))
        self.menu_help.add_command(label="Chat", command=lambda: help_chat_callback(self))

        self.menubar.add_cascade(menu=self.menu_file, label="File")
        self.menubar.add_cascade(menu=self.menu_help, label="Help")
        self.nmlgui['menu'] = self.menubar

    def create_tabs(self):
        """Create tabs """
        self.tab_notebook = ttk.Notebook(self.nmlgui)
        self.tabs = {}

        for h in self.tab_headings:
            new_tab = Frame(self.tab_notebook)
            self.tab_notebook.add(new_tab, text=h)
            self.tabs[h] = new_tab

        self.tab_notebook.pack(expand=1, fill="both")

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
