# import calendar
# from datetime import datetime
# import plotly.graph_objects as go
# import streamlit as st
# from streamlit_option_menu import option_menu
# import matplotlib.pyplot as plt

# #----------------Settings--------
# incomes = ["Salary", "Blog", "Other", "Income"]
# expenses = ["Rent", "Utilities", "Groceries", "Car", "Other expenses", "Savings"]
# currency = "USD"
# page_title =  "Income and Expense Tracker"
# page_icon = ":money_with_wings:"
# layout = "centered"

# #----------------Page config-----------
# st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
# st.title(page_title + " " + page_icon)
# #-----------------Dropdown values for selecting the period---
# years = [datetime.today().year, datetime.today().year + 1]
# months = list(calendar.month_name[1:])

# #------Hide Streamlit style----
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# #-------Navigation menu--------
# selected = option_menu(
#     menu_title=None,
#     options=["Data Entry", "Data Visualization"],
#     icons=["pencil-square", "bar-chart-fill"],
#     orientation="horizontal",

# )


# #---------------Input & Save periods-----
# if selected == "Data Entry":
#     st.header(f"Data Entry in (currency)")
#     with st.form("entry_form", clear_on_submit=True):
#         col1, col2 = st.columns(2)
#         col1.selectbox("Select Month:", months, key="month")
#         col2.selectbox("Select Year", years, key="year")
#         with st.expander("Income"):
#             for income in incomes:
#                 st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
#         with st.expander("Expenses"):
#             for expense in expenses:
#                 st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
#         with st.expander("Comment"):
#             comment = st.text_area("", placeholder="Enter a comment here")

#         submitted = st.form_submit_button("Save Data")

#     if submitted:
#         period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
#         incomes = {income: st.session_state[income] for income in incomes}
#         expenses = {expense: st.session_state[expense] for expense in expenses}
#         #TODO: Insert the values into the database
#         st.write(f"incomes: {incomes}")
#         st.write(f"expenses: {expenses}")
#         st.success("Data saved!")


# #-------------Plot periods--------
# if selected == "Data Visualization":
#     st.header("Data Visualization")
#     with st.form("saved_periods"):
#         # TODO: Get periodsfrom database
#         period = st.selectbox("Select Period:", ["2022_March"])
#         submitted = st.form_submit_button("Plot Period")
#         if submitted:
#             # TODO: Get data from database
#             comment = "Some comment"
#             incomes = {'Salary': 1500, 'Blog': 50, 'Other Income': 10}
#             expenses = {'Rent': 600, 'Utilities': 200, 'Groceries': 300,
#                         'Car': 100, 'Other Expenses': 50, 'Saving': 10}
            
#             #---Create metrics
#             total_income = sum(incomes.values())
#             total_expense = sum(expenses.values())
#             remaining_budget = total_income - total_expense
#             col1, col2, col3, = st.columns(3)
#             col1.metric("Total Income", f"{total_income} {currency}")
#             col2.metric("Total Expense", f"{total_expense} {currency}")
#             col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
#             st.text(f"Comment: {comment}")

#             #----Create sankey chart
#             label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
#             source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
#             target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses]
#             value = list(incomes.values()) + list(expenses.values())

#             #-----Data to dict, Dict to data----
#             link = dict(source=source, target=target, value=value)
#             node = dict(label=label, pad=20, thickness=30, color="#E694FF")
#             data = go.Sankey(link=link, node=node)

#             #-----Plot outcome---
#             fig = go.Figure(data)
#             fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
#             st.plotly_chart(fig, use_container_width=True)


#------------1st----------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# import uuid

# # Load the COVID-19 data from a public URL
# url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
# data = pd.read_csv(url)

# # Set the title of the app
# st.title('**COVID-19 Dashboard**')

# # Create a sidebar for user input
# side_bar = st.sidebar
# side_bar.markdown('**Select Countries:**')
# selected_countries = side_bar.multiselect(
#     '',
#     options=data['location'].unique(),
#     default=data['location'].unique()
# )

# # Filter the data by country
# country_data = data[data['location'].isin(selected_countries)]

# # Create a line chart of the COVID-19 data
# fig = px.line(country_data, x='date', y='total_cases', color='location', title='COVID-19 cases over time')
# fig.update_layout(xaxis_title='Date', yaxis_title='Number of cases')
# st.plotly_chart(fig)

# # Add a date range filter
# start_date = pd.to_datetime(country_data['date'].min()).to_pydatetime()
# # end_date = pd.to_datetime(side_bar.date_input('End Date', country_data['date'].max()))
# # start_date = pd.to_datetime(country_data['date'].min().to_pydatetime())
# end_date = pd.to_datetime(country_data['date'].max()).to_pydatetime()


# # Filter the data by the specified date range
# # date_range_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
# # date_range_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
# date_range_data = country_data[(pd.to_datetime(country_data['date']) >= start_date) & (pd.to_datetime(country_data['date']) <= end_date)]

# # Update the line chart with the new data
# fig = px.line(date_range_data, x='date', y='total_cases', color='location', title=f'COVID-19 cases over time from {start_date} to {end_date}')
# fig.update_layout(xaxis_title='Date', yaxis_title='Number of cases')
# st.plotly_chart(fig)

