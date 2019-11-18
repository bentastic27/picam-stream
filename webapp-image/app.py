from kubernetes import client, config
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    config.load_incluster_config()
    v1 = client.CoreV1Api()

    pod_list = v1.list_namespaced_pod("picam", label_selector="app=picam")

    return render_template("index.html", pod_list=pod_list.items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)