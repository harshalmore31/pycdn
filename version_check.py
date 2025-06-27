#!/usr/bin/env python3
"""
PyCDN Version Checker

Quick script to check your PyCDN version and available features.
"""

import pycdn

def main():
    print("🔍 PyCDN Version Checker")
    print("=" * 40)
    
    try:
        version = pycdn.__version__
        print(f"📦 Installed Version: {version}")
        
        # Test connection capability
        try:
            cdn = pycdn.pkg("http://test:8000")
            print(f"✅ CDN Connection: Working")
            
            # Check for natural import system
            if hasattr(cdn, '_prefix'):
                prefix = cdn._prefix
                print(f"🔥 Natural Imports: Available (prefix: '{prefix}')")
                print("   Usage: from cdn.package import Class")
                
                # Check for advanced features
                if hasattr(pycdn, 'get_cdn_mappings'):
                    print("🌟 Multi-CDN Support: Available")
                    print("   Usage: pycdn.pkg('url', prefix='custom')")
                else:
                    print("🌟 Multi-CDN Support: Not Available")
                    
            else:
                print("🔥 Natural Imports: Not Available")
                print("   Upgrade: pip install --upgrade pycdn")
                
        except Exception as e:
            print(f"❌ CDN Connection Test: Failed ({e})")
            
        # Check for encryption features
        if hasattr(pycdn, 'enable_encryption'):
            print("🔐 Encryption: Available")
            print("   Usage: pycdn.enable_encryption()")
        else:
            print("🔐 Encryption: Not Available")
            
        print("\n" + "=" * 40)
        print("🚀 Feature Summary:")
        
        # Version-specific features
        if version >= "1.1.1":
            print("   ✅ Natural Import System")
            print("   ✅ Multi-CDN Support") 
            print("   ✅ Dynamic Prefix Management")
            print("   ✅ Advanced Proxy System")
            print("   ✅ Revolutionary UX")
        elif version >= "1.1.0":
            print("   ✅ Cloud Deployment Support")
            print("   ✅ Auto-Installation")
            print("   ❌ Natural Import System")
        elif version >= "1.0.9":
            print("   ✅ Dotenv Compatibility")
            print("   ✅ Environment Variables")
            print("   ❌ Natural Import System")
        else:
            print("   ✅ Basic CDN Functionality")
            print("   ❌ Many Advanced Features")
            
        print(f"\n💡 Latest Available: 1.1.7")
        if version < "1.1.7":
            print("🔄 Upgrade Command: pip install --upgrade pycdn")
            
    except ImportError:
        print("❌ PyCDN not installed")
        print("📥 Install Command: pip install pycdn")
    except Exception as e:
        print(f"❌ Error checking PyCDN: {e}")

if __name__ == "__main__":
    main() 