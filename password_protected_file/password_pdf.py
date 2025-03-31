# import pikepdf

# old_pdf = pikepdf.Pdf.open("example.pdf") #open pdf to encrypt

# no_ext = pikepdf.Permissions(extract=False) #stop pdf from opening

# old_pdf.save("protected_file.pdf",
#              encryption=pikepdf.Encryption(user="1234", #password
#                                            owner="Gaurav",
#                                            allow=no_ext))

import pikepdf

# Open the existing PDF file
# old_pdf = pikepdf.Pdf.open("example.pdf")
old_pdf = pikepdf.Pdf.open(r"C:\Users\Gaurav\Downloads\ENGINEERING\Project file\python mini projects\password_protected_file\example.pdf")


# Define permissions for the new encrypted PDF
no_extract = pikepdf.Permissions(extract=False)

# Save the encrypted PDF with specified encryption settings
old_pdf.save("protected_file.pdf",
             encryption=pikepdf.Encryption(user="1234", owner="Gaurav", allow=no_extract))

