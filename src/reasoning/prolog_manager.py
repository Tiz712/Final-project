from pyswip import Prolog
import os

class PrologManager:
    def __init__(self):
        self.prolog = Prolog()
        self.rules_loaded = False
        self.rules_dir = os.path.join(os.path.dirname(__file__), '..', 'rules')
        
    def load_rules(self):
        """加载所有规则文件"""
        try:
            rule_files = ['base_elements.pl', 'axioms.pl', 'relations.pl', 'derivation.pl']
            for file in rule_files:
                file_path = os.path.join(self.rules_dir, file)
                self.prolog.consult(file_path)
            self.rules_loaded = True
            return True
        except Exception as e:
            print(f"加载规则失败: {str(e)}")
            return False
            
    def test_rules(self):
        """测试规则系统是否正常工作"""
        if not self.rules_loaded:
            if not self.load_rules():
                return False
                
        try:
            # 测试基本图形定义
            test_queries = [
                "point(p1), coordinates(p1, 0, 0)",
                "line(l1), endpoints(l1, p1, p2)",
                "collinear(p1, p2, p3)"
            ]
            
            results = []
            for query in test_queries:
                result = list(self.prolog.query(query))
                results.append(len(result) >= 0)  # 检查是否可以执行查询
                
            return all(results)
            
        except Exception as e:
            print(f"测试规则失败: {str(e)}")
            return False
            
    def query(self, query_str):
        """执行Prolog查询"""
        if not self.rules_loaded:
            if not self.load_rules():
                return []
                
        try:
            return list(self.prolog.query(query_str))
        except Exception as e:
            print(f"查询失败: {str(e)}")
            return []