from folium import folium

import methods
import trasy

mapka = folium.Map(location=[49.29, 19.94], zoom_start=7, control_scale=True)
trasy.trasyTatry(mapka)
methods.markerBell(mapka, 49.29, 19.94, methods.descriptionRaport(), "RAPORT z wszystkich tras w Tatrach")
methods.openWebbAndSave(mapka, 'C:/Users/zs/Downloads/Tatry.html')
