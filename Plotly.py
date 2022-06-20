#!/usr/bin/env python
# coding: utf-8

# ## Practice exercises on Plotly - 
# Until now, we have looked at various kind of basic plots available with Matplotlib and Seaborn. 
# 
# With Plotly we could take our visualizations to the next level via advance features that plotly offers namely:
# 1. Option to dynamically choose the sub-category to plot the data which could come in handy to selectively choose and  compare multiple categories/sub-categories plotted in the data
# 2. Customizations such as facets, marginal visualizations
# 3. Geo-political mapping
# 4. Animation feature- which could be used to visualize the changes in the target data over a chosen continuous value such as GDP of a country vs time
# 
# As part of this exercise, we would have a look at multiple kinds of plots suitable for various types of data, and try to see what customizations/features provided by Plotly could be leveraged to create a better infographic.
# 
# Generally, there are three different methods for visual data analysis:
# 1. Relationship
# 2. Comparison
# 3. Composition
# 
# As part of this exercise, we will focus on plotly to explore various plots and their corresponding features for each category, starting with Relationship analysis plots.
# 
# 

# In[1]:


#importing essential libraries
 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from sklearn.preprocessing import Standard
import os # accessing directory structure
import plotly
import plotly.express as px
import plotly.graph_objects as go


# ## 1. Checking the Relationship among variables - 
# 

# ## Scatter plot - 
# Scatter plots are used to check the relationship between the variables and the distribution of the data.
# With plotly, we have the option to add marginal plots such as histogram, box-plots next to the scatter plot in order to get a more summarized and comprehensive view of the data and to add to it we could dynamically choose the categories to plot from by selecting/de-selecting categories from the legend section.

# Task 1 -
# Explore the IMDb dataset used in the assignment, please find the csv file download link on the platform.
# 
# Plot a scatter plot using plotly to see the relationship between the 'Budget' vs 'Gross values' according to different genres. 
# Use plotly express to quickly configure the plot - https://plotly.com/python/plotly-express/
# 
# Subtasks for customizations - 
# 1. Subtask 1.1 - Try customizing your scatter plot with addition of marginal plots such as histogram, box plot or violin plot
# 2. Subtask 1.2 - Try linking hover-over data and try exploring the option to choose the genres dynamically
# 
# Your output should look like this -
# ![image.png](attachment:image.png)
# 

# In[2]:


#Enter your code here
movies =pd.read_csv('Movie+Assignment+Data.csv')
px.scatter(movies,x='budget',y='Gross', marginal_x="histogram", marginal_y="violin",hover_name='Title')


# In[3]:


px.scatter(movies,x='Runtime',y='IMDb_rating',marginal_x='histogram',hover_name='Title',marginal_y='violin',
           color='genre_1',size='IMDb_rating')


# Subtask 1.3 - 
# Try adding multiple facets to the scatter plot, so that we could view three genres - 'Action','Drama','Biography' side by side
# 
# Your output should look like this -
# ![image.png](attachment:image.png)

# In[6]:


px.scatter(z,x=z['Runtime'],y=z['IMDb_rating'],color='genre_1'
          ,facet_col='genre_1',hover_name='Title')


# Is the distribution of data much more evident from this plot?

# ## Bubble plot
# In the bubble plot, we add a third dimension of the data by linking it to the size of the marker; this could bring in additional insights from the data.
# 
# Subtask 1.4 - Try creating a bubble plot between IMDb rating and runtime and see if linking 'actor's Facebook likes' to the size of the marker bring out any additional insight from the plot.
# 
# Your output should look like this - 
# ![image.png](attachment:image.png)

# In[7]:


z=movies[(movies['genre_1']=='Action')|(movies['genre_1']=='Drama')|(movies['genre_1']=='Biography')]


# In[8]:


px.scatter(z,x=z['Runtime'],y=z['IMDb_rating'],color='genre_1'
          ,facet_col='genre_1',size='actor_1_facebook_likes',hover_name='Title')


# ## Animating the data plots
# Data animation against a continuous variable could be a helpful tool to add another dimension to the plot and see the values/pattern change with respect to the animator's value. 
# 
# Let us now explore this feature of plotly through Gapminder's dataset on 'GDP per capita vs life expectancy' 
# 
# This dataset covers the change in GDP per capita vs life expectancy over the years across different continents
# 
# To import this data simply use:
# df = px.data.gapminder()
# 
# Here is a reference on how to add animation to a scatter plot - https://plotly.com/python/plotly-express/
# 

# In[9]:


df = px.data.gapminder()
df.head()


