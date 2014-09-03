#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright (C) 2014 Rafal bluszcz Zawadzki

    This small script is just a bit modified SleekXMPP example
    which I found here: http://sleekxmpp.com/getting_started/sendlogout.html
"""


"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz

    See https://github.com/fritzy/SleekXMPP/blob/develop/LICENSE
    for copying permission.
"""

import sys
import logging
import getpass
from optparse import OptionParser

import sleekxmpp

# Python versions before 3.0 do not use UTF-8 encoding
# by default. To ensure that Unicode is handled properly
# throughout SleekXMPP, we will set the default encoding
# ourselves to UTF-8.
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input


exit_status = 2
class NagiosCheck(sleekxmpp.ClientXMPP):

    """
    A basic SleekXMPP bot that will log in, send a message,
    and then log out.
    """

    test_status = 2
    test_desc = "CRITICAL"

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password, )

        # The message we wish to send, and the JID that
        # will receive it.

        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can initialize
        # our roster.
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("failed_auth", self.failed_auth)

    def failed_auth(self, event):
        pass

    def start(self, event):
        """
        Process the session_start event.

        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.

        Arguments:
            event -- An empty dictionary. The session_start
                     event does not provide any additional
                     data.
        """
        try:
            self.send_presence()
            self.get_roster()
        except:
            self.test_status = 2 
            return 2

        #self.send_message(mto=self.recipient,
        #                  mbody=self.msg,
        #                  mtype='chat')

        # Using wait=True ensures that the send queue will be
        # emptied before ending the session.
        self.test_status = 0
        self.test_desc = "OK"
        self.disconnect(wait=True)
        return 0
        
if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.CRITICAL, default=logging.CRITICAL)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)

    # JID and password options.
    optp.add_option("-j", "--jid", dest="jid",
                    help="JID to use")
    optp.add_option("-p", "--password", dest="password",
                    help="password to use")
    opts, args = optp.parse_args()

    # Setup logging.
    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')

    if opts.jid is None:
        opts.jid = raw_input("Username: ")
    if opts.password is None:
        opts.password = getpass.getpass("Password: ")
    # Setup the EchoBot and register plugins. Note that while plugins may
    # have interdependencies, the order in which you register them does
    # not matter.
    xmpp = NagiosCheck(opts.jid, opts.password)
    #xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0199') # XMPP Ping

    # If you are working with an OpenFire server, you may need
    # to adjust the SSL version used:
    # xmpp.ssl_version = ssl.PROTOCOL_SSLv3

    # If you want to verify the SSL certificates offered by a server:
    # xmpp.ca_certs = "path/to/ca/cert"

    # Connect to the XMPP server and start processing XMPP stanzas.
    if xmpp.connect(reattempt=False):
        # If you do not have the dnspython library installed, you will need
        # to manually specify the name of the server if it does not match
        # the one in the JID. For example, to use Google Talk you would
        # need to use:
        #
        # if xmpp.connect(('talk.google.com', 5222)):
        #     ...
        xmpp.process(block=True)
        print "XMPP %s " % xmpp.test_desc
        sys.exit(xmpp.test_status)
    else:
        print("XMPP CRITICAL Can't connect")
        sys.exit(2)
