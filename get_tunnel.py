#!/usr/bin/env python3
import json
import requests
import os
from datetime import datetime

os.chdir('/media/Data3/rstudio/tunnel/rstudio')
git_readme = 'README.md'
readme_template = '[![RStudio](RStudio-Ball.png)](LINK_GOES_HERE)'
rstudio_port = 8787

for ngrok_api_port in range(4040,4050):
    try:
        raw_html = requests.get('http://localhost:{0:d}/api/tunnels'.format(ngrok_api_port))
        tunnel = json.loads(raw_html.content.decode())
        my_port = tunnel['tunnels'][0]['config']['addr'].split(':')[-1]
        if my_port == str(rstudio_port):
            my_url = tunnel['tunnels'][0]['public_url'].replace('http://','https://')
            readme_new = readme_template.replace('LINK_GOES_HERE', my_url)
            break
    except:
        readme_new = readme_template.replace('LINK_GOES_HERE', 'https://rstudio.com')
else:
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
        
