"""
PyCDN Server Example - Package CDN Server

This example creates a simple PyCDN server that serves packages via CDN
with support for both classic usage and natural import syntax.
"""

from pycdn.server import CDNServer

def main():
    print("🚀 PyCDN Server Example - v1.1.1")
    print("=" * 50)
    
    # Configure allowed packages for security
    allowed_packages = [
        "openai",      # AI/ML
        "requests",    # HTTP
        "numpy",       # Data science
        "pandas",      # Data analysis
        "math",        # Built-in math
        "json",        # JSON handling
        "datetime",    # Date/time
    ]
    
    print("📦 Creating PyCDN server...")
    print(f"🔒 Allowed packages: {', '.join(allowed_packages)}")
    
    # Create CDN server
    server = CDNServer(
        host="localhost",
        port=8000,
        debug=True,
        allowed_packages=allowed_packages
    )
    
    print("\n" + "=" * 50)
    print("🌟 Server Features Enabled:")
    print("=" * 50)
    print("✅ Classic usage: cdn.package.function()")
    print("✅ Natural imports: from cdn.package import Class")
    print("✅ Multi-CDN support with custom prefixes")
    print("✅ Secure sandboxed execution")
    print("✅ Intelligent caching and lazy loading")
    print("✅ Real-time error handling")
    
    print("\n" + "=" * 50)
    print("📡 Server Starting...")
    print("=" * 50)
    print("🌐 Server URL: http://localhost:8000")
    print("🔗 Health check: http://localhost:8000/health")
    print("📖 API docs: http://localhost:8000/docs")
    print("🛑 Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        # Start the server
        server.run()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Server error: {e}")
    finally:
        print("🏁 PyCDN Server shutdown complete")

if __name__ == "__main__":
    main() 