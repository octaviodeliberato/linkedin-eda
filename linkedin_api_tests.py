# IMPORTS --------------------------------------------------------------------

import pandas as pd
from linkedin_api import Linkedin
from dotenv import dotenv_values

# CONFIG ---------------------------------------------------------------------

# Get my credentials from .env file
config = dotenv_values(".env")

# TEST THE API --------------------------------------------------------------

# Authenticate using any Linkedin account credentials
api = Linkedin(config['USERNAME'], config['PASSWORD'])

# GET a profile
profile = api.get_profile('williammazza')

import json
# convert profile dict to json
profile_json = json.dumps(profile)
# write json to file
with open('data/profile.json', 'w') as f:
    json.dump(profile, f)

# GET a profiles contact info
contact_info = api.get_profile_contact_info('williammazza')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('williammazza')
