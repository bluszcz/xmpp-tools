import psycopg2


class EJWriter(object):
	def __init__(self, dbname='', user='', host='', password=''):
		try:
    		self.conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
		except:
    		print "I am unable to connect to the database"