import os
import json
from pyvis.network import Network

def render_arrows_app_json(json_file: str):

    net = Network(notebook=True, directed=True)

    with open(json_file, 'r') as f:
        graph = json.load(f)
        nodes = graph["nodes"]
        links = graph["relationships"]

    for node in nodes:
        net.add_node(node["id"], label=node["caption"])

    for link in links:
        net.add_edge(link["fromId"],link["toId"], label=link["type"])

    return net
