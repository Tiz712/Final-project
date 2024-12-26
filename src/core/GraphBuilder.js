export class GraphBuilder {
  constructor() {
    this.graph = new Map();
  }

  addNode(id, properties) {
    if (!this.graph.has(id)) {
      this.graph.set(id, {
        properties,
        edges: new Map()
      });
    }
    return this;
  }

  addEdge(fromId, toId, relation) {
    if (this.graph.has(fromId) && this.graph.has(toId)) {
      this.graph.get(fromId).edges.set(toId, relation);
    }
    return this;
  }

  validate() {
    // 验证图结构的完整性和正确性
    for (const [nodeId, node] of this.graph) {
      if (!this.validateNode(nodeId, node)) {
        return false;
      }
    }
    return true;
  }

  validateNode(nodeId, node) {
    // 验证节点的属性和关系是否有效
    return node.properties && 
           typeof node.properties === 'object' &&
           node.edges instanceof Map;
  }

  build() {
    if (!this.validate()) {
      throw new Error('Invalid graph structure');
    }
    return this.graph;
  }
}