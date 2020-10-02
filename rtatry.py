from folium import folium

import markers
import methods
import trasy


lat = 49.3
lng = 19.94

mapka = folium.Map(location=[lat, lng], zoom_start=10, control_scale=True)


trasy.trasyTatry2015(mapka)
trasy.trasyTatry2016(mapka)
trasy.trasyTatry2018(mapka)
trasy.trasyTatry2019(mapka)
trasy.trasyTatry2020(mapka)
markers.coronaMarker(mapka)
methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras w Tatrach'
methods.markerRaport(mapka, lat, lng, methods.popupRaport(), tooltip)
methods.openWebbAndSave(mapka, 'C:/Users/zs/Downloads/Tatry.html')
