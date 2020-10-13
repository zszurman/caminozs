from folium import folium

import markers
import methods
import trasyPlugin

mapka = folium.Map(location=[42.77, -7.41], zoom_start=8, control_scale=True)
trasyPlugin.trasy_camino2019(mapka)
markers.camino_marker(mapka)
tooltip = 'RAPORT Camino Santiago de Compostela 2019'
methods.marker_raport(mapka, 42.98, -9.36, methods.popup_raport(), tooltip)
methods.open_webb_and_save(mapka, 'C:/Users/zs/Downloads/Camino.html')
