#!/bin/bash

python3 /config-gen.py

motion -c /etc/motion/motion.config

### TODO enable auto reloading per 
# http://lavrsen.dk/foswiki/bin/view/Motion/MotionGuideGettingItRunning#Signals_40sent_with_e.g._kill_command_41