# # Interactive filtering
# interactive_filter = side_bar.multiselect(
#     'Filter by Region:',
#     options=country_data['continent'].unique(),
#     default=country_data['continent'].unique()
# )

# # Filter the data by the selected regions
# filtered_data = country_data[country_data['continent'].isin(interactive_filter)]

# # Update the line chart with the filtered data
# fig = px.line(filtered_data, x='date', y='total_cases', color='location', title='COVID-19 cases over time')
# st.plotly_chart(fig)

# # Download the data as a CSV file
# st.download_button('Download Data', data=data.to_csv(), mime='text/csv')

# # Choropleth map
# fig = px.choropleth(country_data, locations='location', color='total_cases', scope='world', title='COVID-19 cases in selected countries')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

# # Table of the data
# st.table(country_data)

# # Save and load custom visualizations
# saved_visualizations = st.session_state.get('saved_visualizations', [])
# if st.button('Save Visualization'):
#     saved_visualizations.append(fig)
#     st.session_state.saved_visualizations = saved_visualizations
# if saved_visualizations:
#     st.write('Saved Visualizations:')
#     for i, visualization in enumerate(saved_visualizations):
#         st.plotly_chart(visualization)

# # Share visualizations via a unique URL
# share_link = st.empty()
# if st.button('Share Visualization'):
#     unique_id = str(uuid.uuid4())
#     share_link.markdown(f'Share this link to share the visualization: {st.session_state.sharing_url}/{unique_id}')
#     st.session_state.shared_visualizations[unique_id] = fig


#------------2nd-------------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objs as go
# import uuid
# import base64

# def load_data(url):
#     try:
#         data = pd.read_csv(url)
#         data['date'] = pd.to_datetime(data['date'])
#         return data
#     except Exception as e:
#         st.error(f"Error loading data: {e}")
#         return None

# def create_plot(data, x, y, color, title):
#     fig = px.line(data, x=x, y=y, color=color, title=title)
#     fig.update_layout(xaxis_title='Date', yaxis_title='Number of cases')
#     return fig

# # url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
# url = 'https://storage.googleapis.com/covid19-open-data/v3/latest/aggregated.csv'
# data = load_data(url)
# if data is not None:
#     print(data.columns)
#     st.title('**COVID-19 Dashboard**')

#     side_bar = st.sidebar

#     selected_countries = side_bar.multiselect(
#         'Select countries:',
#         options=data['location'].unique(),
#         default=data['location'].unique()
#     )

#     country_data = data[data['location'].isin(selected_countries)]

#     # start_date = side_bar.date_input('Start date', country_data['date'].min())
#     # end_date = side_bar.date_input('End date', country_data['date'].max())

#     # date_range_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]

#     # Convert the Python date objects to pandas Timestamps
#     start_date = pd.Timestamp(side_bar.date_input('Start date', country_data['date'].min()))
#     end_date = pd.Timestamp(side_bar.date_input('End date', country_data['date'].max()))

#     # Filter the data based on the selected date range
#     date_range_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
    

#     interactive_filter = side_bar.multiselect(
#         'Filter by region:',
#         options=country_data['continent'].unique(),
#         default=country_data['continent'].unique()
#     )

#     region_data = country_data[country_data['continent'].isin(interactive_filter)]

#     st.download_button('Download data', data=data.to_csv(), mime='text/csv')

#     st.table(country_data)

#     # saved_visualizations = st.session_state.get('saved_visualizations', [])
#     # if st.button('Save visualization'):
#     #     saved_visualizations.append(fig)
#     #     st.session_state.saved_visualizations = saved_visualizations

#     # if saved_visualizations:
#     #     st.write('**Saved visualizations:**')
#     #     for i, visualization in enumerate(saved_visualizations):
#     #         st.plotly_chart(visualization)

#     # Add a widget to select a metric.
#     metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
#     selected_metric = side_bar.selectbox('Select a metric:', metric_options)

#     # Create a line chart of the selected metric over time.
#     fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric} over time')
#     st.plotly_chart(fig)

#     # Create a scatter plot of total cases vs. total deaths.
#     fig = px.scatter(country_data, x='total_cases', y='total_deaths', color='location')
#     fig.update_layout(title='Total cases vs. total deaths')
#     st.plotly_chart(fig)

#     # Add a histogram of total cases.
#     fig = px.histogram(country_data, x='total_cases', color='location')
#     fig.update_layout(title='Histogram of total cases')
#     st.plotly_chart(fig)

#     # Add a box plot of total cases by continent.
#     fig = px.box(country_data, x='continent', y='total_cases', color='location')
#     fig.update_layout(title='Box plot of total cases by continent')
#     st.plotly_chart(fig)

#     # Add a map of total cases.
#     # fig = px.scatter_geo(country_data, locations='location', color='total_cases', hover_name='location', size='total_cases', projection='orthographic')
#     # Handle MessageSizeError
#     smaller_data = country_data.sample(frac=0.1)  # Adjust the fraction as needed

#     # Handle ValueError
#     smaller_data['total_cases'] = smaller_data['total_cases'].fillna(0)  # Replace NaNs with 0

