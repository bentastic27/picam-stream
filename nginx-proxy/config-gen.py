#!/usr/bin/env python3

from jinja2 import Template
from kubernetes import client, config

template = """
server {
  listen 80;
  {% for pod in pod_list %}
  location /{{ pod.metadata.name }}/ {
    proxy_pass http://{{pod.status.pod_ip }}:8000/;
  }{% endfor %}
}

"""

config.load_incluster_config()
v1 = client.CoreV1Api()

try:
  pod_list = v1.list_namespaced_pod("picam", label_selector="app=picam").items
except:
  print("cannot get pod list")
  exit()

tm = Template(template)

if len(pod_list) > 0:
  tm = Template(template)
  config_file = open("/etc/nginx/conf.d/default.conf", "w")
  config_file.write(tm.render(pod_list=pod_list))
  config_file.close()

else:
  print("pod list less than 1, no changes made")