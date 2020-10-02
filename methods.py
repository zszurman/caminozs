import webbrowser

import folium
import gpxpy.gpx
from IPython.core.display import display
from folium import plugins
import klasa


def timeDay(hour, minut):
    allMinut = hour * 60 + minut
    xDay = allMinut // (60 * 24)
    restMinut = allMinut % (60 * 24)
    xHour = restMinut // 60
    xMinut = restMinut % 60
    return 'Czas:' + str(xDay) + 'd:' + str(xHour) + 'h:' + str(xMinut) + 'min'


def popupRaport():
    timeD = timeDay(klasa.Trasa.hourTras, klasa.Trasa.minTras)
    descSuma = "Ilość tras:" + str(klasa.Trasa.countTras) + "\nDystans:" \
               + str(int(klasa.Trasa.distanceTras)) + "km\n" + timeD + "\nWzniosy:" + str(klasa.Trasa.upTras) \
               + "m\nSpadki:" + str(klasa.Trasa.downTras) + "m\nNajwyżej:" + str(klasa.Trasa.maxTras) + "m"
    return descSuma


def popup2015():
    timeD = timeDay(klasa.Trasa.hourTras2015, klasa.Trasa.minTras2015)
    descSuma = "Ilość tras:" + str(klasa.Trasa.countTras2015) + "\nDystans:" \
               + str(int(klasa.Trasa.distanceTras2015)) + "km\n" + timeD + "\nWzniosy:" + str(klasa.Trasa.upTras2015) \
               + "m\nSpadki:" + str(klasa.Trasa.downTras2015) + "m\nNajwyżej:" + str(klasa.Trasa.maxTras2015) + "m"
    return descSuma


def popup2016():
    timeD = timeDay(klasa.Trasa.hourTras2016, klasa.Trasa.minTras2016)
    descSuma = "Ilość tras:" + str(klasa.Trasa.countTras2016) + "\nDystans:" \
               + str(int(klasa.Trasa.distanceTras2016)) + "km\n" + timeD + "\nWzniosy:" + str(klasa.Trasa.upTras2016) \
               + "m\nSpadki:" + str(klasa.Trasa.downTras2016) + "m\nNajwyżej:" + str(klasa.Trasa.maxTras2016) + "m"
    return descSuma


def popup2017():
    timeD = timeDay(klasa.Trasa.hourTras2017, klasa.Trasa.minTras2017)
    descSuma = "Ilość tras:" + str(klasa.Trasa.countTras2017) + "\nDystans:" \
               + str(int(klasa.Trasa.distanceTras2017)) + "km\n" + timeD + "\nWzniosy:" + str(klasa.Trasa.upTras2017) \
               + "m\nSpadki:" + str(klasa.Trasa.downTras2017) + "m\nNajwyżej:" + str(klasa.Trasa.maxTras2017) + "m"
    return descSuma


def popup2018():
    timeD = timeDay(klasa.Trasa.hourTras2018, klasa.Trasa.minTras2018)
    descSuma = "Ilość tras:" + str(klasa.Trasa.countTras2018) + "\nDystans:" \
               + str(int(klasa.Trasa.distanceTras2018)) + "km\n" + timeD + "\nWzniosy:" + str(klasa.Trasa.upTras2018) \
               + "m\nSpadki:" + str(klasa.Trasa.downTras2018) + "m\nNajwyżej:" + str(klasa.Trasa.maxTras2018) + "m"
    return descSuma


def popup2019():
    timeD = timeDay(klasa.Trasa.hourTras2019, klasa.Trasa.minTras2019)
    descSuma = "Ilość tras:" + str(klasa.Trasa.countTras2019) + "\nDystans:" \
               + str(int(klasa.Trasa.distanceTras2019)) + "km\n" + timeD + "\nWzniosy:" + str(klasa.Trasa.upTras2019) \
               + "m\nSpadki:" + str(klasa.Trasa.downTras2019) + "m\nNajwyżej:" + str(klasa.Trasa.maxTras2019) + "m"
    return descSuma


