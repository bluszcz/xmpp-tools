import psycopg2

VCARD_XML = """
<vCard xmlns='vcard-temp' prodid='-//HandGen//NONSGML vGen v1.0//EN' version='2.0'>
    <FN>%(fn)s</FN>
    <N>
        <FAMILY>%(family)s</FAMILY>
        <GIVEN>%(given)s</GIVEN>
    </N>
    <NICKNAME>%(nickname)s</NICKNAME>
    <URL>%(url)s</URL>
    <ADR>
        <STREET></STREET>
        <EXTADD></EXTADD>
        <LOCALITY></LOCALITY>
        <REGION></REGION>
        <PCODE></PCODE>
        <CTRY>%(country)s</CTRY>
    </ADR>
    <TEL>
        <NUMBER>%(phone)s</NUMBER>
    </TEL>
    <EMAIL>
        <USERID>%(email)s</USERID>
    </EMAIL>
    <ORG>
        <ORGNAME>%(orgname)s</ORGNAME>
        <ORGUNIT>%(orgunit)s</ORGUNIT>
    </ORG>
    <TITLE>%(title)s</TITLE>
    <ROLE>%(role)s</ROLE>
    <BDAY>%(bday)s</BDAY>
    <DESC>%(desc)s</DESC>
</vCard>"""

class EJWriter(object):
    def connect_db(self, dbname='', user='', host='', password=''):
        print "EJWriter __init__"
        try:
            self.conn = psycopg2.connect(database=dbname,user=user, host=host, password=password)
            self.cur = self.conn.cursor()
        except:
            print "I am unable to connect to the database"

    def insert_user(self, username, password):
        self.cur.execute("""INSERT INTO users(username, password) VALUES (%s, %s) """, 
            (username,password))
        self.conn.commit()

    def insert_vcard(self, dict_vcard):
        text_vcard  = VCARD_XML % dict_vcard
        #self.cur.execute("""INSERT INTO vcard(username, vcard) VALUES (%s,%s)""", (dict_vcard['username'], text_vcard))
        dict_vcard['lusername'] = dict_vcard['username'].lower()
        dict_vcard['lfn'] = dict_vcard['fn'].lower()
        dict_vcard['lfamily'] = dict_vcard['family'].lower()
        dict_vcard['lfamily'] = dict_vcard['family'].lower()
        dict_vcard['lgiven'] = dict_vcard['given'].lower()
        dict_vcard['lgiven'] = dict_vcard['given'].lower()
        #dict_vcard['lmiddle'] = dict_vcard['middle'].lower()
        dict_vcard['lnickname'] = dict_vcard['nickname'].lower()
        dict_vcard['lbday'] = dict_vcard['bday'].lower()
        dict_vcard['lemail'] = dict_vcard['email'].lower()
        #dict_vcard['lctry'] = dict_vcard['ctry'].lower()
        #dict_vcard['lctry'] = dict_vcard['ctry'].lower()
        dict_vcard['lorgname'] = dict_vcard['orgname'].lower()
        dict_vcard['lorgunit'] = dict_vcard['orgunit'].lower()


        for key in dict_vcard.keys():
            print key, dict_vcard[key]
            if not dict_vcard[key]:
                
                dict_vcard[key] = ""

        self.cur.execute(""" INSERT INTO vcard_search(username, lusername, fn, lfn, family, lfamily, given, lgiven, nickname, lnickname,
            bday,lbday, orgname, lorgname, orgunit, lorgunit, email, lemail, middle,lmiddle,ctry,lctry, locality, llocality) VALUES (
            %(username)s, %(lusername)s, %(fn)s, %(lfn)s, %(family)s, %(lfamily)s, %(given)s, %(lgiven)s,  %(nickname)s, %(lnickname)s,
            %(bday)s,%(lbday)s, %(orgname)s, %(lorgname)s, %(orgunit)s, %(lorgunit)s, %(email)s,%(lemail)s, ' ',' ',' ', ' ', ' ', '')  """, dict_vcard)
        self.conn.commit()


if __name__ == "__main__":
    writer = EJWriter(dbname="ejconv", user="ejconv", host="127.0.0.1",
        password="ejconv")
    writer.insert_user("testuser", "testuser!@#666j3zu4l3c5ad")