#     # Then use 'smaller_data' in your visualizations
#     fig = px.scatter_geo(smaller_data, locations='location', color='total_cases', hover_name='location', size='total_cases', projection='orthographic')

#     fig.update_layout(title='Map of total cases', geo=dict(showframe=False))
#     st.plotly_chart(fig)

#     # Add a slider to select the date.
#     date_slider = side_bar.slider(
#         'Select a date:',
#         min_value=country_data['date'].min(),
#         max_value=country_data['date'].max()
#     )

#     # Filter the data based on the selected date.
#     selected_date_data = country_data[country_data['date'] == date_slider]

#     # Create a choropleth map of total cases for the selected date.
#     fig = px.choropleth(selected_date_data, locations='location', color='total_cases', scope='world', title=f'Total cases on {date_slider}')
#     fig.update_layout(geo=dict(showframe=False))
#     st.plotly_chart(fig)

#     # Add a button to export the plot as a PNG image.
#     if st.button('Export plot as PNG'):
#         fig.write_image("plot.png")

#     # Add a sunburst chart of total cases by country and continent.
#     fig = px.sunburst(country_data, path=['continent', 'location'], values='total_cases', color='continent', title='Sunburst chart of total cases by country and continent')
#     st.plotly_chart(fig)


#------------3rd-----------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objs as go
# import uuid
# import base64

# def load_data(url):
#     try:
#         data = pd.read_csv(url)
#         data['date'] = pd.to_datetime(data['date'])
#         return data
#     except Exception as e:
#         st.error(f"Error loading data: {e}")
#         return None

# def create_plot(data, x, y, color, title):
#     fig = px.line(data, x=x, y=y, color=color, title=title)
#     fig.update_layout(xaxis_title='Date', yaxis_title='Number of cases')
#     return fig

# url = 'https://storage.googleapis.com/covid19-open-data/v3/latest/aggregated.csv'  # Google Health aggregated data
# data = load_data(url)
# if data is not None:
#     print(data.columns)
#     st.title('**COVID-19 Dashboard**')

#     side_bar = st.sidebar

#     selected_countries = side_bar.multiselect(
#         'Select countries:',
#         options=data['country'].unique(),  # Adjusted column name
#         default=data['country'].unique()  # Adjusted column name
#     )

#     country_data = data[data['country'].isin(selected_countries)]  # Adjusted column name

#     start_date = pd.Timestamp(side_bar.date_input('Start date', country_data['date'].min()))
#     end_date = pd.Timestamp(side_bar.date_input('End date', country_data['date'].max()))

#     date_range_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]

#     interactive_filter = side_bar.multiselect(
#         'Filter by region:',
#         options=country_data['continent'].unique(),
#         default=country_data['continent'].unique()
#     )

#     region_data = country_data[country_data['continent'].isin(interactive_filter)]

#     st.download_button('Download data', data=data.to_csv(), mime='text/csv')

#     st.table(country_data)

#     # Add a widget to select a metric.
#     metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
#     selected_metric = side_bar.selectbox('Select a metric:', metric_options)

#     # Create a line chart of the selected metric over time.
#     fig = create_plot(country_data, 'date', selected_metric, 'country', f'{selected_metric} over time')  # Adjusted column name

#     # Create a scatter plot of total cases vs. total deaths.
#     fig = px.scatter(country_data, x='total_cases', y='total_deaths', color='country')  # Adjusted column name
#     fig.update_layout(title='Total cases vs. total deaths')
#     st.plotly_chart(fig)

#     # Add a histogram of total cases.
#     fig = px.histogram(country_data, x='total_cases', color='country')  # Adjusted column name
#     fig.update_layout(title='Histogram of total cases')
#     st.plotly_chart(fig)

#     # Add a box plot of total cases by continent.
#     fig = px.box(country_data, x='continent', y='total_cases', color='country')  # Adjusted column name
#     fig.update_layout(title='Box plot of total cases by continent')
#     st.plotly_chart(fig)

#     # Add a map of total cases.
#     fig = px.scatter_geo(country_data, locations='country', color='total_cases', hover_name='country', size='total_cases', projection='orthographic')  # Adjusted column name
#     fig.update_layout(title='Map of total cases', geo=dict(showframe=False))
#     st.plotly_chart(fig)

#     # Add a slider to select the date.
#     date_slider = side_bar.slider(
#         'Select a date:',
#         min_value=country_data['date'].min(),
#         max_value=country_data['date'].max()
#     )

#     # Filter the data based on the selected date.
#     selected_date_data = country_data[country_data['date'] == date_slider]

#     # Create a choropleth map of total cases for the selected date.
#     fig = px.choropleth(selected_date_data, locations='country', color='total_cases', scope='world', title=f'Total cases on {date_slider}')  # Adjusted column name
#     fig.update_layout(geo=dict(showframe=False))
#     st.plotly_chart(fig)

#     # Add a button to export the plot as a PNG image.
#     if st.button('Export plot as PNG'):
#         fig.write_image("plot.png")

#     # Add a sunburst chart of total cases by country and continent.
#     fig = px.sunburst(country_data, path=['continent', 'country'], values='total_cases', color='continent', title='Sunburst chart of total cases by country and continent')  # Adjusted column name
#     st.plotly_chart(fig)



