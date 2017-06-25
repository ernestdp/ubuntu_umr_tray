import mechanize
import cookielib
from locale import gettext as _


class Tasks():

	def loginAndReset(self):
		# Browser
		br = mechanize.Browser()
		# Cookie Jar
		cj = cookielib.LWPCookieJar()
		br.set_cookiejar(cj)
		# Browser options
		br.set_handle_equiv(True)
		br.set_handle_gzip(True)
		br.set_handle_redirect(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		# Follows refresh 0 but not hangs on refresh > 0
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 			Firefox/3.0.1')]
		r = br.open('http://192.168.0.1/cgi-bin/getcfg.cgi?login')
		br.select_form(nr=0)
		br.form['LOGINUNAME']='admin'
		br.form['LOGINPASSWD']='poesface'
		br.submit()
		print br.response().read()

		br.open('http://192.168.0.1/cgi-bin/reset.cgi') #This is where I try to open that page... It doesn't work.
		print br.response().read()

