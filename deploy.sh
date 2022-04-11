#!/bin/bash
NAME="SUPERFLUID_ETL_API"
FLASK_WSGI_MODULE="server"
NUM_WORKERS=10
NUM_THREADS=4
TIMEOUT=1800
PORT=3000

# Paths
PROJECT_DIR="/app"


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

# --daemon

# LOGS="${PROJECT_DIR}/logs/speed_logs.log"
# ERRORS_LOGS="${PROJECT_DIR}/logs/speed_logs.err"
# --log-file $LOGS \
# --error-logfile $ERRORS_LOGS \