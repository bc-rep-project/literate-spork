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
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import uuid

# Load the COVID-19 data from a public URL
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
data = pd.read_csv(url)

# Set the title of the app
st.title('**COVID-19 Dashboard**')

# Create a sidebar for user input
side_bar = st.sidebar
side_bar.markdown('**Select Countries:**')
selected_countries = side_bar.multiselect(
    '',
    options=data['location'].unique(),
    default=data['location'].unique()
)

# Filter the data by country
country_data = data[data['location'].isin(selected_countries)]

# Create a line chart of the COVID-19 data
fig = px.line(country_data, x='date', y='total_cases', color='location', title='COVID-19 cases over time')
fig.update_layout(xaxis_title='Date', yaxis_title='Number of cases')
st.plotly_chart(fig)

# Add a date range filter
start_date = pd.to_datetime(country_data['date'].min()).to_pydatetime()
# end_date = pd.to_datetime(side_bar.date_input('End Date', country_data['date'].max()))
# start_date = pd.to_datetime(country_data['date'].min().to_pydatetime())
end_date = pd.to_datetime(country_data['date'].max()).to_pydatetime()


# Filter the data by the specified date range
# date_range_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
# date_range_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]
date_range_data = country_data[(pd.to_datetime(country_data['date']) >= start_date) & (pd.to_datetime(country_data['date']) <= end_date)]

# Update the line chart with the new data
fig = px.line(date_range_data, x='date', y='total_cases', color='location', title=f'COVID-19 cases over time from {start_date} to {end_date}')
fig.update_layout(xaxis_title='Date', yaxis_title='Number of cases')
st.plotly_chart(fig)

# Interactive filtering
interactive_filter = side_bar.multiselect(
    'Filter by Region:',
    options=country_data['continent'].unique(),
    default=country_data['continent'].unique()
)

# Filter the data by the selected regions
filtered_data = country_data[country_data['continent'].isin(interactive_filter)]

# Update the line chart with the filtered data
fig = px.line(filtered_data, x='date', y='total_cases', color='location', title='COVID-19 cases over time')
st.plotly_chart(fig)

# Download the data as a CSV file
st.download_button('Download Data', data=data.to_csv(), mime='text/csv')

# Choropleth map
fig = px.choropleth(country_data, locations='location', color='total_cases', scope='world', title='COVID-19 cases in selected countries')
fig.update_layout(geo=dict(showframe=False))
st.plotly_chart(fig)

# Table of the data
st.table(country_data)

# Save and load custom visualizations
saved_visualizations = st.session_state.get('saved_visualizations', [])
if st.button('Save Visualization'):
    saved_visualizations.append(fig)
    st.session_state.saved_visualizations = saved_visualizations
if saved_visualizations:
    st.write('Saved Visualizations:')
    for i, visualization in enumerate(saved_visualizations):
        st.plotly_chart(visualization)

# Share visualizations via a unique URL
share_link = st.empty()
if st.button('Share Visualization'):
    unique_id = str(uuid.uuid4())
    share_link.markdown(f'Share this link to share the visualization: {st.session_state.sharing_url}/{unique_id}')
    st.session_state.shared_visualizations[unique_id] = fig


#------------2nd-------------
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
# start_date = pd.to_datetime(str(country_data['date'].min()))
# end_date = pd.to_datetime(side_bar.date_input('End Date', country_data['date'].max()))

# # Filter the data by the specified date range
# date_range_data = country_data[(country_data['date'] >= start_date) & (country_data['date'] <= end_date)]

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
#     st.session_state.saved_visualizations = saved_visualizationsif saved_visualizations:
#     st.write('Saved Visualizations:')
#     for i, visualization in enumerate(saved_visualizations):
#         st.plotly_chart(visualization)

# # Share visualizations via a unique URL
# share_link = st.empty()
# if st.button('Share Visualization'):
#     unique_id = str(uuid.uuid4())
#     share_link.markdown(f'Share this link to share the visualization: {st.session_state.sharing_url}/{unique_id}')
#     st.session_state.shared_visualizations[unique_id] = fig