class Database():
    def __init__(self, host="localhost", database="db_name", user="user_name", password="pswd"):
        self.conn = psycopg2.connect(database=database, user=user, password=password)
        self.cursor = self.conn.cursor()

    def make_query(self, query):
        self.cursor.execute(query)

    def close_conn(self):
        self.cursor.close()
        self.conn.close()
