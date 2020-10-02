from folium import folium

import methods
import trasy
import markers
import private

lat = 52.22534
lng = 21.02793

mapka = folium.Map(location=[lat, lng], zoom_start=6, control_scale=True)
trasy.trasyBeskidy2016(mapka)
trasy.trasyBeskidy2017(mapka)
trasy.trasyBeskidy2018(mapka)
trasy.trasyBeskidy2019(mapka)
trasy.trasyBeskidy2020(mapka)

trasy.trasyTatry2015(mapka)
trasy.trasyTatry2016(mapka)
trasy.trasyTatry2018(mapka)
trasy.trasyTatry2019(mapka)
trasy.trasyTatry2020(mapka)

trasy.trasySudety2016(mapka)
trasy.trasySudety2018(mapka)
trasy.trasySudety2019(mapka)

trasy.trasySlovakia2016(mapka)
trasy.trasySlovakia2017(mapka)
trasy.trasySlovakia2018(mapka)

trasy.trasySpacery2015(mapka)
trasy.trasySpacery2017(mapka)
trasy.trasySpacery2019(mapka)

trasy.trasyCamino2019(mapka)
trasy.trasyCamino2016(mapka)

markers.coronaMarker(mapka)
markers.caminoMarker(mapka)
markers.dolomityMarker(mapka)
private.familyMarker(mapka)

methods.popup2015do2020(mapka, lat, lng)
tooltip = 'RAPORT z wszystkich tras zarejestrowanych od 2015 roku'
methods.markerRaport(mapka, lat, lng, methods.popupRaport(), tooltip)
methods.openWebbAndSave(mapka, 'C:/Users/zs/Downloads/Trasy.html')
