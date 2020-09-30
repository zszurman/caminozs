import folium
import gpxpy.gpx
from folium import plugins

import markers
import methods
import private


class Trasa:
    def __init__(self, name, file, dystans, czas, plus, minus, maks):
        self.name = name
        self.file = file
        self.dystans = dystans
        self.czas = czas
        self.plus = plus
        self.minus = minus
        self.maks = maks

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


def trasyCamino(mapka):
    Trasa('2015-04-17 Gundelsheim', 'camino/2015/04-17 Gundelsheim.gpx', 1.46, '0:27', 5, 5, 150).addToMap(mapka)
    Trasa('2016-06-26 Świety Mikołaj', 'camino/2016/06-26 Swiety Mikolaj.gpx', 14.92, '4:49', 955, 805, 2363).addToMap(
        mapka)
    Trasa('2016-06-27 Plaskowyż Puez', 'camino/2016/06-27 Plaskowyz Puez.gpx', 13.23, '6:47', 595, 1095, 2565).addToMap(
        mapka)
    Trasa('2016-06-28 Piz Boe', 'camino/2016/06-28 Piz Boe.gpx', 6.71, '3:26', 375, 375, 2981).addToMap(mapka)
    Trasa('2016-06-29 Sasalungo', 'camino/2016/06-29 Sasalungo.gpx', 15.11, '6:43', 1080, 1080, 2795).addToMap(mapka)
    Trasa('2016-06-30 Rosengarten', 'camino/2016/06-30 Rosengarten.gpx', 11.53, '5:15', 690, 690, 2463).addToMap(mapka)
    Trasa('2016-06-30 Vigo di Fassa (dojście do kolejki linowej)', 'camino/2016/06-30 Vigo di Fassa.gpx', 1.38, '0:20',
          105, 5, 1420).addToMap(mapka)
    Trasa('2016-07-01 Widok na Marmoladę', 'camino/2016/07-01 Widok na Marmolade.gpx', 6.37, '2:27', 270, 395,
          2429).addToMap(mapka)
    Trasa('2017-03-05 Heilbronn', 'camino/2017/03-05 Heilbronn.gpx', 2.71, '1:05', 50, 50, 200).addToMap(mapka)
    Trasa('2017-03-14 Heilbronn', 'camino/2017/03-14 Heilbronn.gpx', 4.00, '0:31', 10, 35, 200).addToMap(mapka)

    Trasa('2019-09-05 Madryt', 'camino/2019/09-05_Madryt.gpx', 0.61, '0:13', 5, 10, 651).addToMap(mapka)
    Trasa('2019-09-07 I etap: Cacabelos-Pradela', 'camino/2019/09-07 I etap - Cacabelos-Pradela.gpx',
          17.76, '4:49', 675, 215, 930).addToMap(mapka)
    Trasa('2019-09-08 II etap: Pradela-OCebreiro', 'camino/2019/09-08 II etap - Pradela-OCebreiro.gpx',
          20.13, '5:12', 750, 400, 1310).addToMap(mapka)
    Trasa('2019-09-09 III etap(cz.1): OCebreiro-Triacastela', 'camino/2019/09-09 III etap - OCebreiro-Triacastela.gpx',
          8.53, '2:05', 190, 150, 1335).addToMap(mapka)
    Trasa('2019-09-09 III etap(cz.2): OCebreiro-Triacastela',
          'camino/2019/09-09 III etap - Ocebreiro-Triacastela cd .gpx',
          14.77, '3:31', 95, 710, 1335).addToMap(mapka)
    Trasa('2019-09-10 IV etap: Triacastela-Saria', 'camino/2019/09-10 IV etap - Triacastela-Saria.gpx',
          16.00, '3:59', 255, 555, 888).addToMap(mapka)
    Trasa('2019-09-11 V etap: Saria-Gonzar', 'camino/2019/09-11 V etap - Saria-Gonzar.gpx',
          30.43, '6:44', 670, 575, 665).addToMap(mapka)
    Trasa('2019-09-12 VI etap: Gonzar-Casanova', 'camino/2019/09-12 VI Gonzar-Casanova.gpx',
          23.26, '5:06', 440, 485, 702).addToMap(mapka)
    Trasa('2019-09-13 VII etap: Casanova-Salceda', 'camino/2019/09-13 VII etap Casanova-Salceda.gpx',
          35.30, '7:40', 685, 830, 480).addToMap(mapka)
    Trasa('2019-09-14 VIII etap: Salceda-Santiago de Compostela', 'camino/2019/09-14 VIII etap - Salceda-Santiago.gpx',
          28.32, '6:11', 550, 625, 420).addToMap(mapka)
    Trasa('2019-09-16 Fisterra', 'camino/2019/09-16 Fisterra.gpx',
          1.21, '0:56', 95, 95, 121).addToMap(mapka)
    Trasa('2019-09-16 Muxia', 'camino/2019/09-16 Muxia.gpx',
          3.46, '1:16', 85, 75, 55).addToMap(mapka)
    Trasa('2019-09-17 Bazylea', 'camino/2019/09-17 Bazylea.gpx', 3.04, '1:03', 155, 155, 280).addToMap(mapka)


