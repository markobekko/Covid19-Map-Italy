import folium
import pandas as pd
from folium.plugins import MarkerCluster
import webbrowser
import os


def __main__():
    url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv"
    state_geo = "regioni.json"
    state_data = pd.read_csv(url)

    centro = [41.9028,12.4964]
    mappa_italia = folium.Map(location=centro, zoom_start=6)

    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=state_data,
        columns=["denominazione_regione", "nuovi_positivi"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Nuovi Positivi",
    ).add_to(mappa_italia)

    for index, state_data in state_data.iterrows():
        location = [state_data['lat'], state_data['long']]
        folium.Circle(location, radius = state_data["ricoverati_con_sintomi"] * 25,
                      popup=f'Regione:{state_data["denominazione_regione"]}\n Ricoverati con Sintomi:{state_data["ricoverati_con_sintomi"]}').add_to(
            mappa_italia)

    folium.LayerControl().add_to(mappa_italia)

    # Salva la mappa in un file .html e poi lo apre automaticamente
    mappa_italia.save('index2.html')
    filename = 'file:///' + os.getcwd() + '/' + 'index2.html'
    webbrowser.open_new_tab(filename)


__main__()
