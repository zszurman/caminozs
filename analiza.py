import folium
import gpxpy.gpx
import methods
import math

file = 'C:/Users/zs/Downloads/08-27 Blatnia.gpx'

gpx_file = open(file, 'r')
gpx = gpxpy.parse(gpx_file)

pointsElevation = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            pointsElevation.append(point.elevation)

pointsTime = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            pointsTime.append(point.time)

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

pointsXY = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            pointsXY.append(tuple([point.latitude, point.longitude]))


def printLatLonTime():
    for trasa in gpx.tracks:
        for segment2 in trasa.segments:
            for punkt in segment2.points:
                print('Współrzędne ({0},{1}), wysokość: {2}m, czas: {3}'.format(punkt.latitude, punkt.longitude,
                                                                                punkt.elevation, punkt.time))


def wzniosySpadki():
    i = 300
    wzniosy = 0.0
    spadki = 0.0
    while i < len(pointsElevation) - 10:
        x = pointsElevation[i]
        y = pointsElevation[i + 1]
        z = y - x
        if z > 0:
            wzniosy += z
        if z < 0:
            spadki += z
        i += 1
    return "Wzniosy: " + str(wzniosy) + "m \nSpadki: " + str(spadki) + "m \n"


def maxWys():
    maks = 0
    dzien = 0
    godz = 0
    minuta = 0
    for trasa in gpx.tracks:
        for segment1 in trasa.segments:
            for punkt in segment1.points:
                if punkt.elevation > maks:
                    maks = punkt.elevation
                    godz = punkt.time.hour
                    minuta = punkt.time.minute
    if dzien > 9:
        return "Maks.wys: " + str(maks) + "mnpm\n" + "o godz: " + str(godz) + ":" + str(minuta)

    else:
        return "Maks.wys: " + str(maks) + "mnpm\n" + "o godz: " + str(godz) + ":0" + str(minuta)


def czaTrwania():
    tP = pointsTime[0]
    tK = pointsTime[len(pointsTime) - 1]
    str1 = str(tP)
    str2 = str(tK)
    x1 = (int(str2[17]) * 10 + int(str2[18])) - (int(str1[17]) * 10 + int(str1[18]))
    x2 = ((int(str2[14]) * 10 + int(str2[15])) - (int(str1[14]) * 10 + int(str1[15]))) * 60
    x3 = ((int(str2[11]) * 10 + int(str2[12])) - (int(str1[11]) * 10 + int(str1[12]))) * 60 * 60
    x = x1 + x2 + x3
    godz = x // (60 * 60)
    minuta = (x % (60 * 60)) // 60
    sek = (x % (60 * 60)) % 60
    strMinuta = str(minuta)

    if minuta < 10:
        strMinuta = "0" + strMinuta
    if sek < 10:
        pass
    return str1[0:10] + "\nStart: " + str1[11:19] + "\nMeta: " + str2[11:19] + "\nCzas: " + str(
        godz) + ":" + strMinuta + ":" + str(sek) + "\n"


def czasTrwaniaEf():
    i = 0
    t = 0

    while i < len(pointsTime) - 1:
        x = str(pointsTime[i])
        x1 = int(x[11:12]) * 60 * 60 + int(x[14:15]) * 60 + int(x[17:18])
        y = str(pointsTime[i + 1])
        y1 = int(y[11:12]) * 60 * 60 + int(y[14:15]) * 60 + int(y[17:18])
        z = y1 - x1
        t += z
        i += 1

    h = t // (60 * 60)
    b = t % (60 * 60)
    m = b // 60
    s = b % 60

    return "Efektywnie: " + str(h) + ":" + str(m) + ":" + str(s) + "\n"


def czasReturnSecond():
    tP = pointsTime[0]
    tK = pointsTime[len(pointsTime) - 1]
    str1 = str(tP)
    str2 = str(tK)
    x1 = (int(str2[17]) * 10 + int(str2[18])) - (int(str1[17]) * 10 + int(str1[18]))
    x2 = ((int(str2[14]) * 10 + int(str2[15])) - (int(str1[14]) * 10 + int(str1[15]))) * 60
    x3 = ((int(str2[11]) * 10 + int(str2[12])) - (int(str1[11]) * 10 + int(str1[12]))) * 60 * 60
    return x1 + x2 + x3


def distance():
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
    return "Dystans: " + str(round(dystans, 2)) + "km\n"


def distanceReturnKm():
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
    return int(dystans)


def kmNaGodz():
    t = czasReturnSecond() / 60 / 60
    x = distanceReturnKm() / t
    return "Vśr1: " + str(round(x, 2)) + "km/h\n"


def minNaKm():
    t = int(czasReturnSecond() / distanceReturnKm())
    x = t // 60
    x1 = t % 60
    if x1 >= 60:
        x += 1
        x1 -= 60
    if x1 < 10:
        return "Vśr2: " + str(x) + ":0" + str(x1) + "min/km\n"
    else:
        return "Vśr2: " + str(x) + ":" + str(x1) + "min/km\n"


printLatLonTime()

lat = float(sum(p[0] for p in pointsXY) / len(pointsXY))
lon = float(sum(p[1] for p in pointsXY) / len(pointsXY))

mapka = folium.Map(location=[lat, lon], zoom_start=13, control_scale=True)

folium.PolyLine(pointsXY, color="blue", weight=3.5, opacity=1).add_to(mapka)
folium.CircleMarker(location=[lat, lon], color='none', radius=25, fill_color='blue',
                    popup=(
                                czaTrwania() + czasTrwaniaEf() + distance() + kmNaGodz() + minNaKm() + wzniosySpadki() + maxWys()),
                    tooltip=file).add_to(mapka)

methods.openWebbAndSave(mapka, 'analiza.html')
