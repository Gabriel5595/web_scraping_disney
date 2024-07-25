import smtplib
from datetime import datetime, time
from email.message import EmailMessage
from email.utils import formataddr
import os
import sys
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def send_email_backup():
    formatted_date = datetime.now().strftime("%d%m%Y")
    
    base_path_csv = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'resources', 'csv'))
    base_path_excel = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'resources', 'excel'))
    
    parks = ["Disney's_Animal_Kingdom", "Disney's_Hollywood_Studios", "Epcot", "Magic_Kingdom"]
    
    attachments = []
    
    for park in parks:
        file_name_csv = f"{formatted_date}-{park}.csv"
        file_name_excel = f"{formatted_date}-{park}.xlsx"
        
        full_path_csv = os.path.join(base_path_csv, file_name_csv)
        full_path_excel = os.path.join(base_path_excel, file_name_excel)
        
        attachments.append(full_path_csv)
        attachments.append(full_path_excel)
        
    
    sender_email = 'wish.project.data@gmail.com'
    sender_password = 'exxb rbwh ypwn pmvd'
    recipient_email = 'wish.project.data@gmail.com'
    subject = f'{formatted_date}-backup'
    body = f'Segue em anexo os relatórios do dia {datetime.now()} em formato CSV e Excel.'
    
    msg = EmailMessage()
    msg['From'] = formataddr(('Wish Project Backend', sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)
    
    for attachment in attachments:
        with open(attachment, 'rb') as file:
            file_data = file.read()
            file_name = os.path.basename(attachment)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

def main():
    current_time = datetime.now().time()
    if current_time > time(13, 42) and current_time < time(13, 47):
        send_email_backup()

main()