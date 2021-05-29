import pandas.io.sql as sqlio


def load_from_db(db, data_batch: str):
    if data_batch == "validate":
        table_prefix = "test2019"
    elif data_batch == "predict":
        table_prefix = "test2020"
    else:
        table_prefix = "train"
    if data_batch == "predict":
        sql = f"""
                select t2015.code_cultu AS CODE_CULTU_2015, t2015.code_group AS CODE_GROUP_2015, t2015.centroid AS centroid,
                        t2016.code_cultu AS CODE_CULTU_2016, t2016.code_group AS CODE_GROUP_2016,
                        t2017.code_cultu AS CODE_CULTU_2017, t2017.code_group AS CODE_GROUP_2017,
                        t2018.code_cultu AS CODE_CULTU_2018, t2018.code_group AS CODE_GROUP_2018,
                        t2019.code_cultu AS CODE_CULTU_2019, t2019.code_group AS CODE_GROUP_2019
                   from {table_prefix}_2015 t2015 
                   join {table_prefix}_2016 t2016 ON t2016.centroid = t2015.centroid 
                   join {table_prefix}_2017 t2017 ON t2017.centroid = t2015.centroid 
                   join {table_prefix}_2018 t2018 ON t2018.centroid = t2015.centroid 
                   join {table_prefix}_2019 t2019 ON t2018.centroid = t2015.centroid;
            """
    else:
        sql = f"""
            select t2015.code_cultu AS CODE_CULTU_2015, t2015.code_group AS CODE_GROUP_2015, t2015.centroid AS centroid,
                    t2016.code_cultu AS CODE_CULTU_2016, t2016.code_group AS CODE_GROUP_2016,
                    t2017.code_cultu AS CODE_CULTU_2017, t2017.code_group AS CODE_GROUP_2017,
                    t2018.code_cultu AS CODE_CULTU_2018, t2018.code_group AS CODE_GROUP_2018
               from {table_prefix}_2015 t2015 
               join {table_prefix}_2016 t2016 ON t2016.centroid = t2015.centroid 
               join {table_prefix}_2017 t2017 ON t2017.centroid = t2015.centroid 
               join {table_prefix}_2018 t2018 ON t2018.centroid = t2015.centroid 
        """
    result = sqlio.read_sql_query(sql, db.conn)
    # Make columns the same format as in merger.py
    result.columns = [column.upper() if column != 'centroid' else column for column in result.columns]
    return result
