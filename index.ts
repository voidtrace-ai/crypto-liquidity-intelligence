#!/usr/bin/env node

interface LiquidityIntelInput {
  chain: string;
  signalType: string;
  liquidityFlow: number;
  stablecoinIntel: number;
  capitalRotation: number;
  dexActivity: number;
  bridgeActivity: number;
  ecosystemMomentum: number;
}

interface LiquidityIntelOutput {
  chain: string;
  signalType: string;
  liquidityFlowScore: number;
  stablecoinIntelScore: number;
  capitalRotationScore: number;
  dexActivityScore: number;
  bridgeActivityScore: number;
  ecosystemMomentumScore: number;
  overallIntelligenceIndex: number;
  prioritySignal: string;
  chainIntelligence: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function formatSignalType(signalType: string): string {
  return signalType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
}

function getPrioritySignal(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    liquidityFlow: "Liquidity Flow",
    stablecoinIntel: "Stablecoin Intel",
    capitalRotation: "Capital Rotation",
    dexActivity: "DEX Activity",
    bridgeActivity: "Bridge Activity",
    ecosystemMomentum: "Ecosystem Momentum",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getChainIntelligence(flow: number, stable: number, rotation: number, momentum: number): Record<string, number> {
  return {
    "Ethereum": Math.min(100, Math.round(flow * 1.0)),
    "BNB Chain": Math.min(100, Math.round(stable * 1.0)),
    "Solana": Math.min(100, Math.round(rotation * 1.0)),
    "Arbitrum": Math.min(100, Math.round(momentum * 1.0)),
  };
}

export function runLiquidityIntel(input: LiquidityIntelInput): LiquidityIntelOutput {
  const scores = {
    liquidityFlow: input.liquidityFlow,
    stablecoinIntel: input.stablecoinIntel,
    capitalRotation: input.capitalRotation,
    dexActivity: input.dexActivity,
    bridgeActivity: input.bridgeActivity,
    ecosystemMomentum: input.ecosystemMomentum,
  };
  const overallIntelligenceIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    chain: input.chain,
    signalType: formatSignalType(input.signalType),
    liquidityFlowScore: input.liquidityFlow,
    stablecoinIntelScore: input.stablecoinIntel,
    capitalRotationScore: input.capitalRotation,
    dexActivityScore: input.dexActivity,
    bridgeActivityScore: input.bridgeActivity,
    ecosystemMomentumScore: input.ecosystemMomentum,
    overallIntelligenceIndex,
    prioritySignal: getPrioritySignal(scores),
    chainIntelligence: getChainIntelligence(input.liquidityFlow, input.stablecoinIntel, input.capitalRotation, input.ecosystemMomentum),
  };
}

const args = process.argv.slice(2);
const chain = args[0] || "ethereum";
const signalType = args[1] || "liquidity-flow";
const liquidityFlow = parseInt(args[2]) || 88;
const stablecoinIntel = parseInt(args[3]) || 82;
const capitalRotation = parseInt(args[4]) || 85;
const dexActivity = parseInt(args[5]) || 78;
const bridgeActivity = parseInt(args[6]) || 90;
const ecosystemMomentum = parseInt(args[7]) || 84;

const result = runLiquidityIntel({
  chain, signalType, liquidityFlow, stablecoinIntel,
  capitalRotation, dexActivity, bridgeActivity, ecosystemMomentum,
});

console.log(`Chain: ${result.chain}`);
console.log(`Signal Type: ${result.signalType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Liquidity Flow Score:          ${result.liquidityFlowScore}/100  [${getStatus(result.liquidityFlowScore)}]`);
console.log(`Stablecoin Intel Score:        ${result.stablecoinIntelScore}/100  [${getStatus(result.stablecoinIntelScore)}]`);
console.log(`Capital Rotation Score:        ${result.capitalRotationScore}/100  [${getStatus(result.capitalRotationScore)}]`);
console.log(`DEX Activity Score:            ${result.dexActivityScore}/100  [${getStatus(result.dexActivityScore)}]`);
console.log(`Bridge Activity Score:         ${result.bridgeActivityScore}/100  [${getStatus(result.bridgeActivityScore)}]`);
console.log(`Ecosystem Momentum Score:      ${result.ecosystemMomentumScore}/100  [${getStatus(result.ecosystemMomentumScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Intelligence Index:    ${result.overallIntelligenceIndex}/100`);
console.log(`Priority Signal:               ${result.prioritySignal}`);
console.log("\nChain Intelligence:");
Object.entries(result.chainIntelligence).forEach(([chain, score]) => {
  console.log(`  ${chain.padEnd(22)} ${score}/100`);
});
