"""
Basic PyCDN Client Setup
========================

Simple client setup script for connecting to and using a PyCDN server.
This demonstrates the basic PyCDN client functionality.

Usage:
    # First start the server:
    python server_setup.py
    
    # Then in another terminal:
    python client_setup.py

Make sure the PyCDN server is running on http://localhost:8000
"""

import time
import pycdn

def test_server_connection():
    """Test if server is reachable."""
    print("🔍 Testing server connection...")
    try:
        client = pycdn.connect("http://localhost:8000", timeout=5)
        health = client.get_stats()
        client.close()
        print("✅ Server is running and accessible")
        return True
    except Exception as e:
        print(f"❌ Cannot connect to server: {e}")
        print("💡 Make sure to run 'python server_setup.py' first")
        return False

def demo_basic_usage():
    """Demonstrate basic PyCDN usage."""
    print("\n📦 Basic Package Usage Demo")
    print("-" * 40)
    
    try:
        # Method 1: Quick package access
        print("🎯 Method 1: Quick Package Access")
        cdn = pycdn.pkg("http://localhost:8000")
        
        # Math operations
        result1 = cdn.math.sqrt(25)
        print(f"  math.sqrt(25) = {result1}")
        
        result2 = cdn.math.factorial(5)
        print(f"  math.factorial(5) = {result2}")
        
        result3 = cdn.math.pow(2, 8)
        print(f"  math.pow(2, 8) = {result3}")
        
    except Exception as e:
        print(f"❌ Quick access failed: {e}")

def demo_client_configuration():
    """Demonstrate client with configuration."""
    print("\n⚙️  Client Configuration Demo")
    print("-" * 40)
    
    try:
        # Method 2: Full client setup
        client = pycdn.connect(
            url="http://localhost:8000",
            timeout=10,
            cache_size="50MB",
            max_retries=3,
            debug=True
        )
        
        # List available packages
        packages = client.list_packages()
        print(f"📋 Available packages: {packages}")
        
        # Get package info
        if "math" in packages:
            info = client.get_package_info("math")
            print(f"📄 Math package info: {info}")
        
        # Direct function calls
        print("\n🔢 Direct Function Calls:")
        result = client.call_function("json", "dumps", ({"test": "data"},))
        print(f"  json.dumps() = {result}")
        
        result = client.call_function("time", "time")
        print(f"  time.time() = {result}")
        
        result = client.call_function("random", "randint", (1, 100))
        print(f"  random.randint(1, 100) = {result}")
        
        # Get statistics
        stats = client.get_stats()
        print(f"\n📊 Client stats: {stats}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Client demo failed: {e}")

def demo_advanced_features():
    """Demonstrate advanced PyCDN features."""
    print("\n🚀 Advanced Features Demo")
    print("-" * 40)
    
    try:
        client = pycdn.connect("http://localhost:8000")
        
        # Cache management
        print("🗄️  Cache Management:")
        client.clear_cache()
        print("  Cache cleared")
        
        # Preload packages
        print("\n📥 Package Preloading:")
        client.preload_packages(["math", "json", "time"])
        print("  Packages preloaded")
        
        # Performance test
        print("\n⚡ Performance Test:")
        start_time = time.time()
        for i in range(10):
            result = client.call_function("math", "sqrt", (i + 1,))
        end_time = time.time()
        print(f"  10 function calls took {end_time - start_time:.3f} seconds")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Advanced demo failed: {e}")

def main():
    """Run client setup and demos."""
    print("🚀 PyCDN Client Setup & Demo")
    print("=" * 50)
    
    # Test server connection first
    if not test_server_connection():
        return
    
    # Run demos
    demo_basic_usage()
    demo_client_configuration()
    demo_advanced_features()
    
    print("\n🎉 Client demo completed!")
    print("\n💡 Try these next:")
    print("   • python examples/basic_usage.py")
    print("   • python examples/streaming_demo.py")
    print("   • Explore the /examples directory for more")

if __name__ == "__main__":
    main() 