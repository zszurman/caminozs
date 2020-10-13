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

    countTras2015 = 0
    distanceTras2015 = 0
    upTras2015 = 0
    downTras2015 = 0
    maxTras2015 = 0
    hourTras2015 = 0
    minTras2015 = 0

    countTras2016 = 0
    distanceTras2016 = 0
    upTras2016 = 0
    downTras2016 = 0
    maxTras2016 = 0
    hourTras2016 = 0
    minTras2016 = 0

    countTras2017 = 0
    distanceTras2017 = 0
    upTras2017 = 0
    downTras2017 = 0
    maxTras2017 = 0
    hourTras2017 = 0
    minTras2017 = 0

    countTras2018 = 0
    distanceTras2018 = 0
    upTras2018 = 0
    downTras2018 = 0
    maxTras2018 = 0
    hourTras2018 = 0
    minTras2018 = 0

    countTras2019 = 0
    distanceTras2019 = 0
    upTras2019 = 0
    downTras2019 = 0
    maxTras2019 = 0
    hourTras2019 = 0
    minTras2019 = 0

    countTras2020 = 0
    distanceTras2020 = 0
    upTras2020 = 0
    downTras2020 = 0
    maxTras2020 = 0
    hourTras2020 = 0
    minTras2020 = 0

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

        if '2015' in name:
            Trasa.countTras2015 += 1
            Trasa.distanceTras2015 += dystans
            Trasa.upTras2015 += plus
            Trasa.downTras2015 += minus
            if maks > Trasa.maxTras2015:
                Trasa.maxTras2015 = maks
            if len(czas) == 4:
                Trasa.hourTras2015 += int(czas[0])
            else:
                Trasa.hourTras2015 += int(czas[0] + czas[1])
            Trasa.minTras2015 += int(czas[-2] + czas[-1])

        if '2016' in name:
            Trasa.countTras2016 += 1
            Trasa.distanceTras2016 += dystans
            Trasa.upTras2016 += plus
            Trasa.downTras2016 += minus
            if maks > Trasa.maxTras2016:
                Trasa.maxTras2016 = maks
            if len(czas) == 4:
                Trasa.hourTras2016 += int(czas[0])
            else:
                Trasa.hourTras2016 += int(czas[0] + czas[1])
            Trasa.minTras2016 += int(czas[-2] + czas[-1])

        if '2017' in name:
            Trasa.countTras2017 += 1
            Trasa.distanceTras2017 += dystans
            Trasa.upTras2017 += plus
            Trasa.downTras2017 += minus
            if maks > Trasa.maxTras2017:
                Trasa.maxTras2017 = maks
            if len(czas) == 4:
                Trasa.hourTras2017 += int(czas[0])
            else:
                Trasa.hourTras2017 += int(czas[0] + czas[1])
            Trasa.minTras2017 += int(czas[-2] + czas[-1])

        if '2018' in name:
            Trasa.countTras2018 += 1
            Trasa.distanceTras2018 += dystans
            Trasa.upTras2018 += plus
            Trasa.downTras2018 += minus
            if maks > Trasa.maxTras2018:
                Trasa.maxTras2018 = maks
            if len(czas) == 4:
                Trasa.hourTras2018 += int(czas[0])
            else:
                Trasa.hourTras2018 += int(czas[0] + czas[1])
            Trasa.minTras2018 += int(czas[-2] + czas[-1])

        if '2019' in name:
            Trasa.countTras2019 += 1
            Trasa.distanceTras2019 += dystans
            Trasa.upTras2019 += plus
            Trasa.downTras2019 += minus
            if maks > Trasa.maxTras2019:
                Trasa.maxTras2019 = maks
            if len(czas) == 4:
                Trasa.hourTras2019 += int(czas[0])
            else:
                Trasa.hourTras2019 += int(czas[0] + czas[1])
            Trasa.minTras2019 += int(czas[-2] + czas[-1])

        if '2020' in name:
            Trasa.countTras2020 += 1
            Trasa.distanceTras2020 += dystans
            Trasa.upTras2020 += plus
            Trasa.downTras2020 += minus
            if maks > Trasa.maxTras2020:
                Trasa.maxTras2020 = maks
            if len(czas) == 4:
                Trasa.hourTras2020 += int(czas[0])
            else:
                Trasa.hourTras2020 += int(czas[0] + czas[1])
            Trasa.minTras2020 += int(czas[-2] + czas[-1])

    def read_file_plugin(self):
        gpx_file = open(self.file, 'r')
        gpx = gpxpy.parse(gpx_file)
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))

        if self.countTras == 0 or self.countTras % 7 == 0:
            p = plugins.AntPath(points, color="blue")
        elif self.countTras == 1 or self.countTras % 6 == 0:
            p = plugins.AntPath(points, color="darkred")
        elif self.countTras % 5 == 0:
            p = plugins.AntPath(points, color="purple")
        elif self.countTras % 4 == 0:
            p = plugins.AntPath(points, color="orange")
        elif self.countTras % 3 == 0:
            p = plugins.AntPath(points, color="darkblue")
        elif self.countTras % 2 == 0:
            p = plugins.AntPath(points, color="green")
        else:
            p = plugins.AntPath(points, color="black")

        return p

    def read_file_poly(self):
        gpx_file = open(self.file, 'r')
        gpx = gpxpy.parse(gpx_file)
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        if self.countTras == 0 or self.countTras % 7 == 0:
            polyLine = folium.PolyLine(points, color="blue", weight=3.5, opacity=1)
        elif self.countTras == 1 or self.countTras % 6 == 0:
            polyLine = folium.PolyLine(points, color="darkred", weight=3.5, opacity=1)
        elif self.countTras % 5 == 0:
            polyLine = folium.PolyLine(points, color="purple", weight=3.5, opacity=1)
        elif self.countTras % 4 == 0:
            polyLine = folium.PolyLine(points, color="orange", weight=3.5, opacity=1)
        elif self.countTras % 3 == 0:
            polyLine = folium.PolyLine(points, color="darkblue", weight=3.5, opacity=1)
        elif self.countTras % 2 == 0:
            polyLine = folium.PolyLine(points, color="green", weight=3.5, opacity=1)
        else:
            polyLine = folium.PolyLine(points, color="black", weight=3.5, opacity=1)

        return polyLine

    def read_file_marker(self):
        gpx_file = open(self.file, 'r')
        gpx = gpxpy.parse(gpx_file)
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        ave_lat = float(sum(p[0] for p in points) / len(points))
        ave_lon = float(sum(p[1] for p in points) / len(points))

        if self.countTras == 0 or self.countTras % 7 == 0:
            marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='blue',
                                         popup=self.popup(),
                                         tooltip=self.tooltip())

        elif self.countTras == 1 or self.countTras % 6 == 0:
            marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='darkred',
                                         popup=self.popup(),
                                         tooltip=self.tooltip())
        elif self.countTras % 5 == 0:
            marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='purple',
                                         popup=self.popup(),
                                         tooltip=self.tooltip())
        elif self.countTras % 4 == 0:
            marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='orange',
                                         popup=self.popup(),
                                         tooltip=self.tooltip())
        elif self.countTras % 3 == 0:
            marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='darkblue',
                                         popup=self.popup(),
                                         tooltip=self.tooltip())
        elif self.countTras % 2 == 0:
            marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='green',
                                         popup=self.popup(),
                                         tooltip=self.tooltip())
        else:
            marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='black',
                                         popup=self.popup(),
                                         tooltip=self.tooltip())

        return marker

    def tooltip(self):
        return self.name

    def popup(self):
        return "Dystans:" + str(self.dystans) + "km\nCzas:" + self.czas + "h\nWzniosy:" + str(self.plus) \
               + "m\nSpadki:" + str(self.minus) + "m\nNajwyżej:" + str(self.maks)

    def add_to_map(self, mapka):
        self.read_file_marker().add_to(mapka)
        self.read_file_poly().add_to(mapka)

    def add_to_map_plugin(self, mapka):
        self.read_file_plugin().add_to(mapka)
        self.read_file_marker().add_to(mapka)
