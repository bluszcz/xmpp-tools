from j2reader import J2Reader

class Authreg(J2Reader):
	pass

j2reader = J2Reader("/tmp/jabberpl.org.authreg.csv")
j2reader.read()

