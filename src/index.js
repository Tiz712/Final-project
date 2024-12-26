import { MultimodalProcessor } from './core/MultimodalProcessor.js';
import { GraphBuilder } from './core/GraphBuilder.js';
import { HybridReasoner } from './reasoning/HybridReasoner.js';
import { AuxiliaryRecommender } from './auxiliary/AuxiliaryRecommender.js';
import { SystemEvaluator } from './evaluation/SystemEvaluator.js';

export class GeometricReasoningSystem {
  constructor() {
    this.multimodalProcessor = new MultimodalProcessor();
    this.graphBuilder = new GraphBuilder();
    this.reasoner = new HybridReasoner();
    this.recommender = new AuxiliaryRecommender();
    this.evaluator = new SystemEvaluator();
  }

  async solve(problem) {
    // 1. 多模态理解
    const formalRepresentation = await this.multimodalProcessor.process(problem);
    
    // 2. 构建图结构
    const graph = this.buildGraph(formalRepresentation);
    
    // 3. 混合推理
    let reasoningResult = await this.reasoner.reason(graph);
    
    // 4. 如果需要辅助量
    if (this.needsAuxiliary(reasoningResult)) {
      const auxiliary = await this.recommender.recommendAuxiliary(graph);
      const enhancedGraph = this.enhanceGraph(graph, auxiliary);
      reasoningResult = await this.reasoner.reason(enhancedGraph);
    }
    
    // 5. 系统评估
    const evaluation = await this.evaluator.evaluate({
      understanding: formalRepresentation,
      reasoning: reasoningResult,
      auxiliary: reasoningResult.auxiliary
    });
    
    return {
      proof: reasoningResult.path,
      confidence: reasoningResult.confidence,
      evaluation: evaluation
    };
  }

  buildGraph(representation) {
    const builder = this.graphBuilder;
    
    // 添加实体节点
    representation.entities.forEach(entity => {
      builder.addNode(entity.id, entity.properties);
    });
    
    // 添加关系边
    representation.relations.forEach(relation => {
      builder.addEdge(relation.from, relation.to, relation.type);
    });
    
    return builder.build();
  }

  needsAuxiliary(result) {
    return result.confidence < 0.8;
  }

  enhanceGraph(graph, auxiliary) {
    auxiliary.forEach(aux => {
      this.graphBuilder.addNode(aux.id, aux.properties);
      aux.relations.forEach(rel => {
        this.graphBuilder.addEdge(rel.from, rel.to, rel.type);
      });
    });
    return this.graphBuilder.build();
  }
}

// 使用示例
const system = new GeometricReasoningSystem();

const problem = {
  text: "在三角形ABC中，已知AB=AC，证明∠B=∠C。",
  image: null // 可选的几何图形图片
};

system.solve(problem)
  .then(result => {
    console.log('证明路径:', result.proof);
    console.log('置信度:', result.confidence);
    console.log('系统评估:', result.evaluation);
  })
  .catch(error => {
    console.error('求解出错:', error);
  });