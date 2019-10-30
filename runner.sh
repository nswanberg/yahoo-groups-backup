#!/bin/sh

until python yahoo-groups-backup.py   \
          --config=settings.yaml \
          scrape_messages BoulderTrailRunners --driver=chrome; do
    echo "backup stopped with exit code $?. Respawning..." >&2
    sleep 30
done
