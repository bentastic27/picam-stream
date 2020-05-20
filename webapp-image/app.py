from kubernetes import client, config
from flask import Flask, render_template
from os import environ

if "INGRESS_HOST" not in environ:
    print("INGRESS_HOST isn't set, set to your desired IP/hostname of ingress node")
    print("example: https://example.com")
    exit()
else:
    ingress_host = environ.get("INGRESS_HOST")

app = Flask(__name__)

@app.route('/')
def index():

    config.load_incluster_config()
    v1 = client.CoreV1Api()

    pod_list = v1.list_namespaced_pod("picam", label_selector="app=picam")

    return render_template("index.html", pod_list=pod_list.items, ingress_host=ingress_host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)