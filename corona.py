import requests
import logging
import time
from var_dump import var_dump
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd


def fetch_data():
  # api-endpoint 
  URL = "https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true"

  try:
      import http.client as http_client
  except ImportError:
      # Python 2
      import httplib as http_client
  http_client.HTTPConnection.debuglevel = 1

  # You must initialize logging, otherwise you'll not see debug output.
  # logging.basicConfig()
  # logging.getLogger().setLevel(logging.DEBUG)
  # requests_log = logging.getLogger("requests.packages.urllib3")
  # requests_log.setLevel(logging.DEBUG)
  # requests_log.propagate = True

  # sending get request and saving the response as response object 
  r = requests.get(url = URL) 

  # extracting data in json format 
  data = r.json()

  # var_dump(data)

  return data 

def display_chart():

  data = fetch_data()

  countries = []
  infecteds = []

  locations = {
    'Algeria': {
      'lat': 28.0217239,
      'lon': -2.8252919
    },
    'Austria': {
      'lat': 47.9876435,
      'lon': 10.4383811
    },
    'Azerbaijan': {
      'lat': 40.1704527,
      'lon': 46.6335368
    },
    'Bahrain': {
      'lat': 25.9406805,
      'lon': 50.3073945
    },
    'Belgium': {
      'lat': 50.4956972,
      'lon': 3.3452252
    },
    'Brazil': {
      'lat': -14.2374362,
      'lon': -60.3452921
    },
    'Bulgaria': {
      'lat': 42.7199105,
      'lon': 24.4223042
    },
    'Canada': {
      'lat': 54.6996992,
      'lon': -113.705567
    },
    'China': {
      'lat': 34.4214686,
      'lon': 86.0959349
    },
    'Czech Republic': {
      'lat': 49.7983577,
      'lon': 14.3540182
    },
    'Denmark': {
      'lat': 56.2098071,
      'lon': 9.3007224
    },
    'Estonia': {
      'lat': 58.0086177,
      'lon': 24.2660393
    },
    'Finland': {
      'lat': 64.6236661,
      'lon': 17.0954996
    },
    'France': {
      'lat': 46.1314512,
      'lon': -2.4340325
    },
    'Germany': {
      'lat': 51.0899906,
      'lon': 5.9701182
    },
    'Hungary': {
      'lat': 47.1556943,
      'lon': 18.3840033
    },
    'India': {
      'lat': 20.7506988,
      'lon': 73.7325795
    },
    'Iran': {
      'lat': 32.2148842,
      'lon': 49.1927242
    },
    'Italy': {
      'lat': 41.2036496,
      'lon': 8.224739
    },
    'Japan': {
      'lat': 32.676662,
      'lon': 129.4314367
    },
    'Kosovo': {
      'lat': 42.5612976,
      'lon': 20.3416784
    },
    'Lithuania': {
      'lat': 55.1684179,
      'lon': 22.762426
    },
    'Luxembourg': {
      'lat': 49.8149618,
      'lon': 5.8531481
    },
    'Malaysia': {
      'lat': 4.1279396,
      'lon': 105.1226791
    },
    'Netherlands': {
      'lat': 52.2076824,
      'lon': 4.1585021
    },
    'Nigeria': {
      'lat': 9.0270599,
      'lon': 6.4336152
    },
    'Norway': {
      'lat': 64.2868344,
      'lon': 8.7829839
    },
    'Pakistan': {
      'lat': 30.2825277,
      'lon': 64.8572158
    },
    'Palestine': {
      'lat': 31.8846662,
      'lon': 34.3316593
    },
    'Philippines': {
      'lat': 11.6628447,
      'lon': 118.1269378
    },
    'Poland': {
      'lat': 51.9324531,
      'lon': 16.8923509
    },
    'Portugal': {
      'lat': 37.1371578,
      'lon': -23.3157423
    },
    'Romania': {
      'lat': 45.9199658,
      'lon': 22.7777056
    },
    'Russia': {
      'lat': 49.7746371,
      'lon': 68.8775017
    },
    'Saudi Arabia': {
      'lat': 24.013336,
      'lon': 40.5815857
    },
    'Serbia': {
      'lat': 44.1888287,
      'lon': 18.6799444
    },
    'Singapore': {
      'lat': 1.3139961,
      'lon': 103.7041659
    },
    'Slovakia': {
      'lat': 48.6670444,
      'lon': 18.5786147
    },
    'Slovenia': {
      'lat': 46.1478781,
      'lon': 14.43263
    },
    'South Korea': {
      'lat': 35.7982143,
      'lon': 125.6303814
    },
    'Spain': {
      'lat': 40.1217816,
      'lon': -8.2007835
    },
    'Sweden': {
      'lat': 61.7424335,
      'lon': 8.4464236
    },
    'Switzerland': {
      'lat': 46.8077155,
      'lon': 7.1032839
    },
    'Turkey': {
      'lat': 39.0015575,
      'lon': 30.6896175
    },
    'United Kingdom': {
      'lat': 54.2191097,
      'lon': -13.4223412
    },
    'United States': {
      'lat': 37.258357,
      'lon': -104.6528767
    },
    'Vietnam': {
      'lat': 15.7477753,
      'lon': 101.4644837
    },
  }

  types = [
    {
      'key': 'recovered',
      'title': 'Recovered',
      'color': 'rgb(153, 184, 152)',
    },
    {
      'key': 'infected',
      'title': 'Infected',
      'color': 'rgb(254, 206, 171)',
    },
    {
      'key': 'deceased',
      'title': 'Deceased',
      'color': 'rgb(232, 74, 95)',
    },
    {
      'key': 'tested',
      'title': 'Tested',
      'color': 'rgb(204, 175, 175)',
    }
  ]

  fig = go.Figure()


  for index, item in enumerate(data, start=0):
    countries.append(item['country'])
    infecteds.append(item['infected'])

    for key, data_type in enumerate(types, start=0):
      value = 0
      if isinstance(item[data_type['key']], int):
        value = item[data_type['key']] / 50

      fig.add_trace(go.Scattergeo(
              lon = [locations[item['country']]['lon']],
              lat = [locations[item['country']]['lat']],
              text = item[data_type['key']],
              name = data_type['title'],
              marker = dict(
                  size = value,
                  color = data_type['color'],
                  line_width = 0
              )))

  # Inset
  fig.add_trace(go.Choropleth(
          locationmode = 'country names',
          locations = countries,
          z = infecteds,
          text = countries,
          colorscale = [[0,'rgb(185, 185, 185)'],[1,'rgb(185, 185, 185)']],
          autocolorscale = True,
          showscale = False,
          geo = 'geo'
      ))

  fig.update_layout(
      title = go.layout.Title(
          text = 'Corona cases reported by in world<br> \
  Source: <a href="https://apify.com/covid-19">\
  APIFY</a>'),
      geo = go.layout.Geo(
          resolution = 110,
          scope = 'world',
          showframe = False,
          showcoastlines = True,
          landcolor = "rgb(229, 229, 229)",
          countrycolor = "white" ,
          coastlinecolor = "white",
          projection_type = 'mercator',
          domain = dict(x = [ 0, 1 ], y = [ 0, 1 ])
      ),
  )

  fig.show()

display_chart()