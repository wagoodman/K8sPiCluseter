#!/usr/bin/env python
import time
import sys
import os

num_nodes = int(sys.argv[1])

for idx in range(num_nodes):
  os.system("""flash \
  --device /dev/mmcblk0 \
  --hostname pinode%(idx)s \
  --userdata ./user-data.yaml \
  https://github.com/hypriot/image-builder-rpi/releases/download/v1.7.1/hypriotos-rpi-v1.7.1.img.zip
  """  % {'idx': idx})

  raw_input("Press Enter to continue...")

while True:
  os.system('clear ; date; avahi-browse -at | egrep -e pinode -e pearl; echo ; nmap -sP 192.168.86.0/24 | egrep -e pinode -e pearl')
  time.sleep(1)