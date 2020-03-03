#!/bin/bash

python3 /config-gen.py
motion -c /etc/motion/motion.conf &

while true; do
    sleep 60
    OLDLIST=$(find /etc/motion/conf.d -type f -name "*.conf" | sort)
    python3 /config-gen.py
    NEWLIST=$(find /etc/motion/conf.d -type f -name "*.conf" | sort)

    if [ "$OLDLIST" != "$NEWLIST" ]; then
        echo "change detected, reloading"
        kill -s SIGHUP $(cat /var/run/motion.pid)
    fi
done
