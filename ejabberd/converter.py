import os
from j2reader import J2Reader
from ejwriter import EJWriter

#  username |         jid          | nick | subscription | ask | askmessage | server | subscribe | type |         created_at         
# ----------+----------------------+------+--------------+-----+------------+--------+-----------+------+----------------------------
#  bluszcz  | bluszcz@bluszcz.net  |      | B            | O   |            | N      |           | item | 2014-09-23 19:11:51.370879


class Converter(J2Reader, EJWriter):
	def __init__(self, filename, dbname, user, host, password):
		self.open_file(filename)
		self.connect_db(dbname, user, host, password)



def convert_rostergroups():
	filename = os.path.join(os.environ['HOME'], 'dev/ejabberd', 'jabberd2-export-roster-groups.csv')
	converter = Converter(filename=filename, dbname="ejconv", user="ejconv", host="127.0.0.1",
        password="ejconv")
	converter.read()
	counter = 0

	dict_vcard = {}

	for header in converter.get_header():
		print counter, header
		counter += 1

	for row in converter.get_data():	
		dict_vcard['username'] =  row[0].split('@')[0]
		dict_vcard['jid'] = row[2]
	 	dict_vcard['group'] = row[3]

		converter.insert_roster_group(dict_vcard)	



	#	print row, dict_vcard
def convert_rosterusers():
	filename = os.path.join(os.environ['HOME'], 'dev/ejabberd', 'jabberd2-export-roster-items.csv')
	converter = Converter(filename=filename, dbname="ejconv", user="ejconv", host="127.0.0.1",
        password="ejconv")
	converter.read()


	counter = 0

	dict_vcard = {}


	for header in converter.get_header():
		print counter, header
		counter += 1

	for row in converter.get_data():	
		dict_vcard['username'] =  row[0].split('@')[0]
		dict_vcard['jid'] = row[2]
		dict_vcard['nick'] = row[3]

		dict_vcard['subscription'] ='N'
		dict_vcard['ask'] ='N'
		dict_vcard['server'] ='N'
		if row[4]==row[5]:
			if row[4]=='t':
				dict_vcard['subscription'] ='B'	
				print 'hello'
		converter.insert_roster_user(dict_vcard)	



		print row, dict_vcard
		

def convert_vcard()	:
	filename = os.path.join(os.environ['HOME'], 'dev/ejabberd', 'jabberd2-export-vcard.csv')
	converter = Converter(filename=filename, dbname="ejconv", user="ejconv", host="127.0.0.1",
        password="ejconv")
	converter.read()

	counter = 0

	dict_vcard = {}


	for header in converter.get_header():
		print counter, header
		counter += 1

	for row in converter.get_data():
		dict_vcard['username'] =  row[0].split('@')[0]
		dict_vcard['fn'] = row[2]
		dict_vcard['family'] = row[11]
		dict_vcard['given'] = row[12]
		dict_vcard['email'] = row[6]
		dict_vcard['phone'] = row[5]
		dict_vcard['desc'] = row[10]
		dict_vcard['nickname'] = row[3]
		dict_vcard['url'] = row[4]
		dict_vcard['title'] = row[7]
		dict_vcard['role'] = row[8]
		dict_vcard['bday'] = row[9]
		#dict_vcard['street'] = row[18]
		#dict_vcard['locality'] = row[21]
		#dict_vcard['pcode'] = row[22]
		dict_vcard['country'] = row[18]
		dict_vcard['orgname'] = row[19]
		dict_vcard['orgunit'] = row[20]
		converter.insert_vcard(dict_vcard)
		#print dict_vcard['username']
		#print VCARD_XML % dict_vcard
		#print counter,dict_vcard

def convert_users():
	filename = os.path.join(os.environ['HOME'], 'dev/ejabberd', 'jabberd2-export-authreg.csv')
	converter = Converter(filename=filename, dbname="ejconv", user="ejconv", host="127.0.0.1",
        password="ejconv")
	converter.read()

	for row in converter.rows:
		print row
		converter.insert_user(row[0], row[2])
	

if __name__ == "__main__":
	convert_rostergroups()


