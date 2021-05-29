import os

from database import Database
import data_consolidation
import feature_engineering
import models
import pathlib
import pandas as pd

DATA_DIR: str = os.getenv("DATA_DIR", r"/home/user/PycharmProjects/pythonProject/src/")
CACHE_DIR: str = os.getenv("CACHE_DIR")
DB_HOST: str = os.getenv("DB_HOST", "localhost")
DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
DB_NAME: str = os.getenv("DB_NAME", "postgres")
DB_USERNAME: str = os.getenv("DB_USER", "postgres")
DB_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")


db = Database(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD)


def load_data(path: str, data_batch: str, source: str):
    if source == "db":
        data = data_consolidation.load_from_db(db, data_batch)
    else:
        data = data_consolidation \
            .merger \
            .merge_simple_data(data_consolidation \
                               .subset_data \
                               .get_data(path, data_batch))

    # add coordinates
    data_mod = feature_engineering.coordinates.add_lamb_coordinates(data)
    data_mod = feature_engineering.coordinates.add_ws_coordinates(data_mod)

    # add rotations
    data_mod = feature_engineering.patterns.provide_culture_and_culture_group_encodings(data_mod)

    # add weather features
    data_mod = feature_engineering.weather.add_ws_weather(data_mod)

    data_mod = feature_engineering.rotations.add_rotation_info(data_mod)
    return data_mod


def load_data_and_cache(path: str, data_batch: str, cache_dir: str, source: str):
    cache_file = pathlib.Path(os.path.join(cache_dir, f"{data_batch}_{source}.csv"))
    if cache_file.exists():
        data = pd.read_csv(cache_file.name)
    else:
        data = load_data(path, data_batch, source)
        data.to_csv(cache_file.name, index=False)
    return data


def prepare_predictions_for_persisting(predictions):
    return predictions


if CACHE_DIR is None:
    data_to_predict = load_data(DATA_DIR, "predict")
else:
    data_to_predict = load_data_and_cache(DATA_DIR, "predict", CACHE_DIR)


# modelling
nn = models.neural_network.get()
predictions = nn.predict(data_to_predict)
predictions = prepare_predictions_for_persisting(predictions)
try:
    db.copy_from_df(predictions, "culture_prediction")
finally:
    db.close_conn()


