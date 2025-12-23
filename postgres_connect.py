import psycopg

class Python_Connector:
    def __init__(self):
        self.conn= psycopg.connect(
                                    host="localhost",
                                    port=5455,
                                    dbname="postgres",
                                    user="admin",
                                    password="root"
                                    )
    def connect(self):
        self.cur= self.conn.cursor()
    def fetch_data(self):
        self.cur.execute("SELECT attributename FROM python;")
        return self.cur.fetchall()
def main():
    obj=Python_Connector()
    obj.connect()
    results=obj.fetch_data()
    for item in results:
        print(item)
if __name__ == '__main__':
    main()
