from pyswip import Prolog
import os
import networkx as nx
import matplotlib.pyplot as plt

class GeometricReasoner:
    def __init__(self):
        self.prolog = Prolog()
        self.rules_path = os.path.join(os.path.dirname(__file__), 'prolog_rules/geometry_rules.pl')
        self.load_rules()
        
    def load_rules(self):
        """Load Prolog rules from file"""
        try:
            self.prolog.consult(self.rules_path)
            print("Rules loaded successfully")
        except Exception as e:
            print(f"Failed to load rules: {str(e)}")
            
    def query(self, query_str):
        """Execute a Prolog query"""
        try:
            return list(self.prolog.query(query_str))
        except Exception as e:
            print(f"Query failed: {str(e)}")
            return []
            
    def verify_point(self, x, y):
        """Verify if a point exists at given coordinates"""
        query = f"point(P), coordinates(P, {x}, {y})"
        return bool(self.query(query))
        
    def verify_line(self, p1, p2):
        """Verify if a line exists between two points"""
        query = f"line(L), endpoints(L, {p1}, {p2})"
        return bool(self.query(query))