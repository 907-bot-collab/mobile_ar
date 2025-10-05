#!/usr/bin/env python3
"""
Optimized QR Code Generator for AR Surgery Training System
=========================================================
* Lightweight QR generation with minimal dependencies
* Proper error handling and validation
* Configurable for different deployment environments
* Efficient image generation without heavy processing

Author: Optimized Version
Version: 8.0 - Efficient Architecture  
"""

import qrcode
import argparse
import sys
import os
from datetime import datetime

class OptimizedARQRGenerator:
    """Lightweight and efficient QR Code Generator"""

    def __init__(self):
        print("🚀 Optimized AR Surgery QR Generator v8.0")
        print("📱 Efficient QR code generation for mobile AR")

        # Repository-specific URLs
        self.urls = {
            'production': 'https://mobile-ar-phi.vercel.app',
            'staging': 'https://mobile-ar-git-main-907-bot-collab.vercel.app', 
            'local': 'http://localhost:3000',
            'custom': ''
        }

        self.dependencies_ok = self.check_dependencies()

    def check_dependencies(self):
        """Check if required dependencies are installed"""
        try:
            import qrcode
            print("✅ QR code library installed")
            return True
        except ImportError:
            print("❌ Missing qrcode library. Install with: pip install qrcode[pil]")
            return False

    def validate_url(self, url):
        """Basic URL validation"""
        if not url or not url.strip():
            return False
        return url.startswith(('http://', 'https://'))

    def create_simple_qr(self, url, filename='ar_qr.png'):
        """Create a simple, efficient QR code"""
        if not self.dependencies_ok:
            print("❌ Cannot generate QR code - missing dependencies")
            return None

        if not self.validate_url(url):
            print(f"❌ Invalid URL: {url}")
            return None

        try:
            print(f"🔲 Generating QR code for: {url}")

            # Create QR code with optimal settings
            qr = qrcode.QRCode(
                version=1,  # Automatically adjust size
                error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
                box_size=8,  # Reduced box size for efficiency
                border=4,
            )

            qr.add_data(url)
            qr.make(fit=True)

            # Create and save image
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filename)

            print(f"✅ QR code saved: {filename}")
            print(f"📏 Image size: {img.size}")

            return filename

        except Exception as e:
            print(f"❌ QR generation failed: {e}")
            return None

    def generate_for_deployment(self, deployment_type='production'):
        """Generate QR code for specific deployment"""

        if deployment_type not in self.urls:
            print(f"❌ Invalid deployment type: {deployment_type}")
            print(f"Available options: {list(self.urls.keys())}")
            return None

        url = self.urls[deployment_type]
        if not url:
            print(f"❌ No URL configured for {deployment_type}")
            return None

        filename = f'qr_{deployment_type}.png'
        result = self.create_simple_qr(url, filename)

        if result:
            print(f"\n🎯 SUCCESS: QR code for {deployment_type.upper()}")
            print(f"🔗 URL: {url}")
            print(f"📄 File: {result}")
            print("\n📱 Usage Instructions:")
            print("1. Open smartphone camera or Google Lens")
            print("2. Point at QR code")
            print("3. Tap the notification to open AR surgery training")

        return result

    def batch_generate(self):
        """Generate QR codes for all configured deployments"""
        print("🔄 Generating QR codes for all deployments...")
        results = {}

        for deploy_type, url in self.urls.items():
            if url and deploy_type != 'custom':
                print(f"\n--- {deploy_type.upper()} ---")
                result = self.generate_for_deployment(deploy_type)
                results[deploy_type] = result

        print("\n" + "="*50)
        print("📊 BATCH GENERATION SUMMARY")
        print("="*50)
        for deploy_type, result in results.items():
            status = "✅ SUCCESS" if result else "❌ FAILED"
            print(f"{deploy_type.upper()}: {status}")

        return results

def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(description='Generate QR codes for AR Surgery Training')
    parser.add_argument('--type', '-t', 
                       choices=['production', 'staging', 'local', 'batch'], 
                       default='production',
                       help='Deployment type or batch generation')
    parser.add_argument('--url', '-u', type=str, 
                       help='Custom URL (overrides default)')

    args = parser.parse_args()

    generator = OptimizedARQRGenerator()

    if not generator.dependencies_ok:
        print("\n🔧 SETUP REQUIRED:")
        print("pip install qrcode[pil]")
        sys.exit(1)

    if args.type == 'batch':
        generator.batch_generate()
    else:
        if args.url:
            # Custom URL mode
            generator.urls['custom'] = args.url
            result = generator.create_simple_qr(args.url, 'qr_custom.png')
        else:
            result = generator.generate_for_deployment(args.type)

        if result:
            print("\n🎓 Ready for medical education deployment!")
        else:
            print("\n❌ QR generation failed")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Interactive mode
        print("🏥 AR Surgery QR Generator - Interactive Mode")
        print("="*50)
        generator = OptimizedARQRGenerator()

        if not generator.dependencies_ok:
            print("\nInstall required dependencies and try again.")
            sys.exit(1)

        print("\nSelect generation mode:")
        print("1. Production deployment")
        print("2. Staging deployment") 
        print("3. Local development")
        print("4. Generate all")
        print("5. Custom URL")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '1':
            generator.generate_for_deployment('production')
        elif choice == '2':
            generator.generate_for_deployment('staging')
        elif choice == '3':
            generator.generate_for_deployment('local')
        elif choice == '4':
            generator.batch_generate()
        elif choice == '5':
            custom_url = input("Enter custom URL: ").strip()
            if generator.validate_url(custom_url):
                generator.create_simple_qr(custom_url, 'qr_custom.png')
            else:
                print("❌ Invalid URL format")
        else:
            print("❌ Invalid choice")
    else:
        main()
