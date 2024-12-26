import networkx as nx

class GraphBuilder:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        
    def add_node(self, node_id: str, properties: dict) -> 'GraphBuilder':
        if node_id not in self.graph:
            self.graph.add_node(node_id, **properties)
        return self
        
    def add_edge(self, from_id: str, to_id: str, relation: str) -> 'GraphBuilder':
        if from_id in self.graph and to_id in self.graph:
            self.graph.add_edge(from_id, to_id, relation=relation)
        return self
        
    def validate(self) -> bool:
        return all(self._validate_node(node) for node in self.graph.nodes)
        
    def _validate_node(self, node) -> bool:
        return isinstance(self.graph.nodes[node], dict)
        
    def build(self) -> nx.MultiDiGraph:
        if not self.validate():
            raise ValueError("Invalid graph structure")
        return self.graph