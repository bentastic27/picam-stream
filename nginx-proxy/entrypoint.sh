#!/bin/bash

python3 /config-gen.py
nginx -g "daemon off;" &

while true; do
  sleep 60

  OLDSUM=$(md5sum /etc/nginx/conf.d/default.conf | cut -f1 -d' ')
  python3 /config-gen.py
  NEWSUM=$(md5sum /etc/nginx/conf.d/default.conf | cut -f1 -d' ')

  if [ "$OLDSUM" != "$NEWSUM" ]; then
    echo "change detected, reloading"
    nginx -s reload
  fi
done