#!/usr/bin/env python3

from jinja2 import Template
from kubernetes import client, config

template = """
netcam_url http://{{ pod.status.pod_ip }}:8000/
text_left {{ pod.metadata.name }}

"""

config.load_incluster_config()
v1 = client.CoreV1Api()

pod_list = v1.list_namespaced_pod("picam", label_selector="app=picam").items
tm = Template(template)

for pod in pod_list:
  config_file = open("/etc/motion/conf.d/" + pod.metadata.name + ".conf" , "w")
  config_file.write(tm.render(pod=pod))
  config_file.close()