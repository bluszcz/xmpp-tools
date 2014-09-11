import os
from j2reader import J2Reader

class Authreg(J2Reader):
	pass
	

if __name__ == "__main__":
	filename = os.path.join(os.environ['HOME'], 'dev/ejabberd', 'jabberpl.org.authreg.csv')
	j2reader = J2Reader(filename)
	j2reader.read()

