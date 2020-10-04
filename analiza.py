import folium
import gpxpy.gpx
import methods
import math

file = 'tatry/2016/08-23 Bystra.gpx'
gpx_file = open(file, 'r')
gpx = gpxpy.parse(gpx_file)


def latLonTime():
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                print('Współrzędne ({0},{1}), wysokość: {2}m, czas: {3}'.format(point.latitude, point.longitude,
                                                                                point.elevation, point.time))


def wzniosySpadki():
    pointsElevation = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                pointsElevation.append(point.elevation)
    i = 240
    wzniosy = 0.0
    spadki = 0.0
    while i < len(pointsElevation) - 10:
        x = pointsElevation[i]
        y = pointsElevation[i + 1]
        z = y - x
        if z == 1:
            wzniosy += z
        if z == -1:
            spadki += z
        i += 3
    return "Wzniosy:" + str(wzniosy) + "m\nSpadki:" + str(spadki) + "m\n"


def maxWys():
    maks = 0
    rok = 1857
    miesiac = 0
    dzien = 0
    godz = 0
    minuta = 0
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:

                if point.elevation > maks:
                    maks = point.elevation
                    rok = point.time.year
                    miesiac = point.time.month
                    dzien = point.time.day
                    godz = point.time.hour
                    minuta = point.time.minute
    if dzien > 9:
        return str(rok) + "-" + str(miesiac) + "-" + str(dzien) + ", godz:" + str(godz) + ":" + str(
            minuta) + " - " + "maksymalna wysokość " + str(maks) + " mnpm"

    else:
        return str(rok) + "-" + str(miesiac) + "-0" + str(dzien) + ", godz:" + str(godz) + ":" + str(
            minuta) + " - " + "maksymalna wysokość " + str(maks) + " mnpm"


def czaTrwania():
    pointsTime = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                pointsTime.append(point.time)
    tP = pointsTime[0]
    tK = pointsTime[len(pointsTime) - 1]
    str1 = str(tP)
    str2 = str(tK)

    return "Start:" + str1[11:16] + "\nMeta:" + str2[11:16]


def distance():
    pointsX = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                pointsX.append(point.latitude)

    pointsY = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                pointsY.append(point.longitude)

    i = 0
    j = 0
    dystans = 0.0

    while i < len(pointsX) - 1:
        R = 6373.0
        x1 = pointsX[i]
        x2 = pointsX[i + 1]
        y1 = pointsY[j]
        y2 = pointsY[j + 1]
        lat1 = math.radians(x1)
        lat2 = math.radians(x2)
        lon1 = math.radians(y1)
        lon2 = math.radians(y2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dystans += R * c
        i += 1
        j += 1
    return "Dystans:" + str(round(dystans, 2)) + "km\n"


def readFilePoly():
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    polyLine = folium.PolyLine(points, color="blue", weight=3.5, opacity=1)
    return polyLine


def readFileMarker():
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    ave_lat = float(sum(p[0] for p in points) / len(points))
    ave_lon = float(sum(p[1] for p in points) / len(points))
    marker = folium.CircleMarker(location=[ave_lat, ave_lon], color='none', radius=25, fill_color='blue',
                                 popup=(wzniosySpadki() + distance() + czaTrwania()),
                                 tooltip=maxWys())
    return marker


def showGpxReturnMap():
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    ave_lat = sum(p[0] for p in points) / len(points)
    ave_lon = sum(p[1] for p in points) / len(points)
    m = folium.Map(location=[ave_lat, ave_lon], zoom_start=13, control_scale=True)
    return m


latLonTime()
wzniosySpadki()

mapka = showGpxReturnMap()
readFilePoly().add_to(mapka)
readFileMarker().add_to(mapka)
methods.openWebbAndSave(mapka, 'analiza.html')
