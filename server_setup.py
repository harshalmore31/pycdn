"""
Basic PyCDN Server Setup
========================

Simple server setup script for running a PyCDN server locally.
This demonstrates how to start a server with common Python packages available.

Usage:
    python server_setup.py

The server will start on http://localhost:8000 with CORS enabled.
"""

import sys
import asyncio
from pycdn.server import CDNServer

def main():
    """Start basic PyCDN server with common packages."""
    print("🚀 Starting PyCDN Server...")
    print("=" * 50)
    
    # Common packages that are usually available
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
        "operator"
    ]
    
    # Create server instance
    server = CDNServer(
        host="localhost",
        port=8000,
        debug=True,
        allowed_packages=allowed_packages
    )
    
    print(f"📦 Allowed packages: {', '.join(allowed_packages)}")
    print(f"🌐 Server URL: http://localhost:8000")
    print(f"🔓 CORS enabled for all origins")
    print(f"📡 WebSocket streaming available")
    print(f"🔧 Debug mode: ON")
    print("\n⚡ Server starting...")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        # Start the server (no reload for direct app object)
        server.run()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 