#--------------4th----------------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objs as go
# import uuid
# # import base64
# # import kaleido

# def load_data(url):
#     try:
#         data = pd.read_csv(url)
#         data['date'] = pd.to_datetime(data['date'])
#         return data
#     except Exception as e:
#         st.error(f"Error loading data: {e}")
#         return None

# def create_plot(data, x, y, color, title):
#     fig = px.line(data, x=x, y=y, color=color, title=title)
#     fig.update_layout(xaxis_title='Date', yaxis_title='Number of cases')
#     return fig

# url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
# data = load_data(url)
# data = data[data['continent'].notna()]

# # Now you can sort the unique values
# continents = sorted(data['continent'].unique())
# data['continent'] = data['continent'].astype(str)

# # Now you can sort the unique values
# continents = sorted(data['continent'].unique())

# if data is not None:
#     st.title('**COVID-19 Dashboard**')    

# # side_bar = st.sidebar

# # with st.expander('Select countries'):
# #     selected_countries = side_bar.multiselect(
# #         'Select countries:',
# #         options=data['location'].unique(),
# #         default=data['location'].unique()
# #     )

# # with st.expander('Select date range'):
# #     start_date = side_bar.date_input('Start date', data['date'].min())
# #     end_date = side_bar.date_input('End date', data['date'].max())

# # with st.expander('Filter by region'):
# #     interactive_filter = side_bar.multiselect(
# #         'Filter by region:',
# #         options=data['continent'].unique(),
# #         default=data['continent'].unique()
# #     )

# # with st.expander('Select a metric'):
# #     metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
# #     selected_metric = side_bar.selectbox('Select a metric:', metric_options)

# # with st.expander('Select a date'):
# #     date_slider = side_bar.slider(
# #         'Select a date:',
# #         min_value=data['date'].min(),
# #         max_value=data['date'].max()
# #     )
    
# # Create a sidebar for user input.
# side_bar = st.sidebar

# # Add a title for the sidebar
# side_bar.title("COVID-19 Dashboard Settings")

# # Add a collapsible section for country selection.
# with side_bar.expander('Country Settings', expanded=False):
#     selected_countries = side_bar.multiselect(
#         'Select countries:',
#         options=data['location'].unique()
#     )

# # Add a collapsible section for date range selection.
# with side_bar.expander('Date Range Settings', expanded=False):
#     start_date = side_bar.date_input('Start date', data['date'].min())
#     end_date = side_bar.date_input('End date', data['date'].max())

# # Add a collapsible section for region selection.
# with side_bar.expander('Region Settings', expanded=False):
#     interactive_filter = side_bar.multiselect(
#         'Filter by region:',
#         options=data['continent'].unique()
#     )

# # Add a collapsible section for metric selection.
# with side_bar.expander('Metric Settings', expanded=False):
#     metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
#     selected_metric = side_bar.selectbox('Select a metric:', metric_options)

# # Convert 'date' column to native Python datetime objects
# data['date'] = data['date'].dt.to_pydatetime()

# # Now you can use the 'date' column with the slider function
# date_slider = side_bar.slider(
#     'Select a date:',
#     min_value=data['date'].min(),
#     max_value=data['date'].max()
# )

# country_data = data[data['location'].isin(selected_countries)]
# country_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
# country_data = country_data[country_data['continent'].isin(interactive_filter)]

# fig = create_plot(country_data, 'date', 'total_cases', 'location', 'Total cases over time')
# st.plotly_chart(fig)

# st.download_button('Download data', data=data.to_csv(), mime='text/csv')

# fig = px.choropleth(country_data, locations='location', color='total_cases', scope='world', title='Total cases by country')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

# st.table(country_data)

# st.session_state.saved_visualizations = st.session_state.get('saved_visualizations', [])

# if st.button('Save visualization'):
#     st.session_state.saved_visualizations.append(fig)

# if st.session_state.saved_visualizations:
#     st.write('**Saved visualizations:**')
#     for i, visualization in enumerate(st.session_state.saved_visualizations):
#         st.plotly_chart(visualization)

# share_link = st.empty()
# if st.button('Share visualization'):
#     visualization_id = str(uuid.uuid4())
#     share_link.markdown(f'Share this link to share the visualization: {st.session_state.share_url}/{visualization_id}')
#     st.session_state.saved_visualizations[visualization_id] = fig

# fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric} over time')
# st.plotly_chart(fig)

# fig = px.scatter(country_data, x='total_cases', y='total_deaths', color='location')
# fig.update_layout(title='Total cases vs. total deaths')
# st.plotly_chart(fig)

# fig = px.histogram(country_data, x='total_cases', color='location')
# fig.update_layout(title='Histogram of total cases')
# st.plotly_chart(fig)

# fig = px.box(country_data, x='continent', y='total_cases', color='location')
# fig.update_layout(title='Box plot of total cases by continent')
# st.plotly_chart(fig)

# fig = px.scatter_geo(country_data, locations='location', color='total_cases', hover_name='location', size='total_cases', projection='orthographic')
# fig.update_layout(title='Map of total cases', geo=dict(showframe=False))
# st.plotly_chart(fig)

