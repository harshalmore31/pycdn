#!/usr/bin/env python3
"""
Basic PyCDN Server Example
==========================

This example shows how to start a basic PyCDN server with common Python packages.
Perfect for getting started with PyCDN server setup.

Usage:
    python examples/server/basic_server.py

Server will start on http://localhost:8000
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from pycdn.server import CDNServer

def main():
    """Start basic PyCDN server with common packages."""
    print("🚀 Basic PyCDN Server Example")
    print("=" * 40)
    
    # Common Python standard library packages
    allowed_packages = [
        "math",
        "os", 
        "sys",
        "json",
        "time",
        "datetime",
        "random",
        "string",
        "re",
        "collections",
        "itertools",
        "functools",
        "operator",
        "pathlib",
        "urllib",
        "base64",
        "hashlib",
        "uuid"
    ]
    
    print(f"📦 Configuring {len(allowed_packages)} packages:")
    for pkg in allowed_packages:
        print(f"   • {pkg}")
    
    print(f"\n🌐 Server Configuration:")
    print(f"   • Host: localhost")
    print(f"   • Port: 8000")
    print(f"   • Debug: ON")
    print(f"   • CORS: Enabled")
    print(f"   • WebSocket: Enabled")
    
    # Create server instance
    server = CDNServer(
        host="localhost",
        port=8000,
        debug=True,
        allowed_packages=allowed_packages
    )
    
    print(f"\n⚡ Starting server...")
    print(f"📡 Server URL: http://localhost:8000")
    print(f"🔧 Press Ctrl+C to stop\n")
    
    try:
        server.run()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 