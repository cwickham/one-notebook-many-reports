import geopandas as gpd
import polars as pl
import matplotlib.pyplot as plt

def oregon_map(city, figsize=(12, 8), map_color='lightgrey', point_color='red', background_color='white'):
    oregon = gpd.read_file('data/oregon.geojson')
    cities = pl.read_csv('data/cities.csv')
    
    this_city = cities.filter(pl.col('city') == city).select(['lng', 'lat'])
    point = gpd.GeoDataFrame(geometry=gpd.points_from_xy(this_city['lng'], this_city['lat']), crs='WGS84')

    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(background_color)
    oregon.plot(ax=ax, color=map_color)
    point.plot(ax=ax, color=point_color, markersize=100, zorder=5)
    ax.set_axis_off()
    return ax