# selected_date_data = country_data[country_data['date'] == date_slider]

# fig = px.choropleth(selected_date_data, locations='location', color='total_cases', scope='world', title=f'Total cases on {date_slider}')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

# if st.button('Export plot as PNG', key='export_plot'):
#     fig.write_image("plot.png")

# fig = px.sunburst(country_data, path=['continent', 'location'], values='total_cases', color='continent', title='Sunburst chart of total cases by country and continent')
# st.plotly_chart(fig)



    #---------------5th--------------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objs as go
# import uuid
# # import base64
# # import kaleido

# def load_data(url):
#     try:
#         data = pd.read_csv(url)
#         data['date'] = pd.to_datetime(data['date']).dt.date  # Convert to datetime.date
#         return data
#     except Exception as e:
#         st.error(f"Error loading data: {e}")
#         return None

# def create_plot(data, x, y, color, title):
#     fig = px.line(data, x=x, y=y, color=color, title=title)
#     fig.update_layout(xaxis_title='Date', yaxis_title='Number of cases')
#     return fig

# url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
# data = load_data(url)

# if data is not None:
#     st.title('**COVID-19 Dashboard**')    

# side_bar = st.sidebar

# with side_bar.expander('Country Settings', expanded=False):
#     selected_countries = side_bar.multiselect(
#         'Select countries:',
#         options=sorted(data['location'].unique())
#     )

# with side_bar.expander('Date Range Settings', expanded=False):
#     min_date = data['date'].min()
#     max_date = data['date'].max()
#     start_date = side_bar.date_input('Start date', min_date, min_value=min_date, max_value=max_date)
#     end_date = side_bar.date_input('End date', max_date, min_value=min_date, max_value=max_date)

# with side_bar.expander('Region Settings', expanded=False):
#     interactive_filter = side_bar.multiselect(
#         'Filter by region:',
#         options=sorted(data['continent'].dropna().unique())
#     )

# # with side_bar.expander('Metric Settings', expanded=False):
# #     metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
# #     selected_metric = side_bar.selectbox('Select a metric:', metric_options)
# with side_bar.expander('Metric Settings', expanded=False):
#     metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
#     selected_metric = side_bar.selectbox('Select a metric:', metric_options)

# country_data = data[data['location'].isin(selected_countries)]
# country_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
# country_data = country_data[country_data['continent'].isin(interactive_filter)]

# # fig = create_plot(country_data, 'date', 'total_cases', 'location', 'Total cases over time')
# # st.plotly_chart(fig)
# fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric.capitalize()} over time')
# st.plotly_chart(fig)

# st.download_button('Download data', data=data.to_csv(), mime='text/csv')

# fig = px.choropleth(country_data, locations='location', color='total_cases', scope='world', title='Total cases by country')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

# st.table(country_data)

# st.session_state.saved_visualizations = st.session_state.get('saved_visualizations', [])

# if st.button('Save visualization'):
#     st.session_state.saved_visualizations.append(fig)

# if st.session_state.saved_visualizations:
#     st.write('**Saved visualizations:**')
#     for i, visualization in enumerate(st.session_state.saved_visualizations):
#         st.plotly_chart(visualization)

# share_link = st.empty()
# if st.button('Share visualization'):
#     visualization_id = str(uuid.uuid4())
#     share_link.markdown(f'Share this link to share the visualization: {st.session_state.share_url}/{visualization_id}')
#     st.session_state.saved_visualizations[visualization_id] = fig

# # fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric} over time')
# # st.plotly_chart(fig)
# fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric.capitalize()} over time')
# fig.update_layout(xaxis_title='Date', yaxis_title=selected_metric.capitalize())
# st.plotly_chart(fig)

# # fig = px.scatter(country_data, x=selected_metric, y='total_deaths', color='location')
# # fig.update_layout(title=f'{selected_metric} vs. total deaths')
# # st.plotly_chart(fig)
# fig = px.scatter(country_data, x=selected_metric, y='total_deaths', color='location')
# fig.update_layout(title=f'{selected_metric.capitalize()} vs. Total Deaths', xaxis_title=selected_metric.capitalize(), yaxis_title='Total Deaths')
# st.plotly_chart(fig)

# # fig = px.histogram(country_data, x='total_cases', color='location')
# # fig.update_layout(title='Histogram of total cases')
# # st.plotly_chart(fig)
# fig = px.histogram(country_data, x=selected_metric, color='location')
# fig.update_layout(title=f'Histogram of {selected_metric.capitalize()}')
# st.plotly_chart(fig)

# # fig = px.box(country_data, x='continent', y='total_cases', color='location')
# # fig.update_layout(title='Box plot of total cases by continent')
# # st.plotly_chart(fig)
# fig = px.box(country_data, x='continent', y=selected_metric, color='location')
# fig.update_layout(title=f'Box plot of {selected_metric.capitalize()} by continent')
# st.plotly_chart(fig)

# country_data['total_cases'] = country_data['total_cases'].fillna(0)

# country_data[selected_metric] = country_data[selected_metric].fillna(0)

