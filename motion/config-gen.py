#!/usr/bin/env python3

from os import listdir, remove
from jinja2 import Template
from kubernetes import client, config

template = """
netcam_url http://{{ pod.status.pod_ip }}:8000/
text_left {{ pod.metadata.name }}
movie_filename {{ pod.metadata.name }}-%Y%m%d%H%M
on_movie_end "gzip %f"
"""

config.load_incluster_config()
v1 = client.CoreV1Api()

try:
  pod_list = v1.list_namespaced_pod("picam", label_selector="app=picam").items
except:
  print("cannot get pod list")
  exit()

if len(pod_list) > 0:
  for config_file in listdir("/etc/motion/conf.d/"):
    remove("/etc/motion/conf.d/" + config_file)

  tm = Template(template)
  for pod in pod_list:
    config_file = open("/etc/motion/conf.d/" + pod.metadata.name + ".conf" , "w")
    config_file.write(tm.render(pod=pod))
    config_file.close()

else:
  print("pod list less than 1, no changes made")