#!/usr/bin/env python3
"""
VOIDTRACE AI — Crypto Liquidity Intelligence Engine
A blockchain intelligence software concept designed to organize and interpret
cross-chain market activity. Combines specialized AI agents with blockchain
data to analyze liquidity flows, stablecoin movements, capital rotation,
DEX activity, bridge activity, and ecosystem momentum.

https://voidtraceai.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def format_signal_type(signal_type: str) -> str:
    return " ".join(w.capitalize() for w in signal_type.split("-"))


def get_priority_signal(scores: dict) -> str:
    labels = {
        "liquidity_flow": "Liquidity Flow",
        "stablecoin_intel": "Stablecoin Intel",
        "capital_rotation": "Capital Rotation",
        "dex_activity": "DEX Activity",
        "bridge_activity": "Bridge Activity",
        "ecosystem_momentum": "Ecosystem Momentum",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_chain_intelligence(flow: int, stable: int, rotation: int, momentum: int) -> dict:
    return {
        "Ethereum": min(100, round(flow * 1.0)),
        "BNB Chain": min(100, round(stable * 1.0)),
        "Solana": min(100, round(rotation * 1.0)),
        "Arbitrum": min(100, round(momentum * 1.0)),
    }


def run_liquidity_intel(
    chain: str,
    signal_type: str = "liquidity-flow",
    liquidity_flow: int = 88,
    stablecoin_intel: int = 82,
    capital_rotation: int = 85,
    dex_activity: int = 78,
    bridge_activity: int = 90,
    ecosystem_momentum: int = 84,
) -> dict:
    """
    Run the VOIDTRACE AI Crypto Liquidity Intelligence Engine.

    Args:
        chain: Target blockchain network
        signal_type: Type of intelligence signal to analyze
        liquidity_flow: Cross-chain liquidity flow score (0-100)
        stablecoin_intel: Stablecoin intelligence score (0-100)
        capital_rotation: Capital rotation score (0-100)
        dex_activity: DEX activity score (0-100)
        bridge_activity: Bridge activity score (0-100)
        ecosystem_momentum: Ecosystem momentum score (0-100)

    Returns:
        dict with individual signal scores, overall intelligence index,
        and chain intelligence breakdown
    """
    scores = {
        "liquidity_flow": liquidity_flow,
        "stablecoin_intel": stablecoin_intel,
        "capital_rotation": capital_rotation,
        "dex_activity": dex_activity,
        "bridge_activity": bridge_activity,
        "ecosystem_momentum": ecosystem_momentum,
    }
    overall_intelligence_index = round(sum(scores.values()) / 6)

    return {
        "chain": chain,
        "signal_type": format_signal_type(signal_type),
        "liquidity_flow_score": liquidity_flow,
        "stablecoin_intel_score": stablecoin_intel,
        "capital_rotation_score": capital_rotation,
        "dex_activity_score": dex_activity,
        "bridge_activity_score": bridge_activity,
        "ecosystem_momentum_score": ecosystem_momentum,
        "overall_intelligence_index": overall_intelligence_index,
        "priority_signal": get_priority_signal(scores),
        "chain_intelligence": get_chain_intelligence(liquidity_flow, stablecoin_intel, capital_rotation, ecosystem_momentum),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    chain = args[0] if len(args) > 0 else "ethereum"
    signal_type = args[1] if len(args) > 1 else "liquidity-flow"
    liquidity_flow = int(args[2]) if len(args) > 2 else 88
    stablecoin_intel = int(args[3]) if len(args) > 3 else 82
    capital_rotation = int(args[4]) if len(args) > 4 else 85
    dex_activity = int(args[5]) if len(args) > 5 else 78
    bridge_activity = int(args[6]) if len(args) > 6 else 90
    ecosystem_momentum = int(args[7]) if len(args) > 7 else 84

    result = run_liquidity_intel(
        chain, signal_type, liquidity_flow, stablecoin_intel,
        capital_rotation, dex_activity, bridge_activity, ecosystem_momentum
    )

    print(f"Chain: {result['chain']}")
    print(f"Signal Type: {result['signal_type']}")
    print("=" * 45)
    print(f"Liquidity Flow Score:          {result['liquidity_flow_score']}/100  [{get_status(result['liquidity_flow_score'])}]")
    print(f"Stablecoin Intel Score:        {result['stablecoin_intel_score']}/100  [{get_status(result['stablecoin_intel_score'])}]")
    print(f"Capital Rotation Score:        {result['capital_rotation_score']}/100  [{get_status(result['capital_rotation_score'])}]")
    print(f"DEX Activity Score:            {result['dex_activity_score']}/100  [{get_status(result['dex_activity_score'])}]")
    print(f"Bridge Activity Score:         {result['bridge_activity_score']}/100  [{get_status(result['bridge_activity_score'])}]")
    print(f"Ecosystem Momentum Score:      {result['ecosystem_momentum_score']}/100  [{get_status(result['ecosystem_momentum_score'])}]")
    print("=" * 45)
    print(f"Overall Intelligence Index:    {result['overall_intelligence_index']}/100")
    print(f"Priority Signal:               {result['priority_signal']}")
    print("\nChain Intelligence:")
    for chain, score in result['chain_intelligence'].items():
        print(f"  {chain:<24} {score}/100")


if __name__ == "__main__":
    main()
