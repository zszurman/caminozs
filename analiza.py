import math

import folium
import gpxpy.gpx

import methods

file = 'C:/Users/zs/Downloads/Zbigniew_Szurman_2020-09-18_08-10-36.GPX'

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
            print(point)
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
                                                                                punkt.elevation,
                                                                                punkt.time))


def secondReturnTime(sekundy):
    h = sekundy // (60 * 60)
    x = sekundy % (60 * 60)
    m = x // 60
    s = x % 60
    strH = str(h)
    if h < 10:
        strH = "0" + strH
    strM = str(m)
    if m < 10:
        strM = "0" + strM
    strS = str(s)
    if s < 10:
        strS = "0" + strS
    return strH + ":" + strM + ":" + strS


def secondReturnTempo(second):
    m = second // 60
    s = second % 60
    strM = str(m)
    if m < 10:
        strM = "0" + strM
    strS = str(s)
    if s < 10:
        strS = "0" + strS
    return strM + ":" + strS


def secondOfDay(data):
    x = str(data)
    dgo = (int(x[11]) * 10) + int(x[12]) * 60 * 60
    dmi = (int(x[14]) * 10 + int(x[15])) * 60
    dse = int(x[17]) * 10 + int(x[18])
    return dgo + dmi + dse


def wzniosySpadki():
    i = 0
    wzniosy = 0.0
    spadki = 0.0
    while i < len(pointsElevation) - 120:
        x = pointsElevation[i]
        y = pointsElevation[i + 120]
        z = y - x
        if z > 0:
            wzniosy += z
        if z < 0:
            spadki += z
        i += 120
    return "Wzniosy:" + str(wzniosy) + "m \nSpadki:" + str(spadki) + "m \n"


def maxWys():
    maks = 0
    godz = 0
    minuta = 0
    for trasa in gpx.tracks:
        for x in trasa.segments:
            for punkt in x.points:
                if punkt.elevation > maks:
                    maks = punkt.elevation
                    godz = punkt.time.hour
                    minuta = punkt.time.minute
    strMaks = str(int(maks))
    strGodz = str(godz)
    strMinuta = str(minuta)
    if minuta < 10:
        strMinuta = "0" + strMinuta
    return "Maks.wys:" + strMaks + "mnpm\n(godz." + strGodz + ":" + strMinuta + ")\n"


def startMeta():
    tP = pointsTime[0]
    tK = pointsTime[len(pointsTime) - 1]
    str1 = str(tP)
    str2 = str(tK)
    return str1[0:10] + "\nStart:" + str1[11:19] + "\nMeta:" + str2[11:19] + "\n"


def czasAllSec():
    tP = pointsTime[0]
    tK = pointsTime[len(pointsTime) - 1]
    str1 = str(tP)
    str2 = str(tK)
    x1 = (int(str2[17]) * 10 + int(str2[18])) - (int(str1[17]) * 10 + int(str1[18]))
    x2 = ((int(str2[14]) * 10 + int(str2[15])) - (int(str1[14]) * 10 + int(str1[15]))) * 60
    x3 = ((int(str2[11]) * 10 + int(str2[12])) - (int(str1[11]) * 10 + int(str1[12]))) * 60 * 60
    x = x1 + x2 + x3
    return x


def czasPauseSec():
    i = 0
    t = 0
    while i < len(pointsTime) - 1:
        tx = pointsTime[i]
        x = secondOfDay(tx)
        dx = tx.weekday()
        ty = pointsTime[i + 1]
        y = secondOfDay(ty)
        dy = ty.weekday()
        z = y - x
        if z > 1 and dx == dy:
            t += z
            print(z)
        if z > 1 and dx != dy:
            y += 24 * 60 * 60
            z = y - x
            t += z
        i += 1
    return t


def czasPauseString():
    x = czasPauseSec()
    return "Postoje:" + secondReturnTime(x) + "\n"


def czasEfReturnString():
    x = czasAllSec() - czasPauseSec()
    return "Ruch:" + secondReturnTime(x) + "\n"


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
    return "Dystans:" + str(round(dystans, 2)) + "km\n"


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
    return dystans


def kmNaGodz():
    t = czasAllSec() / 60 / 60
    x = distanceReturnKm() / t
    return "Vśr.:" + str(round(x, 2)) + "km/h\n"


def minNaKm():
    s = int(czasAllSec() / distanceReturnKm())
    return "Tśr.:" + secondReturnTempo(s) + "min/km\n"


def maxSpeed():
    i = 0
    j = 0
    recordKm = 0
    while i < len(pointsX) - 60:
        R = 6373.0
        x1 = pointsX[i]
        x2 = pointsX[i + 60]
        y1 = pointsY[j]
        y2 = pointsY[j + 60]
        lat1 = math.radians(x1)
        lat2 = math.radians(x2)
        lon1 = math.radians(y1)
        lon2 = math.radians(y2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        x = R * c
        if x > recordKm:
            recordKm = x
        i += 1
        j += 1

    vMax = round(recordKm * 60, 2)
    tSek = int((60 * 60) / vMax)
    return "Vmax.:" + str(vMax) + "km/h\n" + "Tmax.:" + secondReturnTempo(tSek) + "min/km\n"


printLatLonTime()

lat = float(sum(p[0] for p in pointsXY) / len(pointsXY))
lon = float(sum(p[1] for p in pointsXY) / len(pointsXY))

mapka = folium.Map(location=[lat, lon], zoom_start=13, control_scale=True)

folium.PolyLine(pointsXY, color="blue", weight=3.5, opacity=1).add_to(mapka)
folium.CircleMarker(location=[lat, lon], color='none', radius=25, fill_color='blue',
                    popup=(
                            startMeta() + czasEfReturnString() + czasPauseString() + distance() + kmNaGodz()
                            + minNaKm() + maxSpeed() + wzniosySpadki() + maxWys()
                    ),
                    tooltip=file).add_to(mapka)

methods.openWebbAndSave(mapka, 'analiza.html')
