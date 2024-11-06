# Email Voucher Sender

**English below**
Dieses Python-Skript sendet E-Mails mit Anhängen an eine Liste von Empfängern. Es ist insbesondere dafür gedacht, personalisierte Voucher als PDF-Dateien zu versenden, die über eine CSV-Datei und ein Ordnerverzeichnis für die Anhänge zugeordnet werden.
Einen Konkreten Workflow für die Bochumer Berufskollegs finden Sie unten.

## Voraussetzungen

- Python 3.11.3 (getestet)
- Die Bibliotheken `smtplib`, `email`, `os`, `csv`, `tkinter`, `time` (alle sind in der Standardbibliothek von Python enthalten).

## Funktionalität

Das Skript:

1. Fordert den Benutzer auf, die eigene E-Mail-Adresse und das Passwort einzugeben (Hinweis zur Passwortsicherheit siehe unten).
2. Öffnet eine grafische Oberfläche (GUI) zur Auswahl des Ordners mit den Voucher-Dateien und einer CSV-Datei mit den Empfänger-E-Mail-Adressen.
3. Prüft, ob die Anzahl der Empfänger in der CSV-Datei mit der Anzahl der Dateien im Voucher-Ordner übereinstimmt.
4. Sendet eine E-Mail an jeden Empfänger mit einem spezifischen Voucher als Anhang.
5. Speichert die Zuordnung von Empfängern zu Vouchern in einer CSV-Datei zur späteren Nachverfolgung.

## Installation und Ausführung

1. **Klone oder lade das Repository herunter.**
2. **Installiere Python 3**, falls noch nicht geschehen.
3. **Installiere die notwendigen Pakete**, falls erforderlich.
4. **Passe das Skript an**, wie unter Konfiguration beschrieben.
5. **Führe das Skript aus**, indem du in der Konsole zum Ordner mit dem Skript navigierst und "python email_voucher_sender.py" ausführst.

## Konfiguration

1. **SMTP-Einstellungen** anpassen. Standartmäßig ist der Server und Port für O365 (smtp.office365.com, 587) gesetzt.
2. **Emailaccountpasswort setzen/einbinden** entweder mit der getpass library, APP-Kennwort oder Umgebungsvariablen.
3. **E-Mail-Betreff und Nachrichtentext ändern**

## Workflow für die Bochumer Berufskollegs

1. Auf der Seite unseres Anbieters Vouchers für den benötigten Zeitraum (Schuljahr, bei SuS bzw. ein bestimmter Tag bei Veranstaltungen mit Externen) erstellen.**Wichtig: 1 Seite pro Voucher auswählen**
2. Jetzt hat man ein PDF mit bis zu 300 Vouchers. Dies kann man nun z.B. mit "PDF 24" in eine Datei pro Voucher Umwandeln. Diese kommen dann in einen leeren Ordner.
3. **CSV-Datei erstellen**, indem man z.B. einen Schild-Export mit allen Emails der SuS zieht und die Dateiendung von .txt in .csv umbenennt. Dann muss man in der obersten Zeile "email-schulisch" durch "Email" ersetzen. Hat man für ein Ausbildertreffen eine Exceldatei mit Name, Email, etc. angelegt, kann man eine Kopie erstellen. Dann löscht man alle anderen Spalten, sodass nur noch in der ersten Spalte "Email" in der Zelle A1 und darunter die entsprechenden Emails der Ausbildungsbetriebskontakte hat. Dann speichert man die Excel-Datei als .csv ab.
Das ganze sieht dann so aus:

    ```csv
    Email
    vorname.nachname@betrieb1.de
    vorname.nachname@betrieb2.de
    vorname.nachname@betrieb3.de
    ```

4. **Programm starten** und bei der Ausführung den Voucherordner und die .csv Datei auswählen.

## Lizenz

CC0 vgl. <https://creativecommons.org/publicdomain/zero/1.0/deed.de>

---

## English

This Python script sends emails with attachments to a list of recipients. It is specifically designed to send personalized vouchers as PDF files, with attachments matched to recipients through a CSV file and a directory of voucher files.
A specific workflow for Bochum vocational schools is outlined below.

## Requirements

- Python 3.11.3 (tested)
- The libraries `smtplib`, `email`, `os`, `csv`, `tkinter`, `time` (all included in Python's standard library).

## Functionality

The script:

1. Prompts the user to enter their email address and password (see password security note below).
2. Opens a graphical user interface (GUI) to select the folder containing voucher files and a CSV file with recipient email addresses.
3. Checks if the number of recipients in the CSV file matches the number of files in the voucher folder.
4. Sends an email to each recipient with a specific voucher attached.
5. Saves the mapping of recipients to vouchers in a CSV file for future reference.

## Installation and Execution

1. **Clone or download the repository.**
2. **Install Python 3** if not already installed.
3. **Install necessary packages** if required.
4. **Customize the script** as described in the Configuration section.
5. **Run the script** by navigating to the script's folder in the console and executing "python email_voucher_sender.py".

## Configuration

1. **Adjust SMTP settings**. By default, the server and port for O365 (smtp.office365.com, 587) are set.
2. **Set/Integrate the email account password** using the getpass library, an app-specific password, or environment variables.
3. **Edit email subject and message content** as needed.

## Workflow for Bochum Vocational Schools

1. On the provider's page, generate vouchers for the required time period (academic year for students or a specific day for events with external guests). **Important: Select 1 page per voucher**.
2. This will produce a PDF with up to 300 vouchers. Use a tool like "PDF 24" to split the PDF into individual files, one for each voucher. Place these files in an empty folder.
3. **Create the CSV file** by, for example, exporting student email addresses from the Schild system and renaming the file extension from .txt to .csv. Then, replace "email-schulisch" in the top row with "Email". For an employer meeting, if you have an Excel file with names, emails, etc., make a copy. Then delete all columns except for the first column, which should contain "Email" in cell A1 and the relevant emails of contacts from the companies below it. Save this file as .csv.
The file should look like this:

    ```csv
    Email
    givenname.surename@company1.de
    givenname.surename@company2.de
    givenname.surename@company3.de
    ```

4. **Start the program** and, during execution, select the voucher folder and the .csv file.

## License

CC0 see <https://creativecommons.org/publicdomain/zero/1.0/deed.en>
