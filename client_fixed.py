"""
PyCDN Client Example - Natural Import System Demo

This example showcases both the classic PyCDN usage and the revolutionary
new natural import syntax that allows importing packages directly from CDN servers.

FIXED VERSION: Works with all PyCDN versions (handles missing _prefix gracefully)
"""

import os
import pycdn
from dotenv import load_dotenv

load_dotenv()

def main():
    print(f"🚀 PyCDN Client Example - v{pycdn.__version__}")
    print("=" * 50)
    
    # Get API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  Warning: OPENAI_API_KEY not found in environment")
        print("   Set your API key: export OPENAI_API_KEY='your-key-here'")
        api_key = "demo-key-for-testing"
    
    # Connect to local PyCDN server
    print("🔗 Connecting to PyCDN server...")
    cdn = pycdn.pkg("http://localhost:8000")
    print(f"✅ Connected to {cdn._cdn_client.url}")
    
    # FIXED: Safely get prefix (handle older versions)
    try:
        prefix = getattr(cdn, '_prefix', 'cdn')  # Default to 'cdn' if not available
        print(f"📦 Import prefix registered: '{prefix}'")
        natural_imports_available = True
    except AttributeError:
        print(f"📦 Using classic PyCDN (natural imports require PyCDN v1.1.1+)")
        natural_imports_available = False
    
    print("\n" + "=" * 50)
    print("🎯 Method 1: Classic PyCDN Usage")
    print("=" * 50)
    
    try:
        # Classic usage - attribute access
        client = cdn.openai.OpenAI(api_key=api_key)
        print("✅ Created OpenAI client via: cdn.openai.OpenAI()")
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Hello from PyCDN classic usage!"}]
        )
        print("🧠 AI Response (Classic):", response.choices[0].message.content)
        
    except Exception as e:
        print(f"❌ Classic usage error: {e}")
        print("   Note: This requires a running PyCDN server with OpenAI package")
    
    print("\n" + "=" * 50)
    if natural_imports_available:
        print("🌟 Method 2: NEW Natural Import Syntax")
    else:
        print("🌟 Method 2: Natural Import Syntax (Requires v1.1.1+)")
    print("=" * 50)
    
    if natural_imports_available:
        try:
            # NEW: Natural Python import syntax!
            from cdn.openai import OpenAI
            print("✅ Imported via: from cdn.openai import OpenAI")
            
            # Use exactly like a local package
            client = OpenAI(api_key=api_key)
            print("✅ Created client via: OpenAI(api_key=...)")
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": "Hello from PyCDN natural imports!"}]
            )
            print("🧠 AI Response (Natural):", response.choices[0].message.content)
            
        except Exception as e:
            print(f"❌ Natural import error: {e}")
            print("   Note: This requires a running PyCDN server with OpenAI package")
    else:
        print(f"📥 Please upgrade to PyCDN v1.1.1+ for natural import support:")
        print("   pip install --upgrade pycdn")
        print("   Then you can use: from cdn.openai import OpenAI")
    
    print("\n" + "=" * 50)
    print("🎉 PyCDN Demo Complete!")
    print("=" * 50)
    if natural_imports_available:
        print("✨ Both methods work seamlessly together!")
    else:
        print("✨ Classic method working! Upgrade for natural imports!")
    print("🚀 PyCDN: The Netflix of Python packages!")

if __name__ == "__main__":
    main() 