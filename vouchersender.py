import time
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import csv
import tkinter as tk
from tkinter import filedialog
#import getpass

#############################User-Interface##################################################
root = tk.Tk()
root.withdraw() #Versteckt das Hauptfenster


#############################Variablen#######################################################
EMAIL = input("Bitte geben Sie Ihre E-Mail-Adresse ein: ")
PASSWORD = "wtdgqcfzstmsdfbt" #getpass.getpass("Bitte geben Sie Ihr Passwort ein: ") oder "Appkennwort" falls 2FA aktiviert ist
emaillist = []
voucherpath = filedialog.askdirectory(title="Wählen Sie den Ordner mit den Vouchern aus")
if not voucherpath:
    print("Kein Ordner ausgewählt. Das Programm wird beendet.")
    exit()    
# Alle Dateinamen im Voucher-Ordner abrufen
vouchernamelist = os.listdir(voucherpath)

# Pfad zur CSV-Datei
csv_file_path = filedialog.askopenfilename(title="Wählen Sie die CSV-Datei mit den E-Mail-Adressen aus", filetypes=[("CSV files", "*.csv")])
if not csv_file_path:
    print("Keine CSV-Datei ausgewählt. Das Programm wird beendet.")
    exit()


# CSV-Datei einlesen
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emaillist.append(row['email'])

# Überprüfen, ob die Anzahl der E-Mails und Voucher übereinstimmt
if len(emaillist) != len(vouchernamelist):
    print("Anzahl der E-Mails und Voucher stimmen nicht überein.")
    exit()


#############################Methoden#######################################################
def message(subject="Python Notification", text="", attachment=None, sender=None, recipient=None):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    if sender:
        msg['From'] = sender
    if recipient:
        msg['To'] = recipient
    msg.attach(MIMEText(text))
    if attachment:
        if not isinstance(attachment, list):
            attachment = [attachment]
        for one_attachment in attachment:
            try:
                with open(one_attachment, 'rb') as f:
                    file = MIMEApplication(f.read(), name=os.path.basename(one_attachment))
                    file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
                    msg.attach(file)
            except Exception as e:
                print(f"Fehler beim Anhängen der Datei: {e}")
                continue
    return msg

def send_email(msg, recipient):
    if not EMAIL or not PASSWORD:
        print("E-Mail-Zugangsdaten nicht in Umgebungsvariablen gefunden.")
        return
    # Setzen der Header 'From' und 'To' in der Nachricht
    msg['From'] = EMAIL
    msg['To'] = recipient 
    try:
        # Hier die Emailendung und den Port anpassen. Der Port ist in der Regel 587 oder 465.
        smtp = smtplib.SMTP('smtp.office365.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL, PASSWORD)
        smtp.sendmail(from_addr=EMAIL, to_addrs=[recipient], msg=msg.as_string())
        smtp.quit()
        print(f"E-Mail erfolgreich an {recipient} gesendet.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentifizierungsfehler beim Senden der E-Mail an {recipient}: {e}")
    except Exception as e:
        print(f"Fehler beim Senden der E-Mail an {recipient}: {e}")

def dokumentiere_email_voucher_paare(emaillist, vouchernamelist):
    output_csv_path = filedialog.asksaveasfilename(
        title="Speichern der E-Mail-Voucher-Paare als CSV",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")]
    )
    if not output_csv_path:
        print("Kein Speicherort für die CSV-Datei ausgewählt. Das Programm wird beendet.")
        exit()
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Email', 'Vouchername'])
        for email, voucher in zip(emaillist, vouchernamelist):
            writer.writerow([email, voucher])

# Hier Betreff und Emailtext anpassen
def mail():
    for number in range(len(emaillist)):
        attachment_path = os.path.join(voucherpath, vouchernamelist[number])
        recipient_email = emaillist[number]
        
        msg = message(
            "WLAN Zugang BYOD TBS1",
            "Guten Tag \n\nDieser Email ist ein Voucher für den WLAN Zugang BYOD-TBS angehangen. Um diese zu nutzen befolgen Sie bitte folgende Schritte:\nVerbinden Sie sich mit dem WLAN \"BYOD TBS\". \nÖffnen Sie eine beliebige Seite im Browser. \nSie werden nun auf eine andere Seite umgeleitet, wo Sie ihren Vouchercode aus der PDF eingeben können. \n Pro Voucher könnne maximal 3 Geräte verbunden werden. \n\nMit freundlichen Grüßen \nKai Aschenbach",
            attachment=attachment_path,
            sender=EMAIL,
            recipient=recipient_email
        )
        #to = emaillist[number]
        send_email(msg, recipient_email)
        time.sleep(1)

#############################Programmstart##################################################
dokumentiere_email_voucher_paare(emaillist, vouchernamelist)
mail()
