import qrcode


# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=2,
#     border=2,
#     )


# qr.add_data('1@7RwLUXBEEJXXSPqw8JUve+DAeq9nHW6NxH5mxLA5GqFdtqQnTuYQjsZro8Pj9E5DkM6cywOMM14glA==,KvtU+9uIy/PgRM4whIBEf6OvDHIBaqYjPNaRs0BIWHk=,dax/i2tE5NDxygA/MNh9GQ==')
# qr.print_ascii()
# input()


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)

data = '1@7RwLUXBEEJXXSPqw8JUve+DAeq9nHW6NxH5mxLA5GqFdtqQnTuYQjsZro8Pj9E5DkM6cywOMM14glA==,KvtU+9uIy/PgRM4whIBEf6OvDHIBaqYjPNaRs0BIWHk=,dax/i2tE5NDxygA/MNh9GQ=='
qr.add_data(data)
qr.print_ascii()
