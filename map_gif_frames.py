import plotly.express as px
import pandas as pd
from st_csv_dl import st_df

# old colorscale
# =============================================================================
# colorscale = ['rgb(193, 193, 193)',
#     'rgb(239,239,239)',
#     'rgb(195, 196, 222)',
#     'rgb(144,148,194)',
#     'rgb(101,104,168)',
#     'rgb(65, 53, 132)']
# =============================================================================

frames = []

dates = []

for i in st_df['date']:
    if i not in dates:
        dates.append(i)
dates = sorted(dates)
c = 0

# =============================================================================
# Through 10/10/2020 version of map, scale only went up to 300 cases per million 
# people. This needed to be changed as of 1/1/2020 as cases in some states reached
# over 1500 cases per million inhabitants. Chose an upper bound of 1000 cases per mil
# =============================================================================

colorscale = [[0.0, 'rgb(68, 1, 84)'],
 [0.05, 'rgb(67, 56, 128)'],
 [0.1, 'rgb(48, 104, 142)'],
 [0.15000000000000002, 'rgb(34, 144, 139)'],
 [0.2, 'rgb(52, 182, 121)'],
 [0.25, 'rgb(145, 214, 65)'],
 [0.30000000000000004, 'rgb(220, 227, 25)'],
 [0.35000000000000003, 'rgb(249, 241, 12)'],
 [0.4, 'rgb(249, 237, 0)'],
 [0.45, 'rgb(253, 193, 0)'],
 [0.5, 'rgb(252, 182, 0)'],
 [0.55, 'rgb(251, 145, 0)'],
 [0.6000000000000001, 'rgb(251, 93, 0)'],
 [0.65, 'rgb(251, 93, 0)'],
 [0.7000000000000001, 'rgb(251, 60, 0)'],
 [0.75, 'rgb(215, 0, 0)'],
 [0.8, 'rgb(153, 0, 0)'],
 [0.8500000000000001, 'rgb(92, 0, 0)'],
 [0.9, 'rgb(54, 0, 0)'],
 [0.9500000000000001, 'rgb(18, 0, 0)'],
 [1.0, 'rgb(0, 0, 0)']]


#creating a frame for a gif for each date recorded
for i in dates:
    # For last day of data set, creates 40 frames to give a "pause" at the end of gif to see current value
    # this is shorter in github version of gif to keep gif under 10 MB
    if i == dates[len(dates)-1]:
        while c < 40:
            temp_df = st_df.loc[st_df['date'] == i]
            tit = 'Covid-19 Cases per Million People'
            print(tit)
            fig = px.choropleth(temp_df, locations = 'state code', locationmode="USA-states", color= '7 Day Average', color_continuous_scale=colorscale, 
                            range_color=(0, 1000), scope="usa", title= tit)
            fig.add_annotation(x=.5,y=-.125, text=i, showarrow = False)
            fig.add_annotation(x=-.09375,y=1.15, text= 'Gar Esborn', showarrow = False)
            fname = str(i) + '_' + str(c) + '_US.png'
            print(fname)
            frames.append(fig.write_image(fname))
            c = c + 1
    else:
        #create temp DF for current day
        temp_df = st_df.loc[st_df['date'] == i]
        tit = 'Covid-19 Cases per Million People'
        print(tit)
        #create figure from temp DF from state code
        fig = px.choropleth(temp_df, locations = 'state code', locationmode="USA-states", color= '7 Day Average', color_continuous_scale=colorscale, 
                        range_color=(0, 1000), scope="usa", title= tit)
        # adds date of current data to img
        fig.add_annotation(x=.5,y=-.125, text=i, showarrow = False)
        fig.add_annotation(x=-.09375,y=1.15, text= 'Gar Esborn', showarrow = False)
        #create file name that can be easily called to create gif
        fname = str(i + '_US.png')
        print(fname)
        # adds frame to list, although alternative .py is used to create GIF
        frames.append(fig.write_image(fname))