# Subtask 1.5 - Plot the GDP per capita vs life expectancy for all the countries grouped in facets according to their respective continent and add an animation frame to it according to the 'year'
# 
# 
# Your output should look like this -
# ![image.png](attachment:image.png)

# In[10]:


px.scatter(df,x='gdpPercap',y='lifeExp',facet_col='continent',color='continent',animation_frame='year',
           hover_name='country',range_y=[25,90],log_x=True,size='pop',size_max=45)


# ## Comparison Plots

# Comparison plots are crucial to compare multiple variables with each other. Comparison plots are helpful to detect underlying patterns and relationship in-between the variables. 

# 1. Subtask 1- Plotting 'Many categories table chart'
# 
# Many categories table chart is used to plot multiple plots side by side in a tabular format; this chart is especially useful when we have multiple variables/dimensions along with multiple categorical values such the case in the below-mentioned dataset - where we have multiple categorical values - the day of the week, and numerous other variables (in this case - 6)
# 
# Plotly has given access to various inbuilt-datasets in the package, 'restaurant tips dataset' is one such data set that could be imported using command px.data.tips(), go ahead explore this data. 
# 
# Reference - https://plotly.com/python/plotly-express/

# In[11]:


df2 = px.data.tips()
df.head(5)


#  Subtask 1-
#     Create a comparison plot among different days of a week with respect to time of the day, total bill value and tip amount.    
#     Also, try color coding the client based on gender
#     
# Your output should look like this:
# ![image.png](attachment:image.png)

# In[12]:


px.scatter(df2,x='total_bill',y='tip',facet_col='day',facet_row='time',
          category_orders={'day':['Thur','Fri','Sat','Sun'],'time':['Lunch','Dinner']},color='sex'
          ,trendline='ols')


# ## Radar Chart/ Spyder Chart - 
# Radar chart are best used for comparing two products with each other against multiple sub-categories
# 
# More reference on radar charts can be found at this link - https://plotly.com/python/radar-chart/

# Subtask 2- We have data from various brands of beer; Create a radar chart to compare them as shown in image below:
# 1. Characterstics=      ['Bitterness','Froth','Price','Content', 'Mouthfeel']
# 2. Product A_corresponding_values= [1, 4, 2, 2, 3]
# 3. Product A_corresponding_values= [3, 2, 2.5, 1, 2]
# 4. Product A_corresponding_values= [4, 3, 4, 3.5, 2]
# 
# ![image.png](attachment:image.png)

# In[13]:


data={'Characterstics':['Bitterness','Froth','Price','Content', 'Mouthfeel'],'Product_A_corresponding_values':[1, 4, 2, 2, 3],
      'Product_B_corresponding_values': [3, 2, 2.5, 1, 2],'Product_C_corresponding_values': [4, 3, 4, 3.5, 2]}

df1=pd.DataFrame(data)

df1


# In[14]:


fig=go.Figure()
for i in df1.columns[1:]:
    fig.add_trace(go.Scatterpolar(theta=df1.loc[:,df1.columns[0]],
                                  r=df1.loc[:,i],
                                  fill='toself',name=i[:10]
                ))
fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=True
)

fig.show()


# ## Area line chart
# Line charts and area line chart are suitable for time-based data plotting example - population increase over the years as seen in Gapminder's dataset is time-based data
# 
# Area line charts are helpful to show categorically stacked data, for example, if we wanted to see the trend of population stack of various continents changing over-time we would use this plot
# 
# Note: the lines are randomly placed, each filled area corresponds to one value of the column given by the line_group parameter.
# 
# Reference - https://plotly.com/python/filled-area-plots/

# Subtask 3-
# 
# Import Gapminder dataset using command -  df = px.data.gapminder()
# 
# Plot an area line chart between 'population' and 'years', and colour code the line_group according to the continent.
# 
# Your output should look like this:
# ![image.png](attachment:image.png)

# In[15]:


px.area(df,x='year',y='pop',color='continent',line_group='country')


# ## Boxplot and Violin plot 
# Boxplot and Violin plot are great plots to have a summarized view of the data, let us try and see how well they summarize the info on 'Restaurant tips dataset'
# 
# Try loading the dataset using code: 
# df = px.data.tips()
# 
# Boxplot reference - https://plotly.com/python/box-plots/
# Violin plot reference - https://plotly.com/python/violin/

# Subtask 4 - Create box plot on resturant tips dataset between the variables 'total bill' vs 'day of the week' and color code based on gender
# ![image.png](attachment:image.png)

# In[16]:


px.box(df2,x='day',y='total_bill',color='sex',notched=True)


