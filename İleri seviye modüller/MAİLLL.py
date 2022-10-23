import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

kaç_kisi = int(input("KAÇ KİŞİYE GÖNDERİLECEK?\n\nCevap:"))
while True:
    kaç_kisi = kaç_kisi - 1
    mesaj = MIMEMultipart()
    e_mail = input("E-MAİL:")
    mesaj["From"] = e_mail
    password = input("E-MAİL ŞİFRESİ:")
    kime = input("GÖNDERİLECEK E-MAİL:")
    mesaj["To"] = kime
    massage = input("MAİL BAŞLIĞI:")
    mesaj["Subject"] = massage
    yazi = input("MAİL İÇERİĞİ:")
    mesaj_govdesi = MIMEText(yazi, "plain")
    mesaj.attach(mesaj_govdesi)
    try:
        if (e_mail.endswith("@yandex.com")):
            mail = smtplib.SMTP("smtp.yandex.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(e_mail, password)
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        elif (e_mail.endswith("@outlook.com") or e_mail.endswith("@hotmail.com")):
            mail = smtplib.SMTP("smtp.outlook.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(e_mail, password)
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        elif (e_mail.endswith("@gmail.com")):
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(e_mail, password)
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

        print("Mail Başarıyla Gönderildi!")
        mail.close()
    except:
        sys.stderr.write("Hata!")
        sys.stderr.flush()
    if (kaç_kisi == 0):
        break