import csv,os


"""

J2Reader expects files created in following way:

COPY "vcard" TO '/tmp/jabberpl.org-vcard.csv' DELIMITER ',' CSV HEADER;

"""

class J2Reader(object):
	rows = []

	def open_file(self, filename):
		print "J2Reader __init__"
		self.filename = filename

	def get_data(self):
		return self.rows[1:]

	def get_header(self):
		return self.rows[0]


	def read(self):
		self.rows = []
		with open(self.filename, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				self.rows.append(row)
		

if __name__ == "__main__":
	filename = os.path.join(os.environ['HOME'], 'dev/ejabberd', 'jabberd2-export-authreg.csv')
	j2reader = J2Reader(filename)
	j2reader.read()
	#print j2reader.rows