def trasyBeskidy(mapka):
    Trasa('2016-04-26 Babia Góra', 'beskidy/2016/04-26 Babia Gora.gpx', 14.02, '3:59', 605, 605, 1723).addToMap(mapka)
    Trasa('2016-05-01 Turbacz', 'beskidy/2016/05-01 Turbacz.gpx', 16.65, '4:41', 720, 720, 1310).addToMap(mapka)
    Trasa('2016-05-02 Wysoka', 'beskidy/2016/05-02  Wysoka.gpx', 8.24, '4:09', 635, 635, 1050).addToMap(mapka)
    Trasa('2016-05-08 Czupel', 'beskidy/2016/05-08 Czupel.gpx', 10.06, '2:43', 345, 345, 933).addToMap(mapka)
    Trasa('2016-05-15 Skrzyczne', 'beskidy/2016/05-15 Skrzyczne.gpx', 4.27, '1:36', 690, 10, 1257).addToMap(mapka)
    Trasa('2016-07-13 Radhost', 'beskidy/2016/07-13 Radhost.gpx', 11.33, '3:49', 690, 690, 1129).addToMap(mapka)
    Trasa('2016-08-15 Stożek', 'beskidy/2016/08-15 Stozek.gpx', 13.54, '3:41', 630, 630, 979).addToMap(mapka)
    Trasa('2016-09-11 Ropice', 'beskidy/2016/09-11 Ropice.gpx', 14.79, '4:05', 705, 705, 1082).addToMap(mapka)
    Trasa('2016-11-30 Pilsko', 'beskidy/2016/11-30 Pilsko.gpx', 11.91, '6:27', 770, 770, 1557).addToMap(mapka)
    Trasa('2016-12-15 Łysa Hora', 'beskidy/2016/12-15 Lysa Hora.gpx', 12.15, '4:28', 890, 890, 1323).addToMap(mapka)
    Trasa('2016-12-27 Łysa Hora', 'beskidy/2016/12-27 Lysa Hora.gpx', 10.26, '4:40', 820, 820, 1323).addToMap(mapka)
    # 2017
    Trasa('2017-01-11 Rysianka schronisko', 'beskidy/2017/01-11 Rysianka.gpx', 15.58, '4:56', 730, 730, 1260).addToMap(
        mapka)
    Trasa('2017-01-19 Rysianka schronisko', 'beskidy/2017/01-19 Rysianka.gpx', 18.22, '6:50', 755, 755, 1260).addToMap(
        mapka)
    Trasa('2017-01-23 Klimczok', 'beskidy/2017/01-23 Klimczok.gpx', 18.67, '5:43', 840, 840, 1117).addToMap(mapka)
    Trasa('2017-01-28 Równica', 'beskidy/2017/01-28 Rownica.gpx', 10.66, '3:28', 555, 555, 884).addToMap(mapka)
    Trasa('2017-02-15 Barania Góra', 'beskidy/2017/02-15 Barania Gora.gpx', 18.46, '5:04', 705, 705, 1220).addToMap(
        mapka)
    Trasa('2017-03-29 Wielka Racza', 'beskidy/2017/03-29 Wielka Racza.gpx', 16.00, '5:36', 980, 980, 1236).addToMap(
        mapka)
    Trasa('2017-04-04 Wielka Rycerzowa', 'beskidy/2017/04-04 Rycerzowa.gpx', 12.59, '4:08', 665, 665, 1226).addToMap(
        mapka)
    Trasa('2017-04-26 Równica', 'beskidy/2017/04-26 Rownica.gpx', 10.03, '2:52', 560, 560, 884).addToMap(mapka)
    Trasa('2017-05-14 Błatnia', 'beskidy/2017/05-14 Blatnia.gpx', 15.60, '4:18', 590, 590, 917).addToMap(mapka)
    Trasa('2017-06-03 Szyndzielnia', 'beskidy/2017/06-03 Szyndzielnia.gpx', 11.37, '3:21', 630, 630, 1028).addToMap(
        mapka)
    Trasa('2017-07-05 Romanka', 'beskidy/2017/07-05 Romanka.gpx', 13.57, '4:23', 720, 720, 1366).addToMap(mapka)
    Trasa('2017-08-24 Koninki', 'beskidy/2017/08-24 Koninki.gpx', 8.36, '2:18', 235, 235, 727).addToMap(mapka)
    Trasa('2017-08-25 Turbacz', 'beskidy/2017/08-25 Turbacz.gpx', 17.23, '6:02', 850, 850, 1310).addToMap(mapka)
    Trasa('2017-08-26 Mogielica', 'beskidy/2017/08-26 Mogielica.gpx', 7.27, '2:39', 520, 520, 1171).addToMap(mapka)
    Trasa('2017-08-27 Lubomir', 'beskidy/2017/08-27 Lubomir.gpx', 4.17, '1:09', 280, 280, 904).addToMap(mapka)
    Trasa('2017-09-09 Czantoria', 'beskidy/2017/09-09 Czantoria.gpx', 18.94, '5:40', 705, 810, 995).addToMap(mapka)
    Trasa('2017-09-30 Skrzyczne', 'beskidy/2017/09-30 Skrzyczne.gpx', 9.69, '2:47', 715, 715, 1257).addToMap(mapka)
    Trasa('2017-10-01 Klimczok schronisko', 'beskidy/2017/10-01 Klimczok.gpx', 9.57, '2:58', 555, 555, 1042).addToMap(
        mapka)
    Trasa('2017-11-23 Czantoria', 'beskidy/2017/11-23 Czantoria.gpx', 9.59, '3:23', 735, 530, 995).addToMap(mapka)

    # 2018
    Trasa('2018-01-12 Babia Góra', 'beskidy/2018/01-12 Babia Gora.gpx', 14.03, '4:58', 745, 745, 1723).addToMap(mapka)
    Trasa('2018-01-29 Barania Góra', 'beskidy/2018/01-29 Barania Gora.gpx', 17.29, '6:07', 875, 875, 1220).addToMap(
        mapka)
    Trasa('2018-02-01 Łysa Hora', 'beskidy/2018/02-01 Lysa Hora.gpx', 11.41, '4:03', 755, 755, 1323).addToMap(mapka)
    Trasa('2018-02-08 Radhost', 'beskidy/2018/02-08 Radhost.gpx', 11.72, '4:03', 660, 660, 1129).addToMap(mapka)
    Trasa('2018-02-09 Błatnia', 'beskidy/2018/02-09 Blatnia.gpx', 9.03, '2:56', 530, 530, 917).addToMap(mapka)
    Trasa('2018-03-07 Babia Hora', 'beskidy/2018/03-07 Babia Hora.gpx', 16.13, '6:28', 1090, 1090, 1723).addToMap(mapka)
    Trasa('2018-03-16 Błękitna EDK', 'beskidy/2018/03-16 Blekitna EDK.gpx', 40.66, '8:41', 440, 440, 270).addToMap(
        mapka)
    Trasa('2018-09-29 Radziejowa', 'beskidy/2018/09-29 Radziejowa.gpx', 10.42, '3:27', 505, 505, 1266).addToMap(mapka)
    Trasa('2018-09-30 Lackowa', 'beskidy/2018/09-30 Lackowa.gpx', 7.87, '2:43', 425, 425, 977).addToMap(mapka)

    # 2019
    Trasa('2019-02-16 Łysa Hora', 'beskidy/2019/02-16 Lysa Hora.gpx', 11.19, '3:55', 760, 760, 1323).addToMap(mapka)
    Trasa('2019-02-19 Hrobacza Łąka', 'beskidy/2019/02-19 Hrobacza Laka.gpx', 7.08, '2:34', 390, 390, 828).addToMap(
        mapka)
    Trasa('2019-02-28 Babia Hora', 'beskidy/2019/02-28 Babia Hora.gpx', 16.42, '6:25', 1015, 1015, 1723).addToMap(mapka)
    Trasa('2019-08-30 Korbielów', 'beskidy/2019/08-30 Korbielow.gpx', 4.34, '1:50', 345, 345, 1011).addToMap(mapka)
    Trasa('2019-08-31 Babia Hora', 'beskidy/2019/08-31 Babia_Hora.gpx', 16.43, '5:41', 1015, 1015, 1723).addToMap(mapka)
    Trasa('2019-09-01 Żar', 'beskidy/2019/09-01 Zar.gpx', 3.59, '0:56', 70, 70, 750).addToMap(mapka)
    Trasa('2019-09-28 Klimczok', 'beskidy/2019/09-28 Klimczok.gpx', 6.49, '2:01', 210, 210, 1117).addToMap(mapka)
    Trasa('2019-10-19 Łysa Hora', 'beskidy/2019/10-19 Lysa Hora.gpx', 12.70, '4:12', 835, 835, 1323).addToMap(mapka)
    Trasa('2019-12-05 Klimczok schronisko', 'beskidy/2019/12-05 Klimczok.gpx', 5.57, '3:37', 550, 5, 1042).addToMap(
        mapka)

    # 2020
    Trasa('2020-01-14 Radhost', 'beskidy/2020/01-14 Radhost.gpx', 14.38, '4:49', 740, 740, 1129).addToMap(mapka)
    Trasa('2020-01-25 Stołów', 'beskidy/2020/01-25 Stolow.gpx', 13.65, '4:47', 660, 660, 1035).addToMap(mapka)
    Trasa('2020-02-08 Błatnia', 'beskidy/2020/02-08 Blatnia.gpx', 13.68, '4:13', 575, 575, 917).addToMap(mapka)
    Trasa('2020-02-15 Kotarz', 'beskidy/2020/02-15 Kotarz.gpx', 13.61, '4:30', 605, 605, 974).addToMap(mapka)
    Trasa('2020-06-13 Kotarz z Zosią', 'beskidy/2020/06-13 Kotarz.gpx', 9.09, '3:58', 215, 540, 974).addToMap(mapka)
    Trasa('2020-06-27 Wielka Racza', 'beskidy/2020/06-27 Wielka Racza.gpx', 8.35, '3:12', 510, 510, 1236).addToMap(
        mapka)
    Trasa('2020-08-27 Błatnia z Hanią', 'beskidy/2020/08-27 Blatnia.gpx', 11.50, '4:21', 520, 520, 917).addToMap(mapka)
    Trasa('2020-09-12 Łysa Hora', 'beskidy/2020/09-12 Lysa Hora.gpx', 16.71, '5:13', 865, 865, 1323).addToMap(mapka)


