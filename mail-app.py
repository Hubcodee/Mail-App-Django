from email.message import EmailMessage
import smtplib
from decouple import config
import imghdr

# Fetching environmental variables
email = config('GMAIL_USER')
password = config('GMAIL_PASS')

# contact-list
contacts = ['anshshrivas26@gmail.com']

msg = EmailMessage()
msg['Subject'] = "Check out attachment"
msg['From'] = email
msg['To'] = ','.join(contacts)
msg.set_content('Attachment Included')

msg.add_alternative("""\
<!DOCTYPE html>
    <html>
        <body>
            <h1>Hello</h1>
        </body>
    </html>
""", subtype='html')

# # uploading files (Images)
# img_file = ['bash.png', 'server.png']
# for file in img_file:
#     # opening attachment file
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         # file type (Image type )
#         file_type = imghdr.what(f.name)
#         file_name = f.name

#     msg.add_attachment(file_data, maintype='image',
#                        subtype=file_type, filename=file_name)

# # uploading files (octet-stream)
# doc_file = ['test1.docx', 'test2.pdf']
# for file in doc_file:
#     # opening attachment file
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_name = f.name
#         file_type = 'octet-stream'

#     msg.add_attachment(file_data, maintype='application',
#                        subtype=file_type, filename=file_name)

# Context manager to start SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    '''
    -->RUN IN CMD FOR DEBUGGING SERVER
    #python -m smtpd -c DebuggingServer -n localhost:1025
    -->CODE
    # with smtplib.SMTP('localhost', 1025) as smtp:
    # # Authenticating the user
    # smtp.ehlo()
    # # TLS encryption of traffic
    # smtp.starttls()
    # # Authenticating the encryption
    # smtp.ehlo()
    '''
    # Login to server
    smtp.login(email, password)

    # sending email
    smtp.send_message(msg)
