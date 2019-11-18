#!/bin/bash
if [ "$0" == "/home/jeroene/rstudio/start_tunnel.sh" ]; then
	sleep 90
fi
nohup ngrok http 8787 -region eu >& /dev/null &
