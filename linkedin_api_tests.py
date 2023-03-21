# IMPORTS --------------------------------------------------------------------

import pandas as pd
# import numpy as np
# import plotly.express as px
from linkedin_api import Linkedin
from dotenv import dotenv_values
import os

# CONFIG ---------------------------------------------------------------------

# Get my credentials from .env file
config = dotenv_values(".env")

# TEST THE API --------------------------------------------------------------

# Authenticate using any Linkedin account credentials
api = Linkedin(config['USERNAME'], config['PASSWORD'])

# GET a profile
profile = api.get_profile('williammazza')

# GET a profiles contact info
contact_info = api.get_profile_contact_info('williammazza')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('williammazza')