# # fig = px.scatter_geo(country_data, locations='location', color=selected_metric, hover_name='location', size=selected_metric, projection='orthographic')
# # fig.update_layout(title=f'Map of {selected_metric}', geo=dict(showframe=False))
# # st.plotly_chart(fig)
# fig = px.scatter_geo(country_data, locations='location', color=selected_metric, hover_name='location', size=selected_metric, projection='orthographic')
# fig.update_layout(title=f'Map of {selected_metric.capitalize()}', geo=dict(showframe=False))
# st.plotly_chart(fig)

# selected_date_data = country_data[country_data['date'] == start_date]

# # fig = px.choropleth(selected_date_data, locations='location', color=selected_metric, scope='world', title=f'{selected_metric} on {start_date}')
# # fig.update_layout(geo=dict(showframe=False))
# # st.plotly_chart(fig)
# fig = px.choropleth(selected_date_data, locations='location', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} on {start_date}')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

# if st.button('Export plot as PNG', key='export_plot'):
#     fig.write_image("plot.png")

# # fig = px.sunburst(country_data, path=['continent', 'location'], values=selected_metric, color='continent', title=f'Sunburst chart of {selected_metric} by country and continent')
# # st.plotly_chart(fig)
# fig = px.sunburst(country_data, path=['continent', 'location'], values=selected_metric, color='continent', title=f'Sunburst chart of {selected_metric.capitalize()} by country and continent')
# st.plotly_chart(fig)



#-------------------6th---------------------


# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objs as go
# import uuid
# import pycountry

# def get_iso3_code(country_name):
#     try:
#         return pycountry.countries.lookup(country_name).alpha_3
#     except:
#         return None

# def load_data(url):
#     try:
#         data = pd.read_csv(url)
#         data['date'] = pd.to_datetime(data['date']).dt.date  # Convert to datetime.date
#         return data
#     except Exception as e:
#         st.error(f"Error loading data: {e}")
#         return None

# def create_plot(data, x, y, color, title):
#     fig = px.line(data, x=x, y=y, color=color, title=title)
#     fig.update_layout(xaxis_title='Date', yaxis_title=y.capitalize())  # Update y-axis title dynamically
#     return fig

# url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
# data = load_data(url)

# if data is not None:
#     st.title('**COVID-19 Dashboard**')    

# side_bar = st.sidebar

# country_to_continent = data.drop_duplicates('location').set_index('location')['continent'].to_dict()

# with side_bar.expander('Country Settings', expanded=False):
#     selected_countries = side_bar.multiselect(
#         'Select countries:',
#         options=sorted(data['location'].unique())
#     )

# selected_continents = [country_to_continent[country] for country in selected_countries]

# with side_bar.expander('Region Settings', expanded=False):
#     interactive_filter = side_bar.multiselect(
#         'Filter by region:',
#         options=sorted(data['continent'].dropna().unique()),
#         default=selected_continents  # Set the default value based on the selected countries
#     )

# with side_bar.expander('Date Range Settings', expanded=False):
#     min_date = data['date'].min()
#     max_date = data['date'].max()
#     start_date = side_bar.date_input('Start date', min_date, min_value=min_date, max_value=max_date)
#     end_date = side_bar.date_input('End date', max_date, min_value=min_date, max_value=max_date)

# # with side_bar.expander('Region Settings', expanded=False):
# #     interactive_filter = side_bar.multiselect(
# #         'Filter by region:',
# #         options=sorted(data['continent'].dropna().unique())
# #     )

# with side_bar.expander('Metric Settings', expanded=False):
#     metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
#     selected_metric = side_bar.selectbox('Select a metric:', metric_options)

# country_data = data[data['location'].isin(selected_countries)]
# country_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
# country_data = country_data[country_data['continent'].isin(interactive_filter)]

# # Replace 'nan' values in the selected metric column with a default size
# country_data[selected_metric] = country_data[selected_metric].fillna(0)

# # fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric.capitalize()} over time')
# # st.plotly_chart(fig)
# fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric.capitalize()} over time for selected countries')
# st.plotly_chart(fig)

# st.download_button('Download data', data=data.to_csv(), mime='text/csv')

# # fig = px.choropleth(country_data, locations='location', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} by country')
# # fig.update_layout(geo=dict(showframe=False))
# # st.plotly_chart(fig)

# # st.table(country_data)

# fig = px.choropleth(country_data, locations='location', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} by country')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

# st.table(country_data)

# st.session_state.saved_visualizations = st.session_state.get('saved_visualizations', [])

# if st.button('Save visualization'):
#     st.session_state.saved_visualizations.append(fig)

# if st.session_state.saved_visualizations:
#     st.write('**Saved visualizations:**')
#     for i, visualization in enumerate(st.session_state.saved_visualizations):
#         st.plotly_chart(visualization)

# share_link = st.empty()
# if st.button('Share visualization'):
#     visualization_id = str(uuid.uuid4())
#     share_link.markdown(f'Share this link to share the visualization: {st.session_state.share_url}/{visualization_id}')
#     st.session_state.saved_visualizations[visualization_id] = fig

# # fig = px.scatter(country_data, x=selected_metric, y='total_deaths', color='location')
# # fig.update_layout(title=f'{selected_metric.capitalize()} vs. Total Deaths', xaxis_title=selected_metric.capitalize(), yaxis_title='Total Deaths')
# # st.plotly_chart(fig)

