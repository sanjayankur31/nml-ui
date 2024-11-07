#!/usr/bin/env python3
"""
Main entry point for the application.

File: main.py

Copyright 2024 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


from tkinter import Tk
from tkinter import ttk



def app():
    """Main app method."""
    nmlgui = Tk()
    nmlgui.title("NeuroML GUI")

    mainframe = ttk.Frame(nmlgui)
    nmlgui.mainloop()
