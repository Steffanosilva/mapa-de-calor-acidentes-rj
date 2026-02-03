import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv('levantamento_de_acidentes_cprv_2024.csv')

mapa = folium.Map(location=[-22.9, -43.2], zoom_start=7)

HeatMap(
    data=df[['latitude', 'longitude', 'acidentes']].values,
    radius=25,
    blur=20
).add_to(mapa)

mapa.save('mapa_calor_acidentes_rj.html')