# # fig = px.scatter(country_data, x=selected_metric, y='total_deaths', color='location')
# # fig.update_layout(title=f'{selected_metric.capitalize()} vs. Total Deaths for selected countries', xaxis_title=selected_metric.capitalize(), yaxis_title='Total Deaths')
# # st.plotly_chart(fig)

# fig = px.scatter(country_data, x=selected_metric, y='total_deaths', color='location')
# fig.update_layout(title=f'{selected_metric.capitalize()} vs. Total Deaths', xaxis_title=selected_metric.capitalize(), yaxis_title='Total Deaths')
# st.plotly_chart(fig)

# fig = px.histogram(country_data, x=selected_metric, color='location')
# fig.update_layout(title=f'Histogram of {selected_metric.capitalize()}')
# st.plotly_chart(fig)

# fig = px.box(country_data, x='continent', y=selected_metric, color='location')
# fig.update_layout(title=f'Box plot of {selected_metric.capitalize()} by continent')
# st.plotly_chart(fig)

# # fig = px.scatter_geo(country_data, locations='location', color=selected_metric, hover_name='location', size=selected_metric, projection='orthographic')
# # fig.update_layout(title=f'Map of {selected_metric.capitalize()}', geo=dict(showframe=False))
# # st.plotly_chart(fig)

# # fig = px.scatter_geo(country_data, locations='location', color=selected_metric, hover_name='location', size=selected_metric, projection='natural earth', color_continuous_scale=px.colors.sequential.Plasma, title=f'Map of {selected_metric.capitalize()}')
# # fig.update_geos(showcountries=True, showcoastlines=True, showland=True, landcolor="lightgray", lakecolor="white", oceancolor="azure", countrycolor="darkgray")
# # fig.update_layout(title=f'Map of {selected_metric.capitalize()} for selected countries', geo=dict(showframe=False))
# # st.plotly_chart(fig)

# fig = px.scatter_geo(country_data, locations='location', color=selected_metric, hover_name='location', size=selected_metric, projection='natural earth', color_continuous_scale=px.colors.sequential.Plasma)
# fig.update_geos(showcountries=True, showcoastlines=True, showland=True, landcolor="lightgray", lakecolor="white", oceancolor="azure", countrycolor="darkgray")
# fig.update_layout(title=f'Map of {selected_metric.capitalize()}', geo=dict(showframe=False))
# st.plotly_chart(fig)

# selected_date_data = country_data[country_data['date'] == start_date]

# # fig = px.choropleth(selected_date_data, locations='location', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} on {start_date}')
# # fig.update_layout(geo=dict(showframe=False))
# # st.plotly_chart(fig)
# fig = px.choropleth(selected_date_data, locations='location', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} on {start_date} for selected countries')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

# if st.button('Export plot as PNG', key='export_plot'):
#     fig.write_image("plot.png")

# # fig = px.sunburst(country_data, path=['continent', 'location'], values=selected_metric, color='continent', title=f'Sunburst chart of {selected_metric.capitalize()} by country and continent')
# # st.plotly_chart(fig)
# fig = px.sunburst(country_data, path=['continent', 'location'], values=selected_metric, color='continent', title=f'Sunburst chart of {selected_metric.capitalize()} by country and continent for selected countries')
# st.plotly_chart(fig)



#-----------------7th------------------
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import uuid
# import base64
# import kaleido
import pycountry

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

with side_bar.expander('Country Settings', expanded=False):
    selected_countries = side_bar.multiselect(
        'Select countries:',
        options=sorted(data['location'].unique())
    )

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

fig = px.choropleth(country_data, locations='iso_alpha', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} by country')
fig.update_layout(geo=dict(showframe=False))
st.plotly_chart(fig)

st.table(country_data)

st.session_state.saved_visualizations = st.session_state.get('saved_visualizations', [])

if st.button('Save visualization'):
    st.session_state.saved_visualizations.append(fig)

if st.session_state.saved_visualizations:
    st.write('**Saved visualizations:**')
    for i, visualization in enumerate(st.session_state.saved_visualizations):
        st.plotly_chart(visualization)

share_link = st.empty()
if st.button('Share visualization'):
    visualization_id = str(uuid.uuid4())
    share_link.markdown(f'Share this link to share the visualization: {st.session_state.share_url}/{visualization_id}')
    st.session_state.saved_visualizations[visualization_id] = fig

fig = px.scatter(country_data, x=selected_metric, y='total_deaths', color='location')
fig.update_layout(title=f'{selected_metric.capitalize()} vs. Total Deaths', xaxis_title=selected_metric.capitalize(), yaxis_title='Total Deaths')
st.plotly_chart(fig)

fig = px.histogram(country_data, x=selected_metric, color='location')
fig.update_layout(title=f'Histogram of {selected_metric.capitalize()}')
st.plotly_chart(fig)

fig = px.box(country_data, x='continent', y=selected_metric, color='location')
fig.update_layout(title=f'Box plot of {selected_metric.capitalize()} by continent')
st.plotly_chart(fig)

