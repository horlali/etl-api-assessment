#!/bin/bash
NAME="SUPERFLUID_ETL_API"
FLASK_WSGI_MODULE="server"
NUM_WORKERS=10
NUM_THREADS=4
TIMEOUT=1800
PORT=3000

# Paths
PROJECT_DIR="/home/gideon/Desktop/PERSONAL/etl-api-assessment"


gunicorn $FLASK_WSGI_MODULE:app \
--name $NAME \
--chdir $PROJECT_DIR \
--timeout $TIMEOUT \
--bind=[::]:$PORT \
--log-level=debug \
--workers $NUM_WORKERS \
--threads=$NUM_THREADS \
--worker-class=gevent \
--pid=$PIDFILE 


