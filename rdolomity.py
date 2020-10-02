from folium import folium

import methods
import trasyPlugin
import markers

mapka = folium.Map(location=[46.47, 11.77], zoom_start=11, control_scale=True)
trasyPlugin.trasyCamino2016(mapka)
markers.dolomityMarker(mapka)
tooltip = 'RAPORT z wszystkich tras w Alpach (Dolomity)'
methods.markerRaport(mapka, 46.47, 11.77, methods.popupRaport(), tooltip)
methods.openWebbAndSave(mapka, 'C:/Users/zs/Downloads/Dolomity.html')
