import csv

class J2Reader(object):
	def __init__(self, filename):
		self.filename = filename

	def read(self):
		with open(self.filename, 'rb') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				print row

if __name__ == "__main__":
	j2reader = J2Reader("/tmp/jabberpl.org.authreg.csv")
	j2reader.read()

