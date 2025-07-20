import qrcode

# Replace with your PDF download URL
pdf_url = "https://raw.githubusercontent.com/K4liber/consistent_importing/presentation/presentation/consistent_importing_all_slides.pdf"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(pdf_url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image (e.g., as a PNG)
img.save("all_slides_pdf_qr_code.png")
