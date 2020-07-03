#!/bin/bash
if [ "$0" == "/media/Data3/rstudio/tunnel/rstudio/start_tunnel.sh" ]; then
	sleep 90
fi
nohup /media/Data3/rstudio/tunnel/bin/ngrok http 8787 -region eu -config=/home/scidev/.ngrok2/ngrok_rstudio-server.yml >& /dev/null &
