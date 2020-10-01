import folium
import gpxpy.gpx
from folium import plugins


class Trasa:
    countTras = 0
    distanceTras = 0
    upTras = 0
    downTras = 0
    maxTras = 0
    hourTras = 0
    minTras = 0

    def __init__(self, name, file, dystans, czas, plus, minus, maks):
        self.name = name
        self.file = file
        self.dystans = dystans
        self.czas = czas
        self.plus = plus
        self.minus = minus
        self.maks = maks
        Trasa.countTras += 1
        Trasa.distanceTras += dystans
        Trasa.upTras += plus
        Trasa.downTras += minus
        if maks > Trasa.maxTras:
            Trasa.maxTras = maks
        if len(czas) == 4:
            Trasa.hourTras += int(czas[0])
        else:
            Trasa.hourTras += int(czas[0] + czas[1])
        Trasa.minTras += int(czas[-2] + czas[-1])

    def readFilePlugin(self):
        gpx_file = open(self.file, 'r')
        gpx = gpxpy.parse(gpx_file)
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        p = plugins.AntPath(points)
        return p

    def readFilePoly(self):
        gpx_file = open(self.file, 'r')
        gpx = gpxpy.parse(gpx_file)
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        polyLine = folium.PolyLine(points, color="blue", weight=3.5, opacity=1)
        return polyLine

    def readFileMarker(self):
        gpx_file = open(self.file, 'r')
        gpx = gpxpy.parse(gpx_file)
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        ave_lat = float(sum(p[0] for p in points) / len(points))
        ave_lon = float(sum(p[1] for p in points) / len(points))
        # marker = methods.markerCircleLarge(ave_lat, ave_lon, self.description2(), self.description1())
        marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='blue',
                                     popup=self.description2(),
                                     tooltip=self.description1())
        return marker

    def description1(self):
        return self.name + ", maks.wys. " + str(self.maks) + " mnpm"

    def description2(self):
        return "trasa=" + str(self.dystans) + "km\nczas=" + self.czas + "h\nwzniosy=" + str(self.plus) \
               + "m\nspadki=" + str(self.minus) + "m"

    def addToMap(self, mapka):
        self.readFileMarker().add_to(mapka)
        self.readFilePoly().add_to(mapka)
