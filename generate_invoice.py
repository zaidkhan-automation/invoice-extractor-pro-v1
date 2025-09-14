from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

os.makedirs("data", exist_ok=True)
path = os.path.join("data", "sample_invoice.pdf")

c = canvas.Canvas(path, pagesize=A4)
width, height = A4

c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 80, "INVOICE")

c.setFont("Helvetica", 12)
c.drawString(50, height - 120, "Invoice No: INV-2025-001")
c.drawString(50, height - 140, "Date: 2025-09-14")
c.drawString(50, height - 160, "Vendor: Acme Supplies Pvt Ltd")
c.drawString(50, height - 200, "Bill To: Zaid Broski")
c.drawString(50, height - 240, "Description                Qty    Price    Amount")
c.drawString(50, height - 260, "Office chairs              4      2500     10000")
c.drawString(50, height - 280, "Stationery set             10     100      1000")
c.drawString(50, height - 320, "Subtotal:                                11000")
c.drawString(50, height - 340, "Tax (18%):                               1980")
c.drawString(50, height - 360, "Total:                                   12980")

c.showPage()
c.save()

print("✅ Created data/sample_invoice.pdf")