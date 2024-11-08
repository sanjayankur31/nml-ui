#!/usr/bin/env python3
"""
Enter one line description here.

File:

Copyright 2024 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import sys
import logging
import webbrowser
from neuroml.utils import component_factory
from pyneuroml.io import read_neuroml2_file
from tkinter import filedialog

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


def file_new_callback(app):
    """Create a new neuroml model object
    :returns: TODO

    """
    if app.model is not None:
        print("Document will be overwritten")
        # TODO: add a confirmation dialog

    app.model = component_factory("NeuroMLDocument", id="new_doc")
    # logger.info("New doc created")
    print("New doc created")


def file_load_callback(app):
    """Load a neuroml file
    :returns: TODO

    """
    filename = filedialog.askopenfilename(title="Select a NeuroML file",
                                          filetypes=[("NeuroML2", "*.nml")])
    if filename:
        if app.model is not None:
            print("Document will be overwritten")
            # TODO: add a confirmation dialog
        app.model = read_neuroml2_file(filename)
        app.filename = filename
        app.nmlgui.title(f"NeuroML GUI - {filename}")

    print(f"File loaded: {app.model}")


def file_exit_callback(app):
    """Exit the app
    :returns: TODO

    """
    if app.model is not None:
        print("Save before exit")
        # TODO: add a confirmation dialog

    sys.exit(0)


def help_docs_callback(app):
    """Open docs in a browser. """
    webbrowser.open("https://docs.neuroml.org")


def help_chat_callback(app):
    """Open docs in a browser. """
    webbrowser.open("https://matrix.to/#/!EQLdKYsJxEfGHAybdP:gitter.im?via=gitter.im&amp;via=matrix.org")
