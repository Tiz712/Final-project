import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from src.core.graph_builder import GraphBuilder
from src.reasoning.geometric_reasoner import GeometricReasoner

class GeometricReasoningApp:
    def __init__(self):
        self.graph_builder = GraphBuilder()
        self.reasoner = GeometricReasoner()
        
    def run(self):
        st.title("几何推理系统")
        
        # 侧边栏控制面板
        with st.sidebar:
            st.header("控制面板")
            
            # 添加节点
            st.subheader("添加节点")
            node_name = st.text_input("节点名称")
            node_type = st.selectbox("节点类型", ["点", "线", "角", "圆"])
            if st.button("添加节点"):
                self.add_node(node_name, {"type": node_type})
            
            # 添加边
            st.subheader("添加关系")
            from_node = st.selectbox("起始节点", self.get_nodes())
            to_node = st.selectbox("终止节点", self.get_nodes())
            relation = st.selectbox("关系类型", ["平行", "垂直", "相等"])
            if st.button("添加关系"):
                self.add_edge(from_node, to_node, relation)
        
        # 主界面
        col1, col2 = st.columns([2, 1])
        
        with col1:
            self.display_graph()
            
        with col2:
            if st.button("开始推理"):
                self.run_reasoning()
    
    def add_node(self, name, properties):
        self.graph_builder.add_node(name, properties)
        st.success(f"添加节点: {name}")
    
    def add_edge(self, from_node, to_node, relation):
        self.graph_builder.add_edge(from_node, to_node, relation)
        st.success(f"添加关系: {from_node} -> {to_node}")
    
    def get_nodes(self):
        return list(self.graph_builder.graph.nodes())
    
    def display_graph(self):
        fig, ax = plt.subplots(figsize=(10, 8))
        pos = nx.spring_layout(self.graph_builder.graph)
        nx.draw(self.graph_builder.graph, pos, with_labels=True, 
                node_color='lightblue', node_size=500, ax=ax)
        plt.close()
        st.pyplot(fig)
    
    def run_reasoning(self):
        graph = self.graph_builder.build()
        result = self.reasoner.reason(graph)
        
        st.subheader("推理结果")
        st.json(result)

if __name__ == "__main__":
    app = GeometricReasoningApp()
    app.run()