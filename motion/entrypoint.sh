#!/bin/bash

python3 /config-gen.py
motion -c /etc/motion/motion.conf &

while true; do
    sleep 60
    OLDSUM=$(find /etc/motion/conf.d -type f -exec md5sum {} \; | sort -k 2 | md5sum | cut -f1 -d' ')
    python3 /config-gen.py
    NEWSUM=$(find /etc/motion/conf.d -type f -exec md5sum {} \; | sort -k 2 | md5sum | cut -f1 -d' ')

    if [ "$OLDSUM" != "$NEWSUM" ]; then
        echo "change detected, reloading"
        kill -s SIGHUP $(cat /var/run/motion/motion.pid)
    fi
done
