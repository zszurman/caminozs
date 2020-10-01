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
    return 'Dni:' + str(xDay) + '\nGodzin:' + str(xHour) + '\nMinut:' + str(xMinut)


def descriptionRaport():
    timeD = timeDay(klasa.Trasa.hourTras, klasa.Trasa.minTras)
    descSuma = "PODSUMOWANIE TATRY\nIlość tras:" + str(klasa.Trasa.countTras) + "\nDystans:" \
               + str(int(klasa.Trasa.distanceTras)) + "km\n" + timeD + "\nWzniosy:" + str(klasa.Trasa.upTras) \
               + "m\nSpadki:" + str(klasa.Trasa.downTras) + "m\nNajwyżej:" + str(klasa.Trasa.maxTras) + "m"
    return descSuma


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
                  tooltip=tooltip, icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)


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
                  icon=folium.Icon(icon='glyphicon-tint', color='pink', prefix='glyphicon')).add_to(mapka)


def markerBackward(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-backward', color='pink', prefix='glyphicon')).add_to(mapka)


def markerBell(mapka, lat, lng, popup, tooltip):
    folium.Marker(location=[lat, lng], popup=popup, tooltip=tooltip,
                  icon=folium.Icon(icon='glyphicon-bell', color='black', prefix='glyphicon')).add_to(mapka)
