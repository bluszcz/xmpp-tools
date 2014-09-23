import os
from j2reader import J2Reader
from ejwriter import EJWriter

class Authreg(J2Reader, EJWriter):
	pass
	

if __name__ == "__main__":
	filename = os.path.join(os.environ['HOME'], 'dev/ejabberd', 'jabberd2-export-authreg.csv')
	j2reader = J2Reader(filename)
	j2reader.read()