def trasySudety(mapka):
    Trasa('2016-06-05 Praded', 'sudety/2016/06-05 Praded.gpx', 12.73, '3:57', 745, 270, 1491).addToMap(mapka)
    Trasa('2018-05-31 Kowadło i Rudawiec', 'sudety/2018/05-31 Kowadło i Rudawiec.gpx', 14.03, '4:17', 705, 705,
          1106).addToMap(mapka)
    Trasa('2018-06-01 Śnieżnik', 'sudety/2018/06-01 Snieznik.gpx', 19.68, '5:28', 940, 940, 1426).addToMap(mapka)
    Trasa('2018-06-02 Jagodna', 'sudety/2018/06-02 Jagodna.gpx', 8.67, '2:01', 215, 215, 977).addToMap(mapka)
    Trasa('2018-06-02 Orlica', 'sudety/2018/06-02 Orlica.gpx', 4.30, '1:06', 215, 215, 1084).addToMap(mapka)
    Trasa('2018-06-24 Biskupia Kopa', 'sudety/2018/06-24 Biskupia Kopa.gpx', 7.59, '2:30', 500, 500, 890).addToMap(
        mapka)
    Trasa('2018-08-01 Śnieżka', 'sudety/2018/08-01 Sniezka.gpx', 5.52, '1:34', 265, 265, 1603).addToMap(mapka)
    Trasa('2018-08-02 Wysoka Kopa', 'sudety/2018/08-02 Wysoka Kopa.gpx', 18.98, '5:45', 510, 775, 1126).addToMap(mapka)
    Trasa('2018-08-03 Kamieńczyk', 'sudety/2018/08-03 Kamienczyk.gpx', 12.71, '3:50', 435, 435, 850).addToMap(mapka)
    Trasa('2018-08-04 Łabski Szczyt', 'sudety/2018/08-04 Sniezne Kotly.gpx', 12.61, '4:19', 955, 235, 1470).addToMap(
        mapka)
    Trasa('2018-08-05 Smrk', 'sudety/2018/08-05 Smrk.gpx', 6.44, '1:44', 175, 175, 1124).addToMap(mapka)
    Trasa('2018-08-06 Skalnik', 'sudety/2018/08-06 Skalnik.gpx', 8.51, '2:30', 365, 365, 944).addToMap(mapka)
    Trasa('2018-08-07 Skopiec', 'sudety/2018/08-07 Skopiec.gpx', 6.16, '1:43', 285, 285, 719).addToMap(mapka)
    Trasa('2018-08-30 Kłodzka Góra', 'sudety/2018/08-30 Klodzka Gora.gpx', 8.45, '2:39', 405, 405, 757).addToMap(mapka)
    Trasa('2018-08-30 Szczeliniec Wielki', 'sudety/2018/08-30 Szczeliniec.gpx', 3.55, '1:19', 180, 180, 919).addToMap(
        mapka)
    Trasa('2018-08-31 Chełmiec', 'sudety/2018/08-31 Chelmiec.gpx', 11.51, '4:12', 515, 515, 851).addToMap(mapka)
    Trasa('2018-09-01 Waligóra', 'sudety/2018/09-01 Waligora.gpx', 0.97, '0:42', 140, 140, 934).addToMap(mapka)
    Trasa('2018-09-01 Wielka Sowa', 'sudety/2018/09-01 Wielka Sowa.gpx', 6.52, '1:48', 265, 265, 1015).addToMap(mapka)
    Trasa('2018-09-02 Ślęża', 'sudety/2018/09-02 Sleza.gpx', 8.09, '2:04', 330, 330, 718).addToMap(mapka)
    Trasa('2019-07-05 Łysa Góra', 'sudety/2019/07-05 Lysa Gora.gpx', 8.93, '2:16', 320, 320, 594).addToMap(mapka)
    Trasa('2019-07-06 Łysica (Święty Krzyż', 'sudety/2019/07-06 Lysica.gpx', 3.77, '1:23', 265, 265, 613).addToMap(
        mapka)


