from pyswip import Prolog
import networkx as nx
import torch
from torch_geometric.nn import GATConv, GraphSAGE
from .prolog_manager import PrologManager

class GeometricReasoner:
    def __init__(self):
        self.prolog_manager = PrologManager()
        self.gnn_model = GeometricGNN()
        
    def initialize(self):
        """初始化推理系统"""
        if not self.prolog_manager.load_rules():
            raise RuntimeError("无法加载Prolog规则")
        if not self.prolog_manager.test_rules():
            raise RuntimeError("规则系统测试失败")
            
    def reason(self, graph: nx.MultiDiGraph):
        graph_results = self._graph_reasoning(graph)
        rule_results = self._rule_reasoning(graph)
        return self._combine_results(graph_results, rule_results)
        
    def _rule_reasoning(self, graph):
        """使用Prolog规则进行推理"""
        results = []
        for node in graph.nodes:
            # 构建查询
            query = f"point({node})"
            query_results = self.prolog_manager.query(query)
            if query_results:
                results.append({
                    "node": node,
                    "type": "point",
                    "inferences": query_results
                })
        return results

# GeometricGNN类保持不变