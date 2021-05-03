from email.message import EmailMessage
import smtplib
from decouple import config
import imghdr

# Fetching environmental variables
email = config('GMAIL_USER')
password = config('GMAIL_PASS')

# contact-list
contacts = ['testmailtesting17@gmail.com']

# subject
subject = "Alert this is the test msg"

# Mail sending initiator


def start_service(msg):
    # Context manager to start SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        # Login to server
        smtp.login(email, password)

        # sending email
        smtp.send_message(msg)

# setting up msg content


def msg_content():

    msg = EmailMessage()
    msg['Subject'] = subject
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

    img_file = ['bash.png', 'server.png']
    doc_file = ['test1.docx', 'test2.pdf']

    def upload_img(img_file):
        # uploading files (Images)

        for file in img_file:
            # opening attachment file
            with open(file, 'rb') as f:
                file_data = f.read()
                # file type (Image type )
                file_type = imghdr.what(f.name)
                file_name = f.name

            msg.add_attachment(file_data, maintype='image',
                               subtype=file_type, filename=file_name)

    def upload_docs(doc_file):
        # uploading files (octet-stream)
        for file in doc_file:
            # opening attachment file
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name
                file_type = 'octet-stream'

            msg.add_attachment(file_data, maintype='application',
                               subtype=file_type, filename=file_name)

    start_service(msg)


msg_content()