def trasyTatry(mapka):
    Trasa('2015-08-01 Solisko', 'tatry/2015/08-01 Solisko.gpx', 2.6, '1:27', 270, 270, 2117).addToMap(mapka)
    Trasa('2015-08-02 Krivan (wejście)', 'tatry/2015/08-02 Krivan.gpx', 6.55, '3:06', 1358, 25, 2494).addToMap(mapka)
    Trasa('2015-08-02 Krivan (zejście)', 'tatry/2015/08-02 Krivan cd.gpx', 5.07, '2:26', 0, 1100, 2494).addToMap(mapka)
    Trasa('2015-08-04 Łomnica (pod szczyt)', 'tatry/2015/08-04 Lomnica.gpx', 9.12, '3:11', 675, 10, 1765).addToMap(
        mapka)
    Trasa('2015-08-04 Łomnica (zejście)', 'tatry/2015/08-04 Lomnica cd.gpx', 5.35, '1:38', 0, 820, 1765).addToMap(mapka)
    Trasa('2015-08-05 Sileski Dom cz.1', 'tatry/2015/08-05 Sileski Dom.gpx', 5.95, '1:59', 360, 50, 1690).addToMap(
        mapka)
    Trasa('2015-08-05 Sileski Dom cz.2', 'tatry/2015/08-05 Sileski Dom cd.gpx', 4.96, '1:23', 0, 575, 1660).addToMap(
        mapka)
    Trasa('2015-08-06 Czerwona Ławka cz.1', 'tatry/2015/08-06 Czerwona Lawka.gpx', 11.01, '3:53', 780, 340,
          2352).addToMap(
        mapka)
    Trasa('2015-08-06 Czerwona Ławka cz.2', 'tatry/2015/08-06 Czerwona Lawka cd.gpx', 5.85, '1:25', 0, 625,
          1960).addToMap(
        mapka)
    Trasa('2015-08-08 Slavkovski Stit (wejście)', 'tatry/2015/08-08 Slavkovski Stit.gpx', 4.32, '2:31', 1152, 0,
          2452).addToMap(
        mapka)
    # Trasa('2015-08-08 Slavkovski Stit (zejście)', 'tatry/08-08 Slavkovski Stit cd.gpx', 4.5, '2:20', 0, 1152, 2452)
    # .addToMap(mapa)
    Trasa('2015-08-29 Czerwone Wierchy cz.1', 'tatry/2015/08-29 Czerwone Wierchy.gpx', 6.12, '2:41', 430, 305,
          2122).addToMap(
        mapka)
    Trasa('2015-08-29 Czerwone Wierchy cz.2', 'tatry/2015/08-29 Czerwone Wierchy cd.gpx', 6.88, '2:37', 25, 1090,
          2122).addToMap(
        mapka)
    Trasa('2016-08-23 Bystra, Błyszcz ', 'tatry/2016/08-23 Bystra.gpx', 21.47, '8:59', 1450, 1450, 2248).addToMap(mapka)
    Trasa('2018-08-16 Rochacze', 'tatry/2018/08-16 Rochacze.gpx', 13.83, '7:27', 1355, 1050, 2125).addToMap(mapka)
    Trasa('2019-07-20 Banikov (wejście)', 'tatry/2019/07-20 Banikov.gpx', 14.03, '8:28', 1495, 1030, 2178).addToMap(
        mapka)
    Trasa('2019-07-20 Banikov (zejście)', 'tatry/2019/07-20_Banikov cd.gpx', 2.3, '1:02', 5, 455, 1496).addToMap(mapka)

    Trasa('2019-10-05 Trzydniowiański Wierch', 'tatry/2019/10-05 Trzydniowianski.gpx', 20.46, '5:58', 960, 960,
          1758).addToMap(
        mapka)
    Trasa('2020-07-06 Gęsia Szyja', 'tatry/2020/07-06 Gesia Szyja.gpx', 11.62, '4:14', 525, 560, 1498).addToMap(mapka)
    Trasa('2020-07-07 Goryczkowa Czuba (zejście z Kasprowego)', 'tatry/2020/07-07 Goryczkowy.gpx', 8.97, '4:06', 190,
          1160,
          1913).addToMap(mapka)
    Trasa('2020-07-07 Świnica (oblodzenie, nie zdobyta)', 'tatry/2020/07-07 Swinica.gpx', 4.39, '2:17', 350, 350,
          2104).addToMap(
        mapka)
    Trasa('2020-07-08 Szpiglasowy Wierch', 'tatry/2020/07-08 Szpiglasowy.gpx', 23.11, '10:02', 1260, 1260,
          2172).addToMap(
        mapka)
    Trasa('2020-07-09 Nosal, Kopieniec', 'tatry/2020/07-09 Nosal.gpx', 11.97, '4:54', 680, 705, 1328).addToMap(mapka)
    Trasa('2020-07-10 Kościelec', 'tatry/2020/07-10 Koscielec.gpx', 16.71, '8:04', 1525, 1525, 2155).addToMap(mapka)
    Trasa('2020-07-11 Przysłop Miętusi', 'tatry/2020/07-11 Mietusi.gpx', 6.31, '2:12', 340, 340, 1268).addToMap(mapka)
    Trasa('2020-08-01 Banikov', 'tatry/2020/08-01 Banikov.gpx', 15.93, '9:51', 1595, 1520, 2178).addToMap(mapka)
    Trasa('2020-09-05 Koprovsky Stit', 'tatry/2020/09-05 Koprovsky Stit.gpx', 20.1, '7:44', 1200, 1200, 2367).addToMap(
        mapka)


