from folium import folium

import methods
import trasy
import markers

lat = 50.74028
lng = 16.64504

mapka = folium.Map(location=[lat, lng], zoom_start=8, control_scale=True)
trasy.trasySudety2016(mapka)
trasy.trasySudety2018(mapka)
trasy.trasySudety2019(mapka)
markers.coronaMarker(mapka)
methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras w Sudetach i Górach Świętokrzyskich'
methods.markerRaport(mapka, lat, lng, methods.popupRaport(), tooltip)
methods.openWebbAndSave(mapka, 'C:/Users/zs/Downloads/Sudety.html')
