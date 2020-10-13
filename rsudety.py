from folium import folium

import methods
import trasy
import markers

lat = 50.74028
lng = 16.64504

mapka = folium.Map(location=[lat, lng], zoom_start=8, control_scale=True)
trasy.trasy_sudety2016(mapka)
trasy.trasy_sudety2018(mapka)
trasy.trasy_sudety2019(mapka)
markers.corona_marker(mapka)
methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras w Sudetach i Górach Świętokrzyskich'
methods.marker_raport(mapka, lat, lng, methods.popup_raport(), tooltip)
methods.open_webb_and_save(mapka, 'C:/Users/zs/Downloads/Sudety.html')
