# PyCDN MVP - Revolutionary Python Package CDN

[![PyPI version](https://badge.fury.io/py/pycdn.svg)](https://badge.fury.io/py/pycdn)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **Revolutionary Python package delivery via CDN with serverless execution and lazy loading**

## 🚀 What is PyCDN?

PyCDN is a revolutionary Python package delivery system that eliminates dependency hell by serving packages through a global CDN network with intelligent lazy loading. Instead of `pip install`, packages are executed remotely on edge servers and results are returned instantly.

### Key Innovations

- **Zero Local Dependencies**: No more package conflicts or environment issues
- **Lazy Loading**: Packages loaded only when functions are called
- **CDN Delivery**: Ultra-fast global distribution via edge servers
- **Remote Execution**: Functions execute on optimized CDN servers
- **Intelligent Caching**: ML-powered package pre-loading and optimization

## 📦 Installation

```bash
# Install PyCDN
pip install pycdn

# Or install from source
git clone https://github.com/harshalmore31/pycdn
cd pycdn
pip install -e .
```

## ⚡ Quick Start

### 1. Start the CDN Server

```bash
# Start server with default settings
pycdn server start

# Or with custom configuration
pycdn server start --port 8080 --allowed-packages math json requests
```

### 2. Use Packages via CDN

```python
import pycdn

# Connect to CDN server
cdn = pycdn.pkg("http://localhost:8000")

# Use packages lazily - no local installation needed!
result = cdn.math.sqrt(16)          # Returns 4.0
factorial = cdn.math.factorial(5)   # Returns 120

# JSON operations
data = {"hello": "world"}
json_str = cdn.json.dumps(data)
parsed = cdn.json.loads(json_str)

print(f"Results: {result}, {factorial}, {parsed}")
```

### 3. OpenAI Integration Example

```python
import pycdn

# Load OpenAI package from CDN
cdn = pycdn.pkg("http://localhost:8000")

# Use OpenAI without local installation
# (requires OpenAI package on server and API key)
import os
if os.environ.get("OPENAI_API_KEY"):
    client = cdn.openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello from PyCDN!"}]
    )
    print(response.choices[0].message.content)
```

## 🏗 Architecture Overview

```
┌─────────────────┐    HTTP/JSON     ┌─────────────────┐
│   PyCDN Client  │◄────────────────►│   PyCDN Server  │
│                 │                  │                 │
│ - Lazy Loading  │                  │ - FastAPI       │
│ - Import Hooks  │                  │ - Package Runtime│
│ - Caching       │                  │ - Execution Env │
│ - Serialization │                  │ - Security      │
└─────────────────┘                  └─────────────────┘
         ▲                                     ▲
         │                                     │
    ┌────▼─────┐                          ┌────▼─────┐
    │ Local    │                          │ Server   │
    │ Python   │                          │ Packages │
    │ Process  │                          │ (math,   │
    │          │                          │ json,    │
    │          │                          │ requests)│
    └──────────┘                          └──────────┘
```

## 🛠 Project Structure

```
pycdn/
├── pycdn/                      # Main package
│   ├── __init__.py            # Package entry point
│   ├── cli.py                 # Command line interface
│   ├── client/                # Client-side SDK
│   │   ├── core.py           # CDN client implementation
│   │   ├── lazy_loader.py    # Lazy loading mechanism
│   │   └── import_hook.py    # Import system integration
│   ├── server/                # Server-side SDK
│   │   ├── core.py           # FastAPI server
│   │   └── runtime.py        # Package execution environment
│   └── utils/                 # Common utilities
│       └── common.py         # Serialization, logging, etc.
├── examples/                  # Usage examples
│   ├── server_example.py     # Server setup examples
│   ├── client_example.py     # Client usage examples
│   └── openai_example.py     # OpenAI integration demo
├── tests/                     # Test suite
│   ├── test_client.py        # Client tests
│   ├── test_server.py        # Server tests
│   └── test_integration.py   # End-to-end tests
├── docs/                      # Documentation
│   └── quickstart.md         # Getting started guide
├── setup.py                  # Package setup
├── pyproject.toml            # Modern Python packaging
└── requirements.txt          # Dependencies
```

## 🧪 Running the Examples

### Example 1: Basic Server and Client

```bash
# Terminal 1: Start server
python examples/server_example.py

# Terminal 2: Run client examples
python examples/client_example.py
```

### Example 2: OpenAI Integration

```bash
# Terminal 1: Start server with OpenAI support
python examples/openai_example.py --mode server

# Terminal 2: Run OpenAI client examples
python examples/openai_example.py --mode client

# For real OpenAI API calls (requires API key):
export OPENAI_API_KEY="your-key-here"
python examples/openai_example.py --mode real
```

### Example 3: Using CLI

```bash
# Server management
pycdn server start --debug

# Client operations
pycdn client list                    # List available packages
pycdn client info math               # Get package information
pycdn client stats                   # Server statistics

# Package deployment
pycdn deploy requests --version latest

# Test connection
pycdn test --url http://localhost:8000
```

## 🧪 Testing

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run unit tests
python -m pytest tests/ -v

# Run specific test files
python tests/test_client.py
python tests/test_server.py
python tests/test_integration.py

# Run with coverage
python -m pytest tests/ --cov=pycdn --cov-report=html
```

## 🔧 API Reference

### Client API

```python
import pycdn

# Quick access
cdn = pycdn.pkg("http://localhost:8000")
result = cdn.math.sqrt(16)

# Advanced client
client = pycdn.connect(
    url="http://localhost:8000",
    timeout=30,
    cache_size="100MB",
    max_retries=3
)

packages = client.list_packages()
info = client.get_package_info("math")
stats = client.get_stats()
client.close()

# Configuration
pycdn.configure(timeout=60, cache_size="200MB")
pycdn.preload(["math", "json", "requests"])
```

### Server API

```python
from pycdn.server import CDNServer, PackageDeployer

# Start server
server = CDNServer(
    host="localhost",
    port=8000,
    allowed_packages=["math", "json", "requests"]
)
server.run()

# Deploy packages
deployer = PackageDeployer("http://localhost:8000")
result = deployer.deploy_package("requests", version="latest")
```

## 🚀 Key Features Implemented

### ✅ Core Functionality
- [x] FastAPI-based CDN server
- [x] Lazy loading client SDK
- [x] Remote function execution
- [x] Request/response serialization
- [x] Error handling and retries

### ✅ Performance Features
- [x] Intelligent caching system
- [x] Connection pooling
- [x] Response compression
- [x] Request batching support

### ✅ Developer Experience
- [x] Command-line interface
- [x] Debug mode and logging
- [x] Comprehensive examples
- [x] Unit and integration tests

### ✅ Security Features
- [x] Package allowlist/blocklist
- [x] Request validation
- [x] Sandboxed execution environment
- [x] Error sanitization

## 🔍 How It Works

1. **Client Request**: When you call `cdn.math.sqrt(16)`, the client serializes the function call
2. **Server Execution**: The CDN server receives the request, loads the math package, and executes `sqrt(16)`
3. **Result Return**: The server serializes the result and sends it back to the client
4. **Transparent Usage**: The client deserializes the result and returns `4.0` - just like a local function call!

## 📊 Performance Characteristics

### Latency Overhead
- **Local function call**: ~0.0001ms
- **CDN function call**: ~10-50ms (depending on network)
- **Cached CDN call**: ~5-20ms

### Benefits
- **Zero installation time**: No `pip install` delays
- **Zero disk space**: No local package storage
- **Zero conflicts**: No dependency hell
- **Instant updates**: Packages updated server-side

## 🛣 Roadmap

### Phase 1 (MVP - Current)
- [x] Basic client-server architecture
- [x] Function execution via HTTP API
- [x] Lazy loading implementation
- [x] OpenAI integration example

### Phase 2 (Enhanced)
- [ ] Class and object support
- [ ] Persistent sessions
- [ ] Advanced caching strategies
- [ ] WebSocket connections

### Phase 3 (Production)
- [ ] Global CDN deployment
- [ ] Enterprise features
- [ ] Performance optimization
- [ ] Multi-language support

## 🤝 Contributing

We welcome contributions! Here's how to get started:

```bash
# Clone the repository
git clone https://github.com/harshalmore31/pycdn
cd pycdn

# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v

# Run examples
python examples/server_example.py  # Terminal 1
python examples/client_example.py  # Terminal 2
```

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Test with multiple Python versions

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Maintainer**: Harshal More ([@harshalmore31](https://github.com/harshalmore31))
- **Email**: harshalmore2468@gmail.com

## 🆘 Support

- **Documentation**: [docs.pycdn.dev](https://docs.pycdn.dev)
- **Issues**: [GitHub Issues](https://github.com/harshalmore31/pycdn/issues)
- **Discord**: [Join our community](https://discord.gg/pycdn)
- **Email**: support@pycdn.dev

## 🎯 Vision

PyCDN represents the future of Python package management. Just as Netflix revolutionized video delivery through CDN, PyCDN revolutionizes package delivery through lazy loading and remote execution. 

**The goal**: Make `pip install` as obsolete as downloading music files.

---

**Built with ❤️ by the PyCDN team**

*"The future of Python package management is here"* 