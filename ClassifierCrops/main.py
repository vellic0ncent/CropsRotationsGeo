import sys, os

# -------------------------
path_src: str = r"/home/user/PycharmProjects/pythonProject/src/"

path_to_scripts: list[str] = [
    os.path.abspath(r'/home/user/PycharmProjects/pythonProject/ClassifierCrops/data_consolidation'),
    os.path.abspath(r'/home/user/PycharmProjects/pythonProject/ClassifierCrops/feature_engineering'),
    os.path.abspath(r'/home/user/PycharmProjects/pythonProject/ClassifierCrops/models')]
for path in path_to_scripts:
    if path not in sys.path:
        sys.path.append(path)
# -------------------------
import data_consolidation
import feature_engineering
import models

# database connection
# db = database.Database()
# request_result = db.make_query(f"SELECT * FROM [DBName].[SCHEMAName].[TABLEName]")  # move to config

# connect to local file
train_data = data_consolidation \
    .merger \
    .merge_simple_data(data_consolidation \
                       .subset_data \
                       .get_data(path_src, "train"))

# add coordinates
train_data_mod = feature_engineering.coordinates.add_lamb_coordinates(train_data)
train_data_mod = feature_engineering.coordinates.add_ws_coordinates(train_data_mod)

# add rotations
train_data_mod = feature_engineering.patterns.provide_culture_and_culture_group_encodings(train_data_mod)

# add weather features
train_data_mod = feature_engineering.weather.add_ws_weather(train_data)

# modelling
res = models.neural_network.get(train_data)


# test it
# print(train_data_mod[:15])
# print(train_data_mod.columns)
