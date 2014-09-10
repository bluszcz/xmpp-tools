import psycopg2

class EJWriter(object):
    def __init__(self, dbname='', user='', host='', password=''):
        try:
            self.conn = psycopg2.connect(database=dbname,user=user, host=host, password=password)
            self.cur = self.conn.cursor()
        except:
            print "I am unable to connect to the database"

    def insert_user(self, username, password):
        self.cur.execute("""INSERT INTO users(username, password) VALUES (%s, %s) """, 
            (username,password))
        self.conn.commit()

if __name__ == "__main__":
    writer = EJWriter(dbname="ejconv", user="ejconv", host="127.0.0.1",
        password="ejconv")
    writer.insert_user("testuser", "testuser!@#666j3zu4l3c5ad")
