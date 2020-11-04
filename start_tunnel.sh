#!/bin/bash
if [ "$0" == "/media/Data3/rstudio/tunnel/rstudio/start_tunnel.sh" ]; then
	sleep 90
fi
nohup /media/Data3/rstudio/bin/ngrok http 8787 -region eu -config=/home/scidev/.ngrok2/ngrok_rstudio-server.yml >& /dev/null &
sleep 60
/media/Data3/rstudio/tunnel/rstudio/get_tunnel.py
cd /media/Data3/rstudio/tunnel/rstudio
git add .
cur_date=$(date "+%Y%m%d%H%M%S")
git commit -m "Incheck at ${cur_date}"
git push
