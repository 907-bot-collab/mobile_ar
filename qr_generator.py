#!/usr/bin/env python3
"""
QR Code Generator for AR Surgery Training System
===============================================
* Generates QR codes that link to hosted HTML interface
* Supports both development and production URLs
* Creates enhanced QR displays with instructions
* Optimized for mobile scanning (Google Lens compatible)

Author: AI-AR Medical Systems
Version: 7.0 - Separated Architecture
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import qrcode
import argparse
from datetime import datetime
import os

class ARSurgeryQRGenerator:
    """Simplified QR Code Generator for hosted AR Surgery interface"""

    def __init__(self):
        print("🚀 AR Surgery QR Generator v7.0")
        print("📱 Generate QR codes for hosted AR surgery training")

        # Default URLs (can be customized)
        self.urls = {
            'local': 'http://localhost:3000',
            'vercel': 'https://your-app-name.vercel.app',
            'custom': ''
        }

    def create_qr_code(self, url, filename='ar_surgery_qr.png'):
        """Create high-quality QR code for mobile access"""
        try:
            print(f"🔲 Generating QR code for: {url}")

            # Create QR code with high error correction
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )

            qr.add_data(url)
            qr.make(fit=True)

            # Create QR code image
            qr_img = qr.make_image(fill_color="black", back_color="white")

            # Convert to numpy array for enhanced display
            qr_array = np.array(qr_img)

            # Create enhanced display
            enhanced_qr = self.create_enhanced_qr_display(qr_array, url)

            # Save both versions
            qr_img.save(filename)
            cv2.imwrite(f"enhanced_{filename}", enhanced_qr)

            print(f"✅ QR codes saved: {filename} & enhanced_{filename}")
            return enhanced_qr, filename

        except Exception as e:
            print(f"❌ QR code generation error: {e}")
            return None, None

    def create_enhanced_qr_display(self, qr_array, url):
        """Create enhanced QR code display with instructions and branding"""
        try:
            # Create larger canvas
            canvas_height = 900
            canvas_width = 700
            canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8) * 255

            # Resize QR code
            qr_size = 350
            qr_resized = cv2.resize((qr_array * 255).astype(np.uint8), (qr_size, qr_size))
            qr_bgr = cv2.cvtColor(qr_resized, cv2.COLOR_GRAY2BGR)

            # Center QR code
            qr_y = 180
            qr_x = (canvas_width - qr_size) // 2
            canvas[qr_y:qr_y + qr_size, qr_x:qr_x + qr_size] = qr_bgr

            # Add title and branding
            cv2.putText(canvas, "AR SURGERY TRAINING", (130, 80),
                       cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 0), 3)
            cv2.putText(canvas, "QR CODE ACCESS", (200, 120),
                       cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 100, 200), 2)
            cv2.putText(canvas, "Scan with Google Lens or Camera", (150, 150),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 100), 2)

            # Add URL info
            url_display = url[:50] + "..." if len(url) > 50 else url
            cv2.putText(canvas, f"URL: {url_display}", (50, 560),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 150), 1)

            # Add mobile instructions
            instructions = [
                "📱 MOBILE ACCESS INSTRUCTIONS:",
                "",
                "1. Open your phone camera or Google Lens",
                "2. Point camera at this QR code",
                "3. Tap the notification/link that appears",
                "4. Click 'START SURGERY' button",
                "5. Experience immersive AR surgery training!",
                "",
                "🏥 FEATURES INCLUDED:",
                "",
                "• Real-time surgery step progression",
                "• Patient vitals monitoring simulation", 
                "• Surgical instrument identification",
                "• Critical safety alerts and warnings",
                "• Educational learning objectives",
                "• Mobile-optimized AR interface",
                "",
                "🎓 Perfect for medical students & residents",
                "⚡ No app installation required",
                "🌐 Works on all smartphones"
            ]

            y_start = 600
            line_height = 22
            for i, instruction in enumerate(instructions):
                if instruction == "":
                    continue

                font_scale = 0.65 if instruction.startswith(('📱', '🏥')) else 0.45
                color = (0, 0, 150) if instruction.startswith(('📱', '🏥')) else (50, 50, 50)
                thickness = 2 if instruction.startswith(('📱', '🏥')) else 1

                if instruction.startswith(('🎓', '⚡', '🌐')):
                    color = (0, 150, 0)
                    font_scale = 0.5
                    thickness = 2

                y_pos = y_start + (i * line_height)
                if y_pos < canvas_height - 20:  # Prevent overflow
                    cv2.putText(canvas, instruction, (30, y_pos),
                               cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

            # Add decorative border
            cv2.rectangle(canvas, (15, 15), (canvas_width-15, canvas_height-15), (0, 0, 0), 3)

            # Add QR code border with color
            cv2.rectangle(canvas, (qr_x-15, qr_y-15), (qr_x+qr_size+15, qr_y+qr_size+15), (0, 100, 200), 4)

            # Add timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(canvas, f"Generated: {timestamp}", (30, canvas_height-30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (100, 100, 100), 1)

            return canvas

        except Exception as e:
            print(f"❌ Enhanced display creation error: {e}")
            return None

    def display_qr_code(self, qr_display, url):
        """Display the QR code using matplotlib"""
        if qr_display is None:
            print("❌ No QR code to display")
            return

        try:
            plt.figure(figsize=(12, 15))
            plt.imshow(cv2.cvtColor(qr_display, cv2.COLOR_BGR2RGB))
            plt.title(f"📱 QR Code for AR Surgery Training\nURL: {url}", fontsize=14, pad=20)
            plt.axis('off')

            plt.figtext(0.5, 0.02, "Scan with any smartphone camera or Google Lens", 
                       ha='center', fontsize=12, style='italic', weight='bold')

            plt.tight_layout()
            plt.show()

            print("\n" + "="*80)
            print("🎯 QR CODE GENERATED SUCCESSFULLY!")
            print("="*80)
            print(f"🔗 Target URL: {url}")
            print("📱 Compatible with all smartphone cameras")
            print("🏥 Perfect for medical education deployment")
            print("⚡ No app installation required")
            print("="*80)

        except Exception as e:
            print(f"❌ Display error: {e}")

    def generate_for_deployment(self, deployment_type='vercel', custom_url=None):
        """Generate QR code for different deployment scenarios"""
        print(f"🚀 Generating QR code for {deployment_type} deployment")

        if deployment_type == 'local':
            url = self.urls['local']
            filename = 'qr_local.png'
        elif deployment_type == 'vercel':
            url = self.urls['vercel']
            filename = 'qr_vercel.png'
        elif deployment_type == 'custom' and custom_url:
            url = custom_url
            filename = 'qr_custom.png'
        else:
            print("❌ Invalid deployment type or missing custom URL")
            return None

        # Generate QR code
        qr_display, qr_filename = self.create_qr_code(url, filename)

        if qr_display is not None:
            # Display the result
            self.display_qr_code(qr_display, url)

            print(f"\n📝 DEPLOYMENT INSTRUCTIONS for {deployment_type.upper()}:")
            print("-" * 50)

            if deployment_type == 'local':
                print("1. Install a local server (e.g., Live Server in VS Code)")
                print("2. Serve the HTML files from the project directory")
                print("3. Make sure all files (index.html, surgery-data.js) are accessible")
                print("4. Use the generated QR code for testing")

            elif deployment_type == 'vercel':
                print("1. Push your files to GitHub repository")
                print("2. Connect your GitHub repo to Vercel")
                print("3. Update the URL in this script with your Vercel domain")
                print("4. Regenerate QR code with the live URL")
                print("5. Deploy using the QR code")

            elif deployment_type == 'custom':
                print(f"1. Deploy your files to: {custom_url}")
                print("2. Ensure all assets are properly served")
                print("3. Test the URL in browser before using QR code")
                print("4. Share the QR code for mobile access")

            return qr_filename

        return None

def main():
    """Main function with command-line interface"""
    parser = argparse.ArgumentParser(description='Generate QR codes for AR Surgery Training')
    parser.add_argument('--type', '-t', choices=['local', 'vercel', 'custom'], 
                       default='vercel', help='Deployment type')
    parser.add_argument('--url', '-u', type=str, help='Custom URL for deployment')
    parser.add_argument('--output', '-o', type=str, default='ar_surgery_qr.png', 
                       help='Output filename')

    args = parser.parse_args()

    print("🏥 AR Surgery Training - QR Generator")
    print("=" * 60)

    generator = ARSurgeryQRGenerator()

    # Update URLs if provided
    if args.url:
        if args.type == 'custom':
            result = generator.generate_for_deployment('custom', args.url)
        else:
            generator.urls[args.type] = args.url
            result = generator.generate_for_deployment(args.type)
    else:
        result = generator.generate_for_deployment(args.type)

    if result:
        print(f"\n✅ SUCCESS! QR code generated: {result}")
        print("🎓 Ready for medical education deployment!")
    else:
        print("❌ Failed to generate QR code")

if __name__ == "__main__":
    # If no command line args, run interactive mode
    import sys
    if len(sys.argv) == 1:
        print("🏥 AR Surgery Training - QR Generator (Interactive Mode)")
        print("=" * 60)

        generator = ARSurgeryQRGenerator()

        print("\nSelect deployment type:")
        print("1. Local development (localhost:3000)")
        print("2. Vercel deployment (requires URL update)")
        print("3. Custom URL")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            generator.generate_for_deployment('local')
        elif choice == '2':
            custom_url = input("Enter your Vercel URL (or press Enter for default): ").strip()
            if custom_url:
                generator.urls['vercel'] = custom_url
            generator.generate_for_deployment('vercel')
        elif choice == '3':
            custom_url = input("Enter your custom URL: ").strip()
            if custom_url:
                generator.generate_for_deployment('custom', custom_url)
            else:
                print("❌ Custom URL required")
        else:
            print("❌ Invalid choice")
    else:
        main()
