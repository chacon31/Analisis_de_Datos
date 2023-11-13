# -*- coding: utf-8 -*-
"""Laboratoria#5-Mapas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F3xqalnh7Fq3Yz1OourIN-IzWEnsWOjU

# Mapa de Costa Rica con 5 puntos donde se ubican las diferentes sedes de la Universidad Nacional.
"""

import folium
from folium.plugins import minimap

import folium
from folium.plugins import minimap
from folium.plugins import MiniMap
CR = folium.Map(location=(9.92816303807613, -84.08705325324966),zoom_start=9,tiles='stamenterrain')

punto1 = '<b>Sede Regional Brunca</b>'
punto2 = '<b>Sede Central</b>'
punto3 = '<b>Campus Benjamin Nuñez</b>'
punto4 = '<b>Interuniversitaria</b>'
punto5 = '<b>Sede Liberia</b>'
#Punto 1
folium.Marker(location=[9.379762649836177, -83.69165065430775],popup=punto1,icon=folium.Icon(color="orange",icon="ok-sing")).add_to(CR)
folium.Circle(location=[9.379762649836177, -83.69165065430775],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Sede Regional Brunca").add_to(CR)
#Punto 2
folium.Marker(location=[9.998850911465215, -84.11139616242562],popup=punto2,icon=folium.Icon(color="orange",icon="ok-sing")).add_to(CR)
folium.Circle(location=[9.998850911465215, -84.11139616242562],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Sede Central").add_to(CR)
#Punto 3
folium.Marker(location=[9.969786670821879, -84.12882284863505],popup=punto3,icon=folium.Icon(color="orange",icon="ok-sing")).add_to(CR)
folium.Circle(location=[9.969786670821879, -84.12882284863505],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Campus Benjamin Nuñez").add_to(CR)
#Punto 4
folium.Marker(location=[10.019488057380933, -84.19713575358111],popup=punto4,icon=folium.Icon(color="orange",icon="ok-sing")).add_to(CR)
folium.Circle(location=[10.019488057380933, -84.19713575358111],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Sede Interuniversitaria").add_to(CR)
#Punto 5
folium.Marker(location=[10.617538684765648, -85.45128854585938],popup=punto5,icon=folium.Icon(color="orange",icon="ok-sing")).add_to(CR)
folium.Circle(location=[10.617538684765648, -85.45128854585938],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Sede Liberia").add_to(CR)

minimap = MiniMap(title_layer='stamenterrain',position='bottomright')
CR.add_child(minimap)

CR.save('C:mapa.html')
CR

"""Codigo hecho en clase."""

USA = folium.Map(location=(39.74280599490961,-105.00625422297078))

USA

from folium.plugins import MiniMap
from branca.element import Figure

popuptext = '<b>Loveland</b>'

my_map = folium.Map(location=[39.74280599490961,-105.00625422297078],zoom_start=16,tiles='stamenterrain')

folium.Marker(location=[40.395261909417165, -105.07436783734191],popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sing")).add_to(my_map)

folium.Circle(location=[40.395261909417165, -105.07436783734191],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Loveland").add_to(my_map)

minimap = MiniMap(title_layer='stamenterrain',position='bottomright')

my_map.add_child(minimap)

my_map.save('C:mapa.html')
my_map