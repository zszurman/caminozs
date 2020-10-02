from folium import folium

import markers
import methods
import trasyPlugin

mapka = folium.Map(location=[42.77, -7.41], zoom_start=8, control_scale=True)
trasyPlugin.trasyCamino2019(mapka)
markers.caminoMarker(mapka)
tooltip = 'RAPORT Camino Santiago de Compostela 2019'
methods.markerRaport(mapka, 42.98, -9.36, methods.popupRaport(), tooltip)
methods.openWebbAndSave(mapka, 'C:/Users/zs/Downloads/Camino.html')
