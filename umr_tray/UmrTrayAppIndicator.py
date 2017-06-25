# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _
from gi.repository import Gtk # pylint: disable=E0611
from gi.repository import AppIndicator3 as appindicator
from umr_tray.Tasks import Tasks
from gi.repository import Notify

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('umr_tray')

# See umr_tray_lib.Window.py for more details about how this class works
class UmrTrayAppIndicator():

    
    def show(self): # pylint: disable=E1002
        ind = appindicator.Indicator.new (
                        "umr-tray-client",
                        "/home/ernest/Pictures/0.png",
                        appindicator.IndicatorCategory.APPLICATION_STATUS)
        ind.set_status (appindicator.IndicatorStatus.ACTIVE)

        #ind.set_attention_icon ("indicator-messages-new")
 
        # create a menu
        menu = Gtk.Menu()
 
        # create some
        restart_item = Gtk.MenuItem("Restart")
        menu.append(restart_item)
        restart_item.show()
        restart_item.connect("activate", self.on_mnu_restart_activate)

        settings_item = Gtk.MenuItem("Settings")
        menu.append(settings_item)
        settings_item.show()
        settings_item.connect("activate", self.on_mnu_settings_activate)
 
        # show the items
        ind.set_menu(menu)
        Gtk.main()

    def on_mnu_settings_activate(self, widget, data=None):
        print 'setting'

    def on_mnu_restart_activate(self, widget, data=None):

        Notify.init('UMR AppIndicator')
        notification = Notify.Notification.new(
            'UMR Router',
            'Restarting Dovado UMR',
            'Restarting Dovado UMR')
        notification.show()
        tasks = Tasks()
        tasks.loginAndReset()
    
	    # try the icon-summary case
	    Notify.init('UMR AppIndicator')
        notification = Notify.Notification.new(
            'UMR Router',
            'Restart in 60 seconds',
            'Restart in 60 seconds')
        notification.show()
    
