from j2reader import J2Reader

# Example blacklist - don't import them

BLACKLIST_ROSTER_ITEMS = [
	"@rss.jabberpl.org", 
	"@gg.jabberpl.org"
]

class RosterItem(J2Reader):
	pass