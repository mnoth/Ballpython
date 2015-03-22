# Michael Nothhard
# Automatically reserve racquetball court through RIT's VEMS
# Syntax:
#	python Ballpython.py <username> <password>	

import mechanize
import cookielib
import sys

def openbr():
	br = mechanize.Browser()
	jar = cookielib.LWPCookieJar()
	br.set_cookiejar(jar)

	# page redirects
	br.set_handle_redirect(True)

	# ??? The internet says to use this
	br.set_handle_equiv(True)

	# HTTP Referer info
	br.set_handle_referer(True)

	# ???
	br.set_handle_robots(False)

	# User Agent
	br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
		AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')]

	return br

def auth():
	# Create the brower and open the first page
	br = openbr()
	br.open('http://vems.main.ad.rit.edu/EMS2_Prod/PortalAuth.aspx')

	# Login
	br.select_form(nr=1)
	br.form['j_username'] = sys.argv[1]
	br.form['j_password'] = sys.argv[2]
	result = br.submit()

	# Pass through javascript workaround
	br.select_form(nr=0)
	result = br.submit()

	html = result.read()
	print html
	
if __name__ == "__main__":
	auth()