def trasySlovakia(mapka):
    Trasa('2016-08-24 Dumbier', 'slovakia/2016/08-24 Dumbier.gpx', 8.13, '3:04', 510, 510, 2043).addToMap(mapka)
    Trasa('2016-08-25 Velky Choc', 'slovakia/2016/08-25 Velky Choc.gpx', 9.00, '4:56', 1110, 1110, 1611).addToMap(mapka)
    Trasa('2016-11-23 Velky Krivan', 'slovakia/2016/11-23 Velky Krivan.gpx', 10.53, '5:39', 1195, 1195, 1709).addToMap(
        mapka)
    Trasa('2016-12-07 Stoh', 'slovakia/2016/12-07 Stoh.gpx', 10.64, '5:40', 1000, 1000, 1607).addToMap(mapka)
    Trasa('2017-06-16 Terchova Diery', 'slovakia/2017/06-16 Terchova Diery.gpx', 5.01, '2:00', 285, 285, 750).addToMap(
        mapka)
    Trasa('2017-06-18 Stoh', 'slovakia/2017/06-18 Stoh.gpx', 11.43, '5:27', 1225, 1225, 1607).addToMap(mapka)
    Trasa('2017-07-17 Boboty', 'slovakia/2017/07-17 Boboty.gpx', 4.38, '2:58', 470, 530, 1086).addToMap(mapka)
    Trasa('2017-07-18 Velky Rozsutec', 'slovakia/2017/07-18 Velky Rozsutec.gpx', 10.15, '6:07', 1210, 1210,
          1610).addToMap(mapka)
    Trasa('2017-07-19 Velky Krivan', 'slovakia/2017/07-19 Velky Krivan.gpx', 11.43, '4:15', 490, 1345, 1709).addToMap(
        mapka)
    Trasa('2017-07-20 Zbojecky Chodnik', 'slovakia/2017/07-20 Zbojecky Chodnik.gpx', 6.25, '4:02', 745, 745,
          1007).addToMap(mapka)
    Trasa('2018-01-25 Velky Choć', 'slovakia/2018/01-25 Velky Choc.gpx', 9.85, '4:31', 965, 965, 1611).addToMap(mapka)


mapa = folium.Map(location=[49.2, 20.0], zoom_start=7, control_scale=True)

# trasyCamino(mapa)
# trasySudety(mapa)
# trasyBeskidy(mapa)
trasyTatry(mapa)
trasySlovakia(mapa)
markers.caminoMarker(mapa)
markers.coronaMarker(mapa)
private.familyMarker(mapa)
methods.openWebbAndSave(mapa, 'Test.html')
