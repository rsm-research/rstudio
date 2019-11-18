#!/usr/bin/env python3
import json
import requests
import os
from datetime import datetime

git_readme = 'README.md'
readme_template = '[![RStudio](RStudio-Ball.png)](LINK_GOES_HERE)'

try:
    raw_html = requests.get('http://localhost:4040/api/tunnels')
    tunnel = json.loads(raw_html.content.decode())
    my_url = tunnel['tunnels'][0]['public_url'].replace('http://','https://')
    readme_new = readme_template.replace('LINK_GOES_HERE', my_url)
except:
    readme_new = readme_template.replace('LINK_GOES_HERE', 'https://rstudio.com')

readme_new = readme_new + '\n'

try:
    with open(git_readme, 'r') as fp:
        readme_old = fp.read()
except FileNotFoundError:
    readme_old = 'file does not exist'

if readme_old != readme_new:
    with open(git_readme, 'w') as fp:
        fp.write(readme_new)
    now = datetime.now().strftime('%Y%m%d%H%M')
    os.system('git add README.md')
    os.system('git commit -m "README.md at {0:s}"'.format(now))
    os.system('git push')
        
