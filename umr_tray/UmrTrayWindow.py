# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENS

from locale import gettext as _

from gi.repository import GObject,Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('umr_tray')

from umr_tray_lib import Window
from umr_tray.AboutUmrTrayDialog import AboutUmrTrayDialog
from umr_tray.PreferencesUmrTrayDialog import PreferencesUmrTrayDialog
from umr_tray.Tasks import Tasks
from time import sleep



# See umr_tray_lib.Window.py for more details about how this class works
class UmrTrayWindow(Window):
    __gtype_name__ = "UmrTrayWindow"
    

            
    def __init__(self):
        GObject.timeout_add (1, self.update_progress)


    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(UmrTrayWindow, self).finish_initializing(builder)

        #Gtk.STYLE_CLASS_PRIMARY_TOOLBAR
        self.AboutDialog = AboutUmrTrayDialog
        self.PreferencesDialog = PreferencesUmrTrayDialog


        
    def update_progress(self):
        print "update"
        self.ui.progressbar.set_fraction(0.1)      
        self.ui.progressbar.pulse()
        #tasks = Tasks()
        #tasks.loginAndReset()
        # Code for other initialization actions should be added here.

