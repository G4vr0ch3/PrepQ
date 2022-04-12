import folium
import io
import warnings
import numpy as np
import pandas as pd
import geopandas as gpd

from os.path import exists

warnings.filterwarnings("ignore")


def create(map):

	try:


		area = gpd.read_file("zones/zones.json")
		area.head(2)

		for x in area.index:
			color = np.random.randint(16, 256, size=3)
			color = [str(hex(i))[2:] for i in color]
			color = '#'+''.join(color).upper()
			area.at[x, 'color'] = color

			def style(feature):
				return {
					'fillColor': feature['properties']['color'],
					'color': feature['properties']['color'],
					'weight': 3,
					'opacity':1,
        			'fillOpacity': 0.3,
        			'interactive': False
				}

		folium.GeoJson(data=area, style_function=style).add_to(map)

		for i in range(len(area)):
			if area["id"][i] != "":
				if (exists("prepa/"+area["id"][i]+".html")):
					html = """<p>{}</p><a href="prepa/{}.html"> <button type="button" class="btn btn-primary">{}</button></a>""".format(area["infos"][i], area["id"][i], area["name"][i])
				elif (exists("prepa/"+area["id"][i]+".pdf")):
					html = """<p>{}</p><a href="prepa/{}.pdf"> <button type="button" class="btn btn-primary">{}</button></a>""".format(area["infos"][i], area["id"][i], area["name"][i])
				else:
					html = """<p>Pas de préparation de quart disponnible.</p>"""

				try:
					lon = area["geometry"][i].centroid.x
					lat = area["geometry"][i].centroid.y
					folium.Marker(location=[lat, lon], popup=html).add_to(map)
				except:
					print("No marker available")

	except:
		try:
			print("Trying old json file")

			area = gpd.read_file("zones/zones.json.old")
			area.head(2)

			for x in area.index:
				color = np.random.randint(16, 256, size=3)
				color = [str(hex(i))[2:] for i in color]
				color = '#'+''.join(color).upper()
				area.at[x, 'color'] = color

			def style(feature):
				return {
					'fillColor': feature['properties']['color'],
					'color': feature['properties']['color'],
					'weight': 1
					}

			folium.GeoJson(data=area, style_function=style).add_to(map)

			for i in range(len(area)):
				if area["id"][i] != "":
					if (exists("prepa/"+area["id"][i]+".html")):
						html = """<p>{}</p><a href="prepa/{}.html"> <button type="button" class="btn btn-primary">{}</button></a>""".format(area["infos"][i], area["id"][i], area["name"][i])
					elif (exists("prepa/"+area["id"][i]+".pdf")):
						html = """<p>{}</p><a href="prepa/{}.pdf"> <button type="button" class="btn btn-primary">{}</button></a>""".format(area["infos"][i], area["id"][i], area["name"][i])
					else:
						html = """<p>Pas de préparation de quart disponnible.</p>"""

					try:
						lon = area["geometry"][i].centroid.x
						lat = area["geometry"][i].centroid.y
						folium.Marker(location=[lat, lon], popup=html).add_to(map)
					except:
						print("No marker available")

			rfile = open("zones/zones.json.old", "r")
			file = open("zones/zones.json", "w")
			file.write(rfile.read())

		except:
			print("Error loading json file.")

	data = io.BytesIO()

def rsetmap():
	mapNew = folium.Map(location=[48.3, -4.9], zoom_start=10)

	create(mapNew)

	mapNew.save('output.html')


class MapCreator():
	mapObj = folium.Map(location=[48.3, -4.9], zoom_start=10)

	create(mapObj)

	mapObj.save('output.html')
