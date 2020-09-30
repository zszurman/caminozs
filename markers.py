import folium


def caminoMarker(mapka):
    folium.Marker([42.59967, -6.72743], popup='START Camino de Santiago 2019',
                  tooltip='Cacabelos',
                  icon=folium.Icon(color='pink', icon='info-sign')).add_to(mapka)

    folium.Marker([42.66113, -6.86426], popup='nocleg w Albergue Lamas',
                  tooltip='Pradela', icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)

    folium.Marker([42.70786, -7.04602], popup='nocleg w Albergue de Cebreiro',
                  tooltip='O Cebreiro', icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)

    folium.Marker([42.76624, -7.25352], popup='nocleg w Albergue Ecologico El Beso',
                  tooltip='Triacastela', icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)

    folium.Marker([42.77686, -7.4132], popup='nocleg w Albergue Casa Peltre',
                  tooltip='Saria', icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)

    folium.Marker([42.82525, -7.6961], popup='nocleg w Albergue Casa Garcia',
                  tooltip='Gonzar', icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)

    folium.Marker([42.87883, -7.92873], popup='nocleg w Albergue de Mato Casanova',
                  tooltip='Casanova', icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)

    folium.Marker([42.92624, -8.28054], popup='nocleg w Albergue Alborada',
                  tooltip='A Salceda', icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)

    folium.Marker([42.88064, -8.54461], popup='META Katedra Santiago de Compostela',
                  tooltip='Santiago de Compostela', icon=folium.Icon(color='pink', icon='info-sign')).add_to(mapka)

    folium.Marker([43.10184, -9.21229], popup='kąpiel w Atlantyku',
                  tooltip='Muxia', icon=folium.Icon(color='pink', icon='info-sign')).add_to(mapka)

    folium.Marker([42.91551, -9.26384], popup='kąpiel w Atlantyku',
                  tooltip='Fisterra', icon=folium.Icon(color='pink', icon='info-sign')).add_to(mapka)

    folium.Marker([46.42119, 11.68189], popup='nocleg w Hotel Dolomiti',
                  tooltip='Vigo di Fassa', icon=folium.Icon(color='pink', icon='bed', prefix='fa')).add_to(mapka)


def coronaMarker(mapka):
    folium.CircleMarker(location=[49.17955, 20.08807], color='yellow', radius=7, fill_color='yellow',
                        popup='Tatry',
                        tooltip='Rysy 2500 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.57307, 19.52952], color='yellow', radius=7, fill_color='yellow',
                        popup='Beskid Żywiecki',
                        tooltip='Babia Góra 1723 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.07455, 22.72625], color='yellow', radius=7, fill_color='yellow',
                        popup='Bieszczady',
                        tooltip='Tarnica 1346 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.54288, 20.11128], color='yellow', radius=7, fill_color='yellow',
                        popup='Gorce',
                        tooltip='Turbacz 1310 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.44935, 20.60433], color='yellow', radius=7, fill_color='yellow',
                        popup='Beskid Sądecki',
                        tooltip='Radziejowa 1266 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.68442, 19.03026], color='yellow', radius=7, fill_color='yellow',
                        popup='Beskid Śląski',
                        tooltip='Skrzyczne 1257 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.3804, 20.5554], color='yellow', radius=7, fill_color='yellow',
                        popup='Pieniny',
                        tooltip='Wysoka 1050 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.42663, 21.10289], color='yellow', radius=7, fill_color='yellow',
                        popup='Beskid Niski',
                        tooltip='Lackowa 997 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.76796, 19.16112], color='yellow', radius=7, fill_color='yellow',
                        popup='Beskid Mały',
                        tooltip='Czupel 933 mnpm').add_to(mapka)
    folium.CircleMarker(location=[49.7669, 20.05978], color='yellow', radius=7, fill_color='yellow',
                        popup='Beskid Makowski',
                        tooltip='Lubomir 904 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.73602, 15.73994], color='yellow', radius=7, fill_color='yellow',
                        popup='Karkonosze',
                        tooltip='Śnieżka 1603 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.20773, 16.84761], color='yellow', radius=7, fill_color='yellow',
                        popup='Masyw Śnieżnika',
                        tooltip='Śnieżnik 1426 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.84974, 15.42034], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Izerskie',
                        tooltip='Wysoka Kopa 1126 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.24482, 16.97641], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Bialskie',
                        tooltip='Rudawiec 1106 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.3532, 16.36071], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Orlickie',
                        tooltip='Orlica 1084 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.68037, 16.48552], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Sowie',
                        tooltip='Wielka Sowa 1015 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.26434, 17.0132], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Złote',
                        tooltip='Kowadło 988 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.25237, 16.56479], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Bystrzyckie',
                        tooltip='Jagodna 977 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.80854, 15.90003], color='yellow', radius=7, fill_color='yellow',
                        popup='Rudawy Janowickie',
                        tooltip='Skalnik 944 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.68081, 16.27809], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Kamienne',
                        tooltip='Waligóra 934 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.48412, 16.3434], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Stołowe',
                        tooltip='Szczeliniec 919 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.25668, 17.42877], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Opawskie',
                        tooltip='Biskupia Kopa 890 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.7796, 16.21107], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Wałbrzyskie',
                        tooltip='Chełmiec 851 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.45159, 16.75325], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Bardzkie',
                        tooltip='Kłodzka Góra 757 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.45356, 16.75845], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Bardzkie',
                        tooltip='Szeroka Góra 766 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.94398, 15.88468], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Kaczawskie',
                        tooltip='Skopiec 724 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.86406, 16.70745], color='yellow', radius=7, fill_color='yellow',
                        popup='Masyw Ślęży',
                        tooltip='Ślęża 718 mnpm').add_to(mapka)
    folium.CircleMarker(location=[50.89154, 20.89677], color='yellow', radius=7, fill_color='yellow',
                        popup='Góry Świętokrzyskie',
                        tooltip='Łysica 613 mnpm').add_to(mapka)
