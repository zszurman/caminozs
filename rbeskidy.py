from folium import folium

import markers
import methods
import trasy

lat = 49.95
lng = 19.05069

mapka = folium.Map(location=[lat, lng], zoom_start=9, control_scale=True)

trasy.trasy_beskidy2016(mapka)
trasy.trasy_beskidy2017(mapka)
trasy.trasy_beskidy2018(mapka)
trasy.trasy_beskidy2019(mapka)
trasy.trasy_beskidy2020(mapka)

markers.corona_marker(mapka)
methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras w Beskidach'
methods.marker_raport(mapka, lat, lng, methods.popup_raport(), tooltip)
methods.open_webb_and_save(mapka, 'C:/Users/zs/Downloads/Beskidy.html')