def popup2020():
    timeD = timeDay(klasa.Trasa.hourTras2020, klasa.Trasa.minTras2020)
    descSuma = "Ilość tras:" + str(klasa.Trasa.countTras2020) + "\nDystans:" \
               + str(int(klasa.Trasa.distanceTras2020)) + "km\n" + timeD + "\nWzniosy:" + str(klasa.Trasa.upTras2020) \
               + "m\nSpadki:" + str(klasa.Trasa.downTras2020) + "m\nNajwyżej:" + str(klasa.Trasa.maxTras2020) + "m"
    return descSuma


def popup2015do2020(mapka, lat, lng):
    markerRaport(mapka, lat, lng + 0.12, popup2015(), 'ROK 2015')
    markerRaport(mapka, lat, lng + 0.10, popup2016(), 'ROK 2016')
    markerRaport(mapka, lat, lng + 0.08, popup2017(), 'ROK 2017')
    markerRaport(mapka, lat, lng + 0.06, popup2018(), 'ROK 2018')
    markerRaport(mapka, lat, lng + 0.04, popup2019(), 'ROK 2019')
    markerRaport(mapka, lat, lng + 0.02, popup2020(), 'ROK 2020')


def showGpxReturnMap(fileGpx):
    gpx_file = open(fileGpx, 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    ave_lat = sum(p[0] for p in points) / len(points)
    ave_lon = sum(p[1] for p in points) / len(points)
    m = folium.Map(location=[ave_lat, ave_lon], zoom_start=12, control_scale=True)
    return m


def openWebbAndSave(mapka, fileHtml):
    folium.raster_layers.TileLayer('Open Street Map').add_to(mapka)
    folium.raster_layers.TileLayer('StamenTerrain').add_to(mapka)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(mapka)
    folium.raster_layers.TileLayer('StamenToner').add_to(mapka)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(mapka)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(mapka)
    folium.LayerControl().add_to(mapka)

    minimap = plugins.MiniMap(toggle_display=True)
    mapka.add_child(minimap)
    # plugins.ScrollZoomToggler().add_to(mapka)
    plugins.Fullscreen(position='topright').add_to(mapka)

    display(mapka)
    mapka.save(fileHtml)
    html_page = f'{fileHtml}'
    mapka.save(html_page)
    new = 2
    webbrowser.open(html_page, new=new)


def markerCircleSmall(mapka, lat, lng, popup, tooltip):
    folium.CircleMarker(location=[lat, lng], color='yellow', radius=7, fill_color='yellow',
                        popup=popup,
                        tooltip=tooltip).add_to(mapka)


def markerCircleLarge(mapka, lat, lng, popup, tooltip):
    folium.CircleMarker(location=[lat, lng], color='none', radius=25, fill_color='blue',
                        popup=popup,
                        tooltip=tooltip).add_to(mapka)


def markerHotel(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup,
                  tooltip=tooltip, icon=folium.Icon(color='blue', icon='bed', prefix='fa')).add_to(mapka)


def markerInfo(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(color='pink', icon='info-sign')).add_to(mapka)


def markerHeart(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-heart', color='pink', prefix='glyphicon')).add_to(mapka)


def markerUser(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-user', color='pink', prefix='glyphicon')).add_to(mapka)


def markerHome(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-home', color='pink', prefix='glyphicon')).add_to(mapka)


def markerTint(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-tint', color='darkblue', prefix='glyphicon')).add_to(mapka)


def markerBackward(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-backward', color='darkblue', prefix='glyphicon')).add_to(mapka)


def markerBell(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-bell', color='darkblue', prefix='glyphicon')).add_to(mapka)


def markerRaport(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-list-alt', color='cadetblue', prefix='glyphicon')).add_to(mapka)
