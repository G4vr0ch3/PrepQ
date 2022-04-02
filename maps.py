import folium
import io
import pandas as pd
import geopandas as gpd

def create(map):

	try:
		area = open("zones.json", 'r')
		area = area.read()
		area = folium.GeoJson(data=area)
		area.add_to(map)

		df = gpd.read_file("zones.json")
		df.head(2)

		for i in range(len(df)):
			html = """<p>{}</p><a href="{}.html"> <button type="button" class="btn btn-primary">{}</button></a>""".format(df["infos"][i], df["id"][i], df["name"][i])
			try:
				lon = df["geometry"][i].centroid.x
				lat = df["geometry"][i].centroid.y
				folium.Marker(location=[lat, lon], popup=html).add_to(map)
			except:
				print("No marker available")

	except:
		try:
			print("Trying old json file")
			area = open("zones.json.old", 'r')
			area = area.read()
			area = folium.GeoJson(data=area)
			area.add_to(map)

			df = gpd.read_file("zones.json.old")
			df.head(2)

			for i in range(len(df)):
				html = """<p>{}</p><a href="{}.html"> <button type="button" class="btn btn-primary">{}</button></a>""".format(df["infos"][i], df["id"][i], df["name"][i])
				try:
					lon = df["geometry"][i].centroid.x
					lat = df["geometry"][i].centroid.y
					folium.Marker(location=[lat, lon], popup=html).add_to(map)
				except:
					print("No marker available")
			rfile = open("zones.json.old", "r")
			file = open("zones.json", "w")
			file.write(rfile.read())
		except:
			print("Error loading json file.")




	data = io.BytesIO()

class MapCreator():
	mapObj = folium.Map(location=[48.3, -4.9], zoom_start=10)

	create(mapObj)

	mapObj.save('output.html')
