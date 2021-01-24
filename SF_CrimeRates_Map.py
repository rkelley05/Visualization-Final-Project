import folium
import numpy as np
import pandas as pd
from pandas import read_csv
import matplotlib as mpl
import matplotlib.pyplot as plt

file = "Police_Department_Incidents_-_Previous_Year__2016_.csv"
police_df= pd.read_csv(file)

police_df.drop(['IncidntNum', 'Category', 'Descript', 'DayOfWeek', 'Date', 'Time', 'Resolution', 'Address', 'X', 'Y', 'Location', 'PdId'], axis=1, inplace=True)
value_count = police_df['PdDistrict'].value_counts()
countdf = pd.DataFrame(value_count)
countdf = countdf.reset_index()
countdf.columns = ['Neighborhood', 'Count']

sf_geo = r'san-francisco.geojson'

sf_map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

folium.Choropleth(
    geo_data=sf_geo,
    data=countdf,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco'
).add_to(sf_map)

folium.LayerControl().add_to(sf_map)


# display map
sf_map


