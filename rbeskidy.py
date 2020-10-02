from folium import folium

import methods
import trasy
import markers

lat = 49.95
lng = 19.05069

mapka = folium.Map(location=[lat, lng], zoom_start=9, control_scale=True)
trasy.trasyBeskidy2016(mapka)
trasy.trasyBeskidy2017(mapka)
trasy.trasyBeskidy2018(mapka)
trasy.trasyBeskidy2019(mapka)
trasy.trasyBeskidy2020(mapka)
markers.coronaMarker(mapka)
methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras w Beskidach'
methods.markerRaport(mapka, lat, lng, methods.popupRaport(), tooltip)
methods.openWebbAndSave(mapka, 'C:/Users/zs/Downloads/Beskidy.html')
