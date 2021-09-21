import folium
import pandas as pd
import webbrowser
import os


def __main__():
    url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv"
    corona_dataset = pd.read_csv(url)
    print(corona_dataset.head())

    centro = [41.9028,12.4964]
    mappa_italia = folium.Map(location=centro, zoom_start=6)

    for index, corona_dataset in corona_dataset.iterrows():
        location = [corona_dataset['lat'], corona_dataset['long']]
        folium.Circle(location, radius = corona_dataset["ricoverati_con_sintomi"] * 25,
                      popup=f'Regione:{corona_dataset["denominazione_regione"]}\n Ricoverati con Sintomi:{corona_dataset["ricoverati_con_sintomi"]}').add_to(
            mappa_italia)

    # Salva la mappa in un file .html e poi lo apre automaticamente
    mappa_italia.save('index.html')
    filename = 'file:///' + os.getcwd() + '/' + 'index.html'
    webbrowser.open_new_tab(filename)


__main__()