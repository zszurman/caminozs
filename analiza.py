import math
import webbrowser
import folium
import gpxpy.gpx
from IPython.core.display import display
from folium import plugins
from tkinter import *


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)

        self.introLbl = Label(self, text="Wprowadź ścieżki do plików")
        self.introLbl.grid(row=0, column=0, columnspan=2, sticky=W)

        self.gpxLbl = Label(self, text="Plik .gpx:")
        self.gpxLbl.grid(row=1, column=0, sticky=W)

        self.gpxEnt = Entry(self, width=100)
        self.gpxEnt.grid(row=1, column=1, sticky=W)

        self.htmlLbl = Label(self, text="Plik .html:")
        self.htmlLbl.grid(row=2, column=0, sticky=W)

        self.htmlEnt = Entry(self, width=100)
        self.htmlEnt.grid(row=2, column=1, sticky=W)

        self.okBtn = Button(self, text="Kliknij aby wyświetlić mapę", command=self.makeMapAndMarker)
        self.okBtn.grid(row=6, column=0, sticky=W)

        self.storyTxt = Text(self, width=75, height=20, wrap=WORD)
        self.storyTxt.grid(row=3, column=0, columnspan=4)
        self.grid()
        self.fileGPX = 'tatry/2020/07-09 Nosal.gpx'
        self.fileHTML = 'gg.html'

    def gpxParse(self):
        gpx_file = open(self.fileGPX, 'r')
        return gpxpy.parse(gpx_file)

    def pointsX(self):
        gpx = self.gpxParse()
        pointsX = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    pointsX.append(point.latitude)
        return pointsX

    def pointsY(self):
        gpx = self.gpxParse()
        pointsY = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    pointsY.append(point.longitude)
        return pointsY

    def pointsXY(self):
        gpx = self.gpxParse()
        pointsXY = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    pointsXY.append(tuple([point.latitude, point.longitude]))
        return pointsXY

    def pointsTime(self):
        gpx = self.gpxParse()
        pointsTime = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    print(point)
                    pointsTime.append(point.time)
        return pointsTime

    def pointsElevation(self):
        gpx = self.gpxParse()
        pointsElevation = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    pointsElevation.append(point.elevation)
        return pointsElevation

    @staticmethod
    def secondTime(sekundy):
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
    def secondTempo(second):
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

    def upDown(self):
        pointsElevation = self.pointsElevation()
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

    def maxHigh(self):
        gpx_file = open(self.fileGPX, 'r')
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

    def startMeta(self):
        pointsTime = self.pointsTime()
        tP = pointsTime[0]
        tK = pointsTime[len(pointsTime) - 1]
        str1 = str(tP)
        str2 = str(tK)
        return str1[0:10] + "\nStart:" + str1[11:19] + "\nMeta:" + str2[11:19] + "\n"

    def allTimeSec(self):
        pointsTime = self.pointsTime()
        tP = pointsTime[0]
        tK = pointsTime[len(pointsTime) - 1]
        str1 = str(tP)
        str2 = str(tK)
        x1 = (int(str2[17]) * 10 + int(str2[18])) - (int(str1[17]) * 10 + int(str1[18]))
        x2 = ((int(str2[14]) * 10 + int(str2[15])) - (int(str1[14]) * 10 + int(str1[15]))) * 60
        x3 = ((int(str2[11]) * 10 + int(str2[12])) - (int(str1[11]) * 10 + int(str1[12]))) * 60 * 60
        x = x1 + x2 + x3
        return x

    def timePauseSec(self):
        pointsTime = self.pointsTime()
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

    def timePauseString(self):
        x = self.timePauseSec()
        return "Postoje:" + self.secondTime(x) + "\n"

    def timeEfString(self):
        x = self.allTimeSec() - self.timePauseSec()
        return "Ruch:" + self.secondTime(x) + "\n"

    def distanceString(self):
        pointsX = self.pointsX()
        pointsY = self.pointsY()
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

    def distanceKm(self):
        pointsX = self.pointsX()
        pointsY = self.pointsY()
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

    def speedString(self):
        t = self.allTimeSec() / 60 / 60
        x = self.distanceKm() / t
        return "Vśr.:" + str(round(x, 2)) + "km/h\n"

    def tempoString(self):
        s = int(self.allTimeSec() / self.distanceKm())
        return "Tśr.:" + self.secondTempo(s) + "min/km\n"

    def maxSpeedTempoString(self):
        pointsX = self.pointsX()
        pointsY = self.pointsY()
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
        return "Vmax.:" + str(vMax) + "km/h\n" + "Tmax.:" + self.secondTempo(tSek) + "min/km\n"

    def __str__(self):

        return self.startMeta() + self.timeEfString() + self.timePauseString() \
               + self.distanceString() + self.speedString() + self.tempoString() + self.maxSpeedTempoString() \
               + self.upDown() + self.maxHigh()

    def makeMapAndMarker(self):
        self.fileGPX = self.gpxEnt.get()
        self.fileHTML = self.htmlEnt.get()
        story = self
        self.storyTxt.delete(0.0, END)
        self.storyTxt.insert(0.0, story)
        pointsXY = self.pointsXY()
        lat = float(sum(p[0] for p in pointsXY) / len(pointsXY))
        lon = float(sum(p[1] for p in pointsXY) / len(pointsXY))
        mapka = folium.Map(location=[lat, lon], zoom_start=13, control_scale=True)
        folium.PolyLine(pointsXY, color="blue", weight=3.5, opacity=1).add_to(mapka)
        folium.CircleMarker(location=[lat, lon], color='none', radius=25, fill_color='blue',
                            popup=(
                                    self.startMeta() +
                                    self.timeEfString() +
                                    self.timePauseString() +
                                    self.distanceString() +
                                    self.speedString() +
                                    self.tempoString() +
                                    self.maxSpeedTempoString() +
                                    self.upDown() +
                                    self.maxHigh()
                            ),
                            tooltip=self.fileGPX).add_to(mapka)
        folium.raster_layers.TileLayer('Open Street Map').add_to(mapka)
        folium.raster_layers.TileLayer('StamenTerrain').add_to(mapka)
        folium.raster_layers.TileLayer('CartoDB Positron').add_to(mapka)
        folium.raster_layers.TileLayer('StamenToner').add_to(mapka)
        folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(mapka)
        folium.raster_layers.TileLayer('Stamen Watercolor').add_to(mapka)
        folium.LayerControl().add_to(mapka)
        minimap = plugins.MiniMap(toggle_display=True)
        mapka.add_child(minimap)
        plugins.Fullscreen(position='topright').add_to(mapka)
        measureControl = plugins.MeasureControl(position='topleft', active_color='red', completed_color='red',
                                                primary_length_unit='km')
        mapka.add_child(measureControl)
        draw = plugins.Draw(position='topleft', export='True')
        draw.add_to(mapka)
        display(mapka)
        mapka.save(self.fileHTML)
        html_page = f'{self.fileHTML}'
        mapka.save(html_page)
        new = 2
        webbrowser.open(html_page, new=new)


root = Tk()
Application(root)
root.mainloop()
