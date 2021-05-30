from functools import reduce
import pandas as pd

def merge_simple_data(frames: list):

    # заменить сборку из цикла ниже на сборку из queries database
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=['centroid'], how='left'), frames)
    #                                                how='outer'), frames)
    df_merged.columns = ['CODE_CULTU_2015', 'CODE_GROUP_2015', 'centroid',
                         'CODE_CULTU_2016', 'CODE_GROUP_2016',
                         'CODE_CULTU_2017', 'CODE_GROUP_2017',
                         'CODE_CULTU_2018', 'CODE_GROUP_2018',
                         'CODE_CULTU_2019', 'CODE_GROUP_2019',
                         ]
    return df_merged
