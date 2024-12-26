import unittest
from src.reasoning.prolog_manager import PrologManager

class TestPrologRules(unittest.TestCase):
    def setUp(self):
        self.prolog_manager = PrologManager()
        
    def test_rules_loading(self):
        """测试规则加载"""
        self.assertTrue(self.prolog_manager.load_rules())
        
    def test_basic_queries(self):
        """测试基本查询"""
        self.prolog_manager.load_rules()
        
        # 测试点的定义
        query = "point(p1), coordinates(p1, 0, 0)"
        result = self.prolog_manager.query(query)
        self.assertIsNotNone(result)
        
        # 测试线的定义
        query = "line(l1), endpoints(l1, p1, p2)"
        result = self.prolog_manager.query(query)
        self.assertIsNotNone(result)
        
    def test_geometric_axioms(self):
        """测试几何公理"""
        self.prolog_manager.load_rules()
        
        # 测试连接公理
        query = "axiom_connect(p1, p2, l1)"
        result = self.prolog_manager.query(query)
        self.assertIsNotNone(result)
        
if __name__ == '__main__':
    unittest.main()