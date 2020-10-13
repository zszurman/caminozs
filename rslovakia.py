from folium import folium

import methods
import trasy


lat = 48.90
lng = 19.3

mapka = folium.Map(location=[lat, lng], zoom_start=9, control_scale=True)
trasy.trasy_slovakia2016(mapka)
trasy.trasy_slovakia2017(mapka)
trasy.trasy_slovakia2018(mapka)
methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras w Tatrach Niżnych, Górach Choczańskich i na Małej Fatrze'
methods.marker_raport(mapka, lat, lng, methods.popup_raport(), tooltip)
methods.open_webb_and_save(mapka, 'C:/Users/zs/Downloads/Slovakia.html')