# ## Violin plot
# Violin plots are similar to Boxplots, but they have an addition of a rotated kernel density plot on each side. Violin plots are particularly helpful in case we want to know the density of datapoints in a particular section.
# 
# You can find more info on Violin plots here - https://plotly.com/python/violin/
# 

# Subtask - 5
# Try and create violin plot on the restaurant tips dataset between 'total_bill' vs 'day of the week' and color code it based on gender
# Your output should look like this -
# ![image.png](attachment:image.png)

# In[17]:


px.violin(df2,x='day',y='total_bill',color='sex')


# ## Composition
# You would be already aware of charts such as pie chart, which are suitable to check composition within the data, with plotly we can go a step ahead and build Sunburst charts;
# 
# Introducing Sunburst chart, using which we could create an interactive pie chart wherein the parents of the components can also be mapped, Sunburst chart is especially helpful when we have multiple children columns/categories and even their corresponding parent categories
# You can find more info on Sunburst chart here:
# https://plotly.com/python/sunburst-charts/

# Subtask 1 - Create a sunburst chart to plot world population from the gapminder's datset; map the population of the countries to there respective continent and color code the plot based on gdp per capita
# 
# Your output should look like this -
# ![image.png](attachment:image.png)

# In[18]:


df.head()


# In[19]:


df=px.data.gapminder().query('year==2007')

fig=px.sunburst(df,path=['continent','country'],values='pop',color='gdpPercap',color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['gdpPercap'], weights=df['pop']))
fig.show()


# ## Geo-political map plots 
# 
# We can also have a look at the gapminders's data directly on world map, with plotly we have access to easy to use geo-political map plots - 
# You can see the syntax for map plots here - https://plotly.com/python/maps/
# 
# With plotly, we can plot various type of geopolitical map such as:
# 1. A Choropleth map -  is a type of thematic map in which areas are shaded or patterned in proportion to a statistical variable that represents an aggregate summary of a geographic characteristic within each region, such as population density or per-capita income.
# 2. A bubble map plot - is a variation of map plots, bubble map plots are especially helpful to plot time-based geopolitical data which closely focuses on a continuous variable that could be linked to the size of the marker.

# Subtask 2- 
# Plot life expectancy across all countries from the gapminder dataset for the year 2007 on the Choropleth map, color code the data based on life expectancy
# 
# Your output should look like this -
# ![image.png](attachment:image.png)

# In[20]:


fig = px.choropleth(df, locations='iso_alpha', color='lifeExp', hover_name='country', 
                    animation_frame='year')
fig.show()


# Subtask - 3
# Plot the country-wise world population using a bubble-map plot and add 'year' as animation_variable to it.
# Also, try adjusting the size of the marker by using argument 'size_max=50'
# 
# Find reference for this task here-
# https://plotly.com/python/bubble-maps/
# 
# Your output should look like this -
# ![image.png](attachment:image.png)

# In[ ]:


df=px.data.gapminder()
fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",animation_frame='year',size_max=60,
                     projection="natural earth")
fig.show()


# An essential aspect of plotly is to export the visualizations in a interactive format i.e. the HTML format, to export any figure created by plotly into HTML format add the command - 'fig.write_html("path/to/file.html")' within the same cell. 
# 
# Reference - https://plotly.com/python/interactive-html-export/
# 
# To export the images in static format such as '.PNG' use the 'save as '.PNG' option available on the upper right end of the plot or use this link for command reference - https://plotly.com/python/static-image-export/
# 
# 

# Subtask 3.1 - Export the geopolitical plot into an interactive format
# 
# If you like some of these graphs and also feel excited about it, please feel free to share these plots on social media platforms, to showcase newly learned skill, this would also help you and your peers to learn from each other's expertise.
# 

# In[ ]:


from dash import Dash, dcc, html
import plotly.express as px
from base64 import b64encode
import io

app = Dash(__name__)

buffer = io.StringIO()

df = px.data.gapminder()
fig = px.scatter(
    df, x="gdpPercap", y="pop", 
    color="continent")
fig.write_html(buffer)

html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

app.layout = html.Div([
    html.H4('Simple plot export options'),
    html.P("↓↓↓ try downloading the plot as PNG ↓↓↓", style={"text-align": "right", "font-weight": "bold"}),
    dcc.Graph(id="graph", figure=fig),
    html.A(
        html.Button("Download as HTML"), 
        id="download",
        href="data:text/html;base64," + encoded,
        download="plotly_graph.html"
    )
])

app.run_server(debug=True, use_reloader=False)
fig.show()


# In[ ]:




