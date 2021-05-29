import pandas as pd
import os
import random


class Database:
    def __init__(self, host="localhost", port=5432, database="db_name", user="user_name", password="pswd"):
        self.conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        self.cursor = self.conn.cursor()

    def make_query(self, query):
        self.cursor.execute(query)

    def persist_predictions(self, predictions: pd.DataFrame, year: int):
        pass

    def copy_from_df(self, df, table):
        """
        Here we are going save the dataframe on disk as
        a csv file, load the csv file
        and use copy_from() to copy it to the table
        """
        # Save the dataframe to disk
        tmp_df = f"/tmp/tmp_dataframe_{random.randint(0, 9)}.csv"
        df.to_csv(tmp_df, header=False, index=False)
        f = open(tmp_df, 'r')
        cursor = self.conn.cursor()
        try:
            cursor.copy_from(f, table, sep=",")
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            os.remove(tmp_df)
            print("Error: %s" % error)
            self.conn.rollback()
            cursor.close()
            raise error
        cursor.close()
        os.remove(tmp_df)

    def close_conn(self):
        self.cursor.close()
        self.conn.close()
