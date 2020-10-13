from folium import folium

import methods
import trasyPlugin
import markers

mapka = folium.Map(location=[46.47, 11.77], zoom_start=11, control_scale=True)
trasyPlugin.trasy_camino2016(mapka)
markers.dolomity_marker(mapka)
tooltip = 'RAPORT z wszystkich tras w Alpach (Dolomity)'
methods.marker_raport(mapka, 46.47, 11.77, methods.popup_raport(), tooltip)
methods.open_webb_and_save(mapka, 'C:/Users/zs/Downloads/Dolomity.html')









