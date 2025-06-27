#!/usr/bin/env python3
"""
Simple PyCDN Server Setup

Starts a basic PyCDN server on localhost:8000 for testing and development.
"""

import sys
import asyncio
from pycdn import CDNServer

def main():
    print("🚀 Starting PyCDN Server")
    print("=" * 30)
    
    # Create server with common packages allowed
    server = CDNServer(
        host="localhost",
        port=8000,
        debug=True,
        allowed_packages=None  # Allow all packages
    )
    
    print(f"🌐 Server starting at http://localhost:8000")
    print("📦 Allowed packages: All")
    print("🔧 Debug mode: Enabled")
    print("💡 Press Ctrl+C to stop")
    print("")
    
    try:
        # Run the server
        server.run()
    except KeyboardInterrupt:
        print("\n⏹️  Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 