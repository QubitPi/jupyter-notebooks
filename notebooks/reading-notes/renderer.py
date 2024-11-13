def render_arrows_app_json(json_file: str):
    import json
    from pyvis.network import Network

    net = Network(notebook=True, directed=True)

    with open(json_file, 'r') as f:
        graph = json.load(f)
        nodes = graph["nodes"]
        links = graph["relationships"]

    for node in nodes:
        net.add_node(node["id"], label=node["caption"])

    for link in links:
        net.add_edge(link["fromId"],link["toId"], title=link["type"])

    return net
