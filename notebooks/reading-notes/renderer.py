def render_arrows_app_json(json_file: str):
    import json
    from pyvis.network import Network

    net = Network(notebook=True, directed=True)

    with open(json_file, 'r') as f:
        graph = json.load(f)
        nodes = graph["nodes"]
        links = graph["relationships"]

    node_map = {}
    for node in nodes:
        net.add_node(node["caption"])
        node_map[node["id"]] = node["caption"]

    for link in links:
        net.add_edge(node_map[link["fromId"]], node_map[link["toId"]], title=link["type"])

    return net
