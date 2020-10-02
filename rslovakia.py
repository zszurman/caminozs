from folium import folium

import methods
import trasy

lat = 48.90
lng = 19.3

mapka = folium.Map(location=[lat, lng], zoom_start=9, control_scale=True)
trasy.trasySlovakia2016(mapka)
trasy.trasySlovakia2017(mapka)
trasy.trasySlovakia2018(mapka)
methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras w Tatrach Niżnych, Górach Choczańskich i na Małej Fatrze'
methods.markerRaport(mapka, lat, lng, methods.popupRaport(), tooltip)
methods.openWebbAndSave(mapka, 'C:/Users/zs/Downloads/Slovakia.html')
