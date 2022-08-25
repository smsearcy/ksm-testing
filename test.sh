#!/usr/bin/env bash

# Helper script for running Pyramid web service via Gunicorn

# Increase the number of workers to replicate production

workers=1

while getopts ':w:' OPTION; do
    case "$OPTION" in
        w)
            workers="$OPTARG"
            ;;
        ?)
            echo "Usage: $(basename $0) [-w WORKER_COUNT] [-t TIMEOUT]"
            exit 1
            ;;
    esac
done

gunicorn --bind=127.0.0.1:8000 --workers=$workers web:wsgi
