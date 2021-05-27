import pandas as pd
from shapely.geometry import Point, Polygon
import geopandas as gpd
import shapely.wkt

def add_ws_weather(data):
	data = gpd.GeoDataFrame(data,
							geometry=gpd.GeoSeries.from_wkt(data['centroid'],
															crs='epsg:2154'
															).to_crs('epsg:4326'))
	#gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

	fr_phz_gdf = gpd.read_file('geojson/FR_PHZ.geojson')
	fr_phz_gdf.drop('pm_icon', axis='columns', inplace=True)

	data = gpd.sjoin(data, fr_phz_gdf, op='within', how='left')
	data.drop('index_right', axis='columns', inplace=True)

	kg_gdf = gpd.read_file('geojson/eur_kg.geojson')
	kg_gdf.drop(['Shape_Leng', 'Shape_Area', 'pnm'], axis='columns', inplace=True)

	data = gpd.sjoin(data, kg_gdf, op='within', how='left')
	data.drop('index_right', axis='columns', inplace=True)

	fr_ff_gdf = gpd.read_file('geojson/FR_ff.geojson')
	fr_ff_gdf.drop('pm_icon', axis='columns', inplace=True)

	data = gpd.sjoin(data, fr_ff_gdf, op='within', how='left')
	data.drop('index_right', axis='columns', inplace=True)

	return pd.DataFrame(data).drop('geometry', axis='columns')
