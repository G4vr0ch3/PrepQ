import folium
import io
import pandas as pd
import geopandas as gpd

def create(map):
	area = open("zones.json", 'r')
	area = area.read()
	area = folium.GeoJson(data=area)
	area.add_to(map)

	df = gpd.read_file("zones.json")
	df.head(2)

	for i in range(len(df)):
		html = """<p>{}</p><a href="{}.html"> <button type="button" class="btn btn-primary">{}</button></a>""".format(df["infos"][i], df["id"][i], df["name"][i])
		lon = df["geometry"][i].centroid.x
		lat = df["geometry"][i].centroid.y

		folium.Marker(location=[lat, lon], popup=html).add_to(map)


	data = io.BytesIO()

class MapCreator():
	mapObj = folium.Map(location=[48.3, -4.9], zoom_start=10)

	create(mapObj)

	mapObj.save('output.html')
