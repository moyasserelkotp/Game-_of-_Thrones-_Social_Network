#!/usr/bin/env python
"""Convert Markdown to PDF using ReportLab"""

import os
import subprocess

html_file = 'got_complete_report.html'
pdf_file = 'got_complete_report.pdf'

# Check if HTML file exists
if os.path.exists(html_file):
    # Try using Microsoft Word (if available)
    try:
        import win32com.client
        word = win32com.client.Dispatch('Word.Application')
        word.Visible = False
        
        html_path = os.path.abspath(html_file)
        pdf_path = os.path.abspath(pdf_file)
        
        doc = word.Documents.Open(html_path)
        doc.SaveAs(pdf_path, FileFormat=17)  # 17 is PDF format
        doc.Close()
        word.Quit()
        
        print(f"✓ PDF successfully created using Microsoft Word: {pdf_file}")
        print(f"✓ File size: {os.path.getsize(pdf_file) / 1024:.2f} KB")
    except:
        # Try using LibreOffice if available
        try:
            libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
            if os.path.exists(libreoffice_path):
                subprocess.run([
                    libreoffice_path,
                    '--headless',
                    '--convert-to', 'pdf',
                    '--outdir', '.',
                    html_file
                ], check=True)
                print(f"✓ PDF successfully created using LibreOffice: {pdf_file}")
                if os.path.exists(pdf_file):
                    print(f"✓ File size: {os.path.getsize(pdf_file) / 1024:.2f} KB")
            else:
                raise FileNotFoundError("LibreOffice not found")
        except:
            print(f"Manual conversion needed:")
            print(f"")
            print(f"Method 1: Using Browser (Recommended)")
            print(f"  1. Open: {html_file}")
            print(f"  2. Press: Ctrl+P (Print)")
            print(f"  3. Select: 'Save as PDF'")
            print(f"  4. Save as: {pdf_file}")
            print(f"")
            print(f"Method 2: Using Online Tool")
            print(f"  Visit: https://cloudconvert.com/html-to-pdf")
            print(f"  Upload: {html_file}")
            print(f"")
else:
    print(f"Error: {html_file} not found")
