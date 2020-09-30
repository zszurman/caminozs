import webbrowser
import folium
import gpxpy.gpx
from IPython.core.display import display
from folium import plugins


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

    # plugins.ScrollZoomToggler().add_to(mapa)
    plugins.Fullscreen(position='topright').add_to(mapka)

    display(mapka)
    mapka.save(fileHtml)
    html_page = f'{fileHtml}'
    mapka.save(html_page)
    new = 2
    webbrowser.open(html_page, new=new)