fig = px.scatter_geo(country_data, locations='iso_alpha', color=selected_metric, hover_name='location', size=selected_metric, projection='natural earth', color_continuous_scale=px.colors.sequential.Plasma)
fig.update_geos(showcountries=True, showcoastlines=True, showland=True, landcolor="lightgray", lakecolor="white", oceancolor="azure", countrycolor="darkgray")
fig.update_layout(title=f'Map of {selected_metric.capitalize()}', geo=dict(showframe=False))
st.plotly_chart(fig)

selected_date_data = country_data[country_data['date'] == start_date]

# fig = px.choropleth(selected_date_data, locations='iso_alpha', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} on {start_date}')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

if st.button('Export plot as PNG', key='export_plot'):
    fig.write_image("plot.png")

fig = px.sunburst(country_data, path=['continent', 'location'], values=selected_metric, color='continent', title=f'Sunburst chart of {selected_metric.capitalize()} by country and continent')
st.plotly_chart(fig)


#------------8th----------------
# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objs as go
# # import uuid
# # import base64
# # import kaleido
# import pycountry

# def load_data(url):
#     try:
#         data = pd.read_csv(url)
#         data['date'] = pd.to_datetime(data['date']).dt.date  # Convert to datetime.date
#         return data
#     except Exception as e:
#         st.error(f"Error loading data: {e}")
#         return None

# def create_plot(data, x, y, color, title):
#     fig = px.line(data, x=x, y=y, color=color, title=title)
#     fig.update_layout(xaxis_title='Date', yaxis_title=y.capitalize())  # Update y-axis title dynamically
#     return fig

# def get_iso3_code(country_name):
#     try:
#         return pycountry.countries.lookup(country_name).alpha_3
#     except:
#         return None

# url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
# data = load_data(url)

# # Convert country names to ISO-3 codes
# data['iso_alpha'] = data['location'].apply(get_iso3_code)

# if data is not None:
#     st.title('**COVID-19 Dashboard**')    

# side_bar = st.sidebar

# with side_bar.expander('Country Settings', expanded=False):
#     selected_countries = side_bar.multiselect(
#         'Select countries:',
#         options=sorted(data['location'].unique())
#     )

# with side_bar.expander('Date Range Settings', expanded=False):
#     min_date = data['date'].min()
#     max_date = data['date'].max()
#     start_date = side_bar.date_input('Start date', min_date, min_value=min_date, max_value=max_date)
#     end_date = side_bar.date_input('End date', max_date, min_value=min_date, max_value=max_date)

# # Create a mapping of countries to continents
# country_to_continent = data.drop_duplicates('location').set_index('location')['continent'].to_dict()

# # Automatically select the continents of the selected countries
# selected_continents = [country_to_continent[country] for country in selected_countries]

# with side_bar.expander('Region Settings', expanded=False):
#     interactive_filter = side_bar.multiselect(
#         'Filter by region:',
#         options=sorted(data['continent'].dropna().unique()),
#         default=selected_continents  # Set the default value based on the selected countries
#     )

# with side_bar.expander('Metric Settings', expanded=False):
#     metric_options = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
#     selected_metric = side_bar.selectbox('Select a metric:', metric_options)

# country_data = data[data['location'].isin(selected_countries)]
# country_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
# country_data = country_data[country_data['continent'].isin(interactive_filter)]

# # Replace 'nan' values in the selected metric column with a default size
# country_data[selected_metric] = country_data[selected_metric].fillna(0)

# # Create a line chart of the selected metric over time for all selected countries
# fig = create_plot(country_data, 'date', selected_metric, 'location', f'{selected_metric.capitalize()} over time')
# st.plotly_chart(fig)

# # Create a scatter plot of total cases vs. total deaths for all selected countries
# fig = px.scatter(country_data, x=selected_metric, y='total_deaths', color='location')
# fig.update_layout(title=f'{selected_metric.capitalize()} vs. Total Deaths', xaxis_title=selected_metric.capitalize(), yaxis_title='Total Deaths')
# st.plotly_chart(fig)

# # Create a scatter_geo plot for all selected countries
# fig = px.scatter_geo(country_data, locations='iso_alpha', color=selected_metric, hover_name='location', size=selected_metric, projection='natural earth', color_continuous_scale=px.colors.sequential.Plasma)
# fig.update_geos(showcountries=True, showcoastlines=True, showland=True, landcolor="lightgray", lakecolor="white", oceancolor="azure", countrycolor="darkgray")
# fig.update_layout(title=f'Map of {selected_metric.capitalize()}', geo=dict(showframe=False))
# st.plotly_chart(fig)

# selected_date_data = country_data[country_data['date'] == pd.to_datetime(start_date)]

# # Create a choropleth map of total cases for the selected date for all selected countries
# fig = px.choropleth(selected_date_data, locations='iso_alpha', color=selected_metric, scope='world', title=f'{selected_metric.capitalize()} on {start_date}')
# fig.update_layout(geo=dict(showframe=False))
# st.plotly_chart(fig)

# # Create a sunburst chart of total cases by country and continent for all selected countries
# fig = px.sunburst(country_data, path=['continent', 'location'], values=selected_metric, color='continent', title=f'Sunburst chart of {selected_metric.capitalize()} by country and continent')
# st.plotly_chart(fig)