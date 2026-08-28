from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="crypto-liquidity-intelligence",
    version="1.0.0",
    author="VOIDTRACE AI",
    author_email="info@voidtraceai.com",
    description="VOIDTRACE AI Crypto Liquidity Intelligence Engine — blockchain intelligence for cross-chain liquidity flows, stablecoin movements, capital rotation, and DEX activity.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://voidtraceai.com",
    project_urls={
        "Homepage": "https://voidtraceai.com",
        "GitHub": "https://github.com/voidtrace-ai/crypto-liquidity-intelligence",
        "Documentation": "https://crypto-liquidity-intelligence.readthedocs.io",
        "PyPI": "https://pypi.org/project/crypto-liquidity-intelligence",
    },
    py_modules=["crypto_liquidity_intel"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "crypto-liquidity-intelligence",
        "blockchain-analytics",
        "cross-chain-intelligence",
        "defi-analytics",
        "on-chain-signals",
        "stablecoin-intelligence",
        "dex-activity",
        "bridge-analytics",
        "voidtrace-ai",
    ],
    entry_points={
        "console_scripts": [
            "voidtrace-intel=crypto_liquidity_intel:main",
        ],
    },
)
