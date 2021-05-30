import re
import pandas as pd
import pyproj


def add_lamb_coordinates(data):
    # заменить следующее наблюдение:
    a = data[data['centroid'] == 'Point (477310.1875 6222352)'].index[0]
    data.iloc[a, 2] = 'Point (477310.1875 6222352.0)'
    pattern_coords = re.compile("\d+\.\d+")

    data['lamb_coordinates'] = data['centroid'].apply(lambda x: pattern_coords.findall(x))
    data['lamb_coordinates_tuple'] = data['lamb_coordinates'].apply(lambda x: tuple(x))
    data[['lamb_longitude', 'lamb_latitude']] = pd.DataFrame(data['lamb_coordinates'].to_list(), index=data.index)
    return data


def add_ws_coordinates(data):

    input_coder = 2154  # (lamb coords)
    output_coder = 4326  # (ws coords)
    proj = pyproj.Transformer.from_crs(input_coder, output_coder, always_xy=True)

    data['ws_coordinates'] = [*map(lambda x, y: list(proj.transform(x, y)),
                                 data['lamb_longitude'],
                                 data['lamb_latitude']
                                 )]
    data['ws_coordinates_tuple'] = data['ws_coordinates'].apply(lambda x: tuple(x))
    data[['longitude', 'latitude']] = pd.DataFrame(data['ws_coordinates'].to_list(), index=data.index)
    return data


def prepare_ws_geolocator(data):
    def get_geolocator(coord):
        return tuple([coord[1], coord[0]])
    data['ws_coordinates_geolocator'] = data['ws_coordinates'].map(get_geolocator)
    return data


def get_result_csv(data, file_name:str):
#    file_name: str = "geodata"
    path_out: str = "/home/user/PycharmProjects/pythonProject/ClassifierCrops/output/"
#    result = data[[]]  # needed columns
    data.to_csv(f"{path_out}/{file_name}.csv")  # define the route
