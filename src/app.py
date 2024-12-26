import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from geometric_reasoner import GeometricReasoner

class GeometricReasoningApp:
    def __init__(self):
        self.reasoner = GeometricReasoner()
        self.graph = nx.Graph()
        
    def run(self):
        st.title("Geometric Reasoning System")
        
        # Sidebar controls
        with st.sidebar:
            st.header("Controls")
            
            # Add point
            st.subheader("Add Point")
            x = st.number_input("X coordinate", value=0.0)
            y = st.number_input("Y coordinate", value=0.0)
            if st.button("Add Point"):
                self.add_point(x, y)
            
            # Add line
            st.subheader("Add Line")
            points = list(self.graph.nodes())
            if len(points) >= 2:
                p1 = st.selectbox("Point 1", points)
                p2 = st.selectbox("Point 2", points)
                if st.button("Add Line"):
                    self.add_line(p1, p2)
        
        # Main area
        col1, col2 = st.columns([2, 1])
        
        with col1:
            self.display_graph()
            
        with col2:
            st.subheader("Verification")
            if st.button("Verify Construction"):
                self.verify_construction()
    
    def add_point(self, x, y):
        point_name = f"P{len(self.graph.nodes()) + 1}"
        self.graph.add_node(point_name, pos=(x, y))
        st.success(f"Added point {point_name} at ({x}, {y})")
    
    def add_line(self, p1, p2):
        if p1 != p2:
            self.graph.add_edge(p1, p2)
            st.success(f"Added line between {p1} and {p2}")
    
    def display_graph(self):
        if not self.graph.nodes():
            st.info("Add points and lines to start constructing the geometric figure")
            return
            
        fig, ax = plt.subplots(figsize=(8, 8))
        pos = nx.get_node_attributes(self.graph, 'pos')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', 
                node_size=500, font_size=16, font_weight='bold')
        plt.close()
        st.pyplot(fig)
    
    def verify_construction(self):
        for node, data in self.graph.nodes(data=True):
            x, y = data['pos']
            if not self.reasoner.verify_point(x, y):
                st.error(f"Invalid point: {node}")
                return
                
        for p1, p2 in self.graph.edges():
            if not self.reasoner.verify_line(p1, p2):
                st.error(f"Invalid line: {p1}-{p2}")
                return
                
        st.success("Construction verified successfully")