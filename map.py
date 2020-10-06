# Map to show the distribution of confirmed coronavirus cases across the world (circular markers).
# Student Action: Run the code below.
#Data Source https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series.git
import pandas as pd # Data processing 
import matplotlib.pyplot as plt # Data visualisation
import folium # Cartograms / maps
conf_csv = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
conf_df = pd.read_csv(conf_csv)
world_map = folium.Map(location=[0, 0], width='100%', height='80%', tiles='Stamen Toner', zoom_start=2.25)
last_col = conf_df.columns[-1]
for i in conf_df.index:
  folium.Circle(location=[conf_df.loc[i, 'Lat'], conf_df.loc[i, 'Long']], 
                radius=int(conf_df.loc[i, last_col]), 
                popup=conf_df.loc[i, 'Country/Region'] + '\n' + str(conf_df.loc[i, last_col]),
                color='crimson', fill=True, fill_color='crimson').add_to(world_map)
world_map