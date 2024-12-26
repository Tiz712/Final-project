import { GraphReasoner } from './reasoners/GraphReasoner.js';
import { RuleReasoner } from './reasoners/RuleReasoner.js';

export class HybridReasoner {
  constructor() {
    this.graphReasoner = new GraphReasoner();
    this.ruleReasoner = new RuleReasoner();
  }

  async reason(graph) {
    const graphResults = await this.graphReasoner.analyze(graph);
    const ruleResults = await this.ruleReasoner.apply(graph);

    const reasoningPath = this.generateReasoningPath(graphResults, ruleResults);
    return this.validateReasoning(reasoningPath);
  }

  generateReasoningPath(graphResults, ruleResults) {
    return {
      steps: [...graphResults.steps, ...ruleResults.steps],
      conclusion: this.combineConcusions(graphResults.conclusion, ruleResults.conclusion)
    };
  }

  validateReasoning(path) {
    // 验证推理路径的正确性
    return {
      isValid: this.checkPathValidity(path),
      path: path,
      confidence: this.calculateConfidence(path)
    };
  }

  checkPathValidity(path) {
    return path.steps.every(step => this.isStepValid(step));
  }

  isStepValid(step) {
    return step.premises && 
           step.conclusion && 
           this.validateLogicalConnection(step.premises, step.conclusion);
  }

  validateLogicalConnection(premises, conclusion) {
    // 验证前提和结论之间的逻辑关系
    return true; // 简化版实现
  }

  calculateConfidence(path) {
    // 计算推理路径的置信度
    return path.steps.reduce((acc, step) => acc * step.confidence, 1);
  }
}