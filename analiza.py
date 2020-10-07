import math
import folium
import gpxpy.gpx
import methods
from tkinter import *


class Application(Frame):

    def __init__(self, master, file):
        super(Application, self).__init__(master)
        self.file = file
        self.personEnt = Entry(self)
        self.personEnt.grid(row=1, column=1, sticky=W)
        self.nounEnt = Entry(self)
        self.nounEnt.grid(row=2, column=1, sticky=W)
        self.grid()
        self.makeLove()

    def makeLove(self):
        Label(self, text="Wprowadź ścieżki do plików").grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self, text="Plik .gpx:").grid(row=1, column=0, sticky=W)
        Label(self, text="Plik .html:").grid(row=2, column=0, sticky=W)
        Button(self, text="Kliknij aby wyświetlić mapę", command=self.makeMapAndMarker(self.file)).grid(row=6, column=0,
                                                                                                        sticky=W)

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def secondOfDay(data):
        x = str(data)
        dgo = (int(x[11]) * 10) + int(x[12]) * 60 * 60
        dmi = (int(x[14]) * 10 + int(x[15])) * 60
        dse = int(x[17]) * 10 + int(x[18])
        return dgo + dmi + dse

    @staticmethod
    def wzniosySpadki(file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
        pointsElevation = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    pointsElevation.append(point.elevation)
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

    @staticmethod
    def maxWys(file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
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

    @staticmethod
    def startMeta(file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
        pointsTime = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    print(point)
                    pointsTime.append(point.time)
        tP = pointsTime[0]
        tK = pointsTime[len(pointsTime) - 1]
        str1 = str(tP)
        str2 = str(tK)
        return str1[0:10] + "\nStart:" + str1[11:19] + "\nMeta:" + str2[11:19] + "\n"

    @staticmethod
    def czasAllSec(file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
        pointsTime = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    print(point)
                    pointsTime.append(point.time)
        tP = pointsTime[0]
        tK = pointsTime[len(pointsTime) - 1]
        str1 = str(tP)
        str2 = str(tK)
        x1 = (int(str2[17]) * 10 + int(str2[18])) - (int(str1[17]) * 10 + int(str1[18]))
        x2 = ((int(str2[14]) * 10 + int(str2[15])) - (int(str1[14]) * 10 + int(str1[15]))) * 60
        x3 = ((int(str2[11]) * 10 + int(str2[12])) - (int(str1[11]) * 10 + int(str1[12]))) * 60 * 60
        x = x1 + x2 + x3
        return x

    def czasPauseSec(self, file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
        pointsTime = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    print(point)
                    pointsTime.append(point.time)
        i = 0
        t = 0
        while i < len(pointsTime) - 1:
            tx = pointsTime[i]
            x = self.secondOfDay(tx)
            dx = tx.weekday()
            ty = pointsTime[i + 1]
            y = self.secondOfDay(ty)
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

    def czasPauseString(self, file):
        x = self.czasPauseSec(file)
        return "Postoje:" + self.secondReturnTime(x) + "\n"

    def czasEfReturnString(self, file):
        x = self.czasAllSec(file) - self.czasPauseSec(file)
        return "Ruch:" + self.secondReturnTime(x) + "\n"

    @staticmethod
    def distance(file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
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

    @staticmethod
    def distanceReturnKm(file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
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
        return dystans

    def kmNaGodz(self, file):
        t = self.czasAllSec(file) / 60 / 60
        x = self.distanceReturnKm(file) / t
        return "Vśr.:" + str(round(x, 2)) + "km/h\n"

    def minNaKm(self, file):
        s = int(self.czasAllSec(file) / self.distanceReturnKm(file))
        return "Tśr.:" + self.secondReturnTempo(s) + "min/km\n"

    def maxSpeed(self, file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
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
        return "Vmax.:" + str(vMax) + "km/h\n" + "Tmax.:" + self.secondReturnTempo(tSek) + "min/km\n"

    def __str__(self):

        return self.startMeta(self.file) + self.czasEfReturnString(self.file) + self.czasPauseString(self.file) \
               + self.distance(self.file) + self.kmNaGodz(self.file) + self.minNaKm(self.file) + self.maxSpeed(
            self.file) \
               + self.wzniosySpadki(self.file) + self.maxWys(self.file)

    def makeMapAndMarker(self, file):
        gpx_file = open(file, 'r')
        gpx = gpxpy.parse(gpx_file)
        pointsXY = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    pointsXY.append(tuple([point.latitude, point.longitude]))
        lat = float(sum(p[0] for p in pointsXY) / len(pointsXY))
        lon = float(sum(p[1] for p in pointsXY) / len(pointsXY))
        mapka = folium.Map(location=[lat, lon], zoom_start=13, control_scale=True)
        folium.PolyLine(pointsXY, color="blue", weight=3.5, opacity=1).add_to(mapka)
        folium.CircleMarker(location=[lat, lon], color='none', radius=25, fill_color='blue',
                            popup=(
                                    self.startMeta(file) +
                                    self.czasEfReturnString(file) +
                                    self.czasPauseString(file) +
                                    self.distance(file) +
                                    self.kmNaGodz(file) +
                                    self.minNaKm(file) +
                                    self.maxSpeed(file) +
                                    self.wzniosySpadki(file) +
                                    self.maxWys(file)
                            ),
                            tooltip=self.file).add_to(mapka)
        methods.openWebbAndSave(mapka, 'analiza.html')


def printLatLonTime(file):
    gpx_file = open(file, 'r')
    gpx = gpxpy.parse(gpx_file)
    for trasa in gpx.tracks:
        for segment2 in trasa.segments:
            for punkt in segment2.points:
                print('Współrzędne ({0},{1}), wysokość: {2}m, czas: {3}'.format(punkt.latitude, punkt.longitude,
                                                                                punkt.elevation,
                                                                                punkt.time))


root = Tk()
trasa1 = Application(root, 'C:/Users/zs/Downloads/Zbigniew_Szurman_2020-09-18_08-10-36.GPX')
print(trasa1)
root.mainloop()
