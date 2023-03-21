# IMPORTS --------------------------------------------------------------------

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# DATA -----------------------------------------------------------------------
network = pd.read_csv('data/Connections.csv')
network.head(10)
network.info()


# ANALYSIS -------------------------------------------------------------------

# Convert 'Connected On' to datetime
network['Connected On'] = pd.to_datetime(network['Connected On'])

# Nr of connectons over time
plot_dat = network.groupby(by='Connected On').count().reset_index()

connections_line = px.line(plot_dat, 
                           x="Connected On", 
                           y="First Name", 
                           labels={'First Name': 'Number'},
                           title='My Connections')
connections_line.show()

# Which organizations do the people in my network work at?
company_dat = network['Company'].value_counts()

# Convert company_dat to a dataframe with two columns: Company and Count
company_dat = pd.DataFrame(company_dat).reset_index().set_axis(['Company', 'Count'], axis=1, copy=False)

# Plot company_dat as a tree map using px
tree_map = px.treemap(company_dat, path=['Company'], values='Count', title='My Network Companies')
tree_map.show()

# Extract the position with frequency greater than 0.5%
network['Position'].value_counts()[network['Position'].value_counts()/len(network) * 100 > 0.5]

px.bar(network.groupby(by='Position').count().sort_values(by='First Name', ascending=False)[:10].reset_index(),
       x='Position',
       y='First Name',
       labels={'First Name': 'Number'},
       title= 'Positions in my LinkedIn Network'
      )

