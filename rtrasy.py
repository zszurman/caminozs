from folium import folium

import methods
import trasy
import markers
import private

lat = 52.22534
lng = 21.02793

mapka = folium.Map(location=[lat, lng], zoom_start=6, control_scale=True)
trasy.trasy_beskidy2016(mapka)
trasy.trasy_beskidy2017(mapka)
trasy.trasy_beskidy2018(mapka)
trasy.trasy_beskidy2019(mapka)
trasy.trasy_beskidy2020(mapka)

trasy.trasy_tatry2015(mapka)
trasy.trasy_tatry2016(mapka)
trasy.trasy_tatry2018(mapka)
trasy.trasy_tatry2019(mapka)
trasy.trasy_tatry2020(mapka)

trasy.trasy_sudety2016(mapka)
trasy.trasy_sudety2018(mapka)
trasy.trasy_sudety2019(mapka)

trasy.trasy_slovakia2016(mapka)
trasy.trasy_slovakia2017(mapka)
trasy.trasy_slovakia2018(mapka)

trasy.trasy_spacery2015(mapka)
trasy.trasy_spacery2017(mapka)
trasy.trasy_spacery2019(mapka)

trasy.trasy_camino2019(mapka)
trasy.trasy_camino2016(mapka)

markers.corona_marker(mapka)
markers.camino_marker(mapka)
markers.dolomity_marker(mapka)
private.family_marker(mapka)

methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras zarejestrowanych od 2015 roku'
methods.marker_raport(mapka, lat, lng, methods.popup_raport(), tooltip)
methods.open_webb_and_save(mapka, 'C:/Users/zs/Downloads/Trasy.html')
