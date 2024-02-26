import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pycountry
import io
import plotly.io as pio

def load_data(url):
    try:
        data = pd.read_csv(url)
        data['date'] = pd.to_datetime(data['date']).dt.date  # Convert to datetime.date
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def create_plot(data, x, y, color, title):
    fig = px.line(data, x=x, y=y, color=color, title=title)
    fig.update_layout(xaxis_title='Date', yaxis_title=y.capitalize())  # Update y-axis title dynamically
    return fig

def get_iso3_code(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except:
        return None



url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
data = load_data(url)

# Convert country names to ISO-3 codes
data['iso_alpha'] = data['location'].apply(get_iso3_code)

if data is not None:
    st.title('**COVID-19 Dashboard**')    



side_bar = st.sidebar

continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']

# Filter out the names of continents from the 'location' column
country_options = sorted([country for country in data['location'].unique() if country not in continents])

# Allow the user to select multiple countries
selected_countries = st.sidebar.multiselect('Select countries:', options=country_options)

#
for selected_country in selected_countries:
    # Filter the data for the selected country
    country_data = data[data['location'] == selected_country]

    # Ensure 'date' column is in datetime format
    country_data['date'] = pd.to_datetime(country_data['date'])

    # Create a filled line graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=country_data['date'], y=country_data['total_cases'], fill='tozeroy', mode='none', name='Total Cases'))
    fig.add_trace(go.Scatter(x=country_data['date'], y=country_data['total_deaths'], fill='tozeroy', mode='none', name='Total Deaths'))
    # fig.add_trace(go.Scatter(x=country_data['date'], y=country_data['total_recoveries'], fill='tozeroy', mode='none', name='Total Recoveries'))  # Replace 'total_recoveries' with the correct column name for recoveries in your dataset

    # Customize the layout
    fig.update_layout(title=f'Covid Evolution for {selected_country}', xaxis_title='Date', yaxis_title='Count')

    # Display the plot in Streamlit
    st.plotly_chart(fig)
#    

with side_bar.expander('Date Range Settings', expanded=False):
    min_date = data['date'].min()
    max_date = data['date'].max()
    start_date = side_bar.date_input('Start date', min_date, min_value=min_date, max_value=max_date)
    end_date = side_bar.date_input('End date', max_date, min_value=min_date, max_value=max_date)

# Create a mapping of countries to continents
country_to_continent = data.drop_duplicates('location').set_index('location')['continent'].to_dict()

# Automatically select the continents of the selected countries
selected_continents = [country_to_continent[country] for country in selected_countries]

with side_bar.expander('Region Settings', expanded=False):
    interactive_filter = side_bar.multiselect(
        'Filter by region:',
        options=sorted(data['continent'].dropna().unique()),
        default=selected_continents  # Set the default value based on the selected countries
    )

with side_bar.expander('Metric Settings', expanded=False):
    metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
    selected_metric = side_bar.selectbox('Select a metric:', metric_options)

country_data = data[data['location'].isin(selected_countries)]
country_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
country_data = country_data[country_data['continent'].isin(interactive_filter)]

# Replace 'nan' values in the selected metric column with a default size
country_data[selected_metric] = country_data[selected_metric].fillna(0)

fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric.capitalize()} over time')
st.plotly_chart(fig)

st.download_button('Download data', data=data.to_csv(), mime='text/csv')

fig = px.choropleth(country_data, locations='iso_alpha', hover_name='location', projection='natural earth', color_continuous_scale='Reds', animation_frame='date', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} by country')
fig.update_layout(geo=dict(showframe=False))
st.plotly_chart(fig)

fig = px.scatter(country_data, x=selected_metric, y='total_deaths', color='location')
fig.update_layout(title=f'{selected_metric.capitalize()} vs. Total Deaths', xaxis_title=selected_metric.capitalize(), yaxis_title='Total Deaths')
st.plotly_chart(fig)

fig = px.histogram(country_data, x=selected_metric, color='location')
fig.update_layout(title=f'Histogram of {selected_metric.capitalize()}')
st.plotly_chart(fig)

fig = px.box(country_data, x='continent', y=selected_metric, color='location')
fig.update_layout(title=f'Box plot of {selected_metric.capitalize()} by continent')
st.plotly_chart(fig)

selected_date_data = country_data[country_data['date'] == start_date]

# if st.button('Export plot as PNG', key='export_plot'):
#     fig.write_image("plot.png")
if st.button('Export plot as PNG', key='export_plot'):
    img_bytes = pio.to_image(fig, format="png")
    st.download_button(
        label="Download plot as PNG",
        data=io.BytesIO(img_bytes),
        file_name='plot.png',
        mime='image/png'
    )

fig = px.sunburst(country_data, path=['continent', 'location'], values=selected_metric, color='continent', title=f'Sunburst chart of {selected_metric.capitalize()} by country and continent')
st.plotly_chart(fig)