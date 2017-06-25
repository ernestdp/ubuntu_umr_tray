# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from gi.repository import GObject,Gtk # pylint: disable=E0611

from umr_tray_lib.helpers import get_builder

import gettext
from gettext import gettext as _
gettext.textdomain('umr-tray')

class ProgressDialog(Gtk.Dialog):
    __gtype_name__ = "ProgressDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated ProgressDialog object.
        """
        builder = get_builder('ProgressDialog')
        new_object = builder.get_object('progress_dialog')
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called when we're finished initializing.

        finish_initalizing should be called after parsing the ui definition
        and creating a ProgressDialog object with it in order to
        finish initializing the start of the new ProgressDialog
        instance.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.ui = builder.get_ui(self)
        GObject.timeout_add(60, self.on_timeout, None)
        self.activity_mode = False

    
 
    def on_timeout(self, user_data):
        """
        Update value on the progress bar
        """
        if self.activity_mode:
            self.ui.progressbar.pulse()
        else:
            new_value = self.ui.progressbar.get_fraction() + 0.01

            if new_value > 1:
                new_value = 0

            self.ui.progressbar.set_fraction(new_value)

        # As this is a timeout function, return True so that it
        # continues to get called
        return True

    def on_btn_ok_clicked(self, widget, data=None):
        """The user has elected to save the changes.

        Called before the dialog returns Gtk.ResponseType.OK from run().
        """
        pass

    def on_btn_cancel_clicked(self, widget, data=None):
        """The user has elected cancel changes.

        Called before the dialog returns Gtk.ResponseType.CANCEL for run()
        """
        pass


if __name__ == "__main__":
    dialog = ProgressDialog()
    dialog.show()
    Gtk.main()
