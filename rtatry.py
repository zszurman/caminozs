from folium import folium

import markers
import methods
import trasy


lat = 49.3
lng = 19.94

mapka = folium.Map(location=[lat, lng], zoom_start=10, control_scale=True)


trasy.trasy_tatry2015(mapka)
trasy.trasy_tatry2016(mapka)
trasy.trasy_tatry2018(mapka)
trasy.trasy_tatry2019(mapka)
trasy.trasy_tatry2020(mapka)
markers.corona_marker(mapka)
methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras w Tatrach'
methods.marker_raport(mapka, lat, lng, methods.popup_raport(), tooltip)
methods.open_webb_and_save(mapka, 'C:/Users/zs/Downloads/Tatry.html')
