.

Pour envoyer des e-mails avec Python, vous pouvez utiliser la bibliothèque SMTP (Simple Mail Transfer Protocol). La bibliothèque SMTP est intégrée dans Python et vous permet d'envoyer des e-mails en utilisant un serveur SMTP.

Voici un exemple de code pour envoyer un e-mail avec Python : 

import smtplib 
from email.message import EmailMessage 
  
# Créer le message 
message = EmailMessage() 
message['Subject'] = 'Un sujet' 
message['From'] = 'adresse_email@example.com' 
message['To'] = 'destinataire@example.com' 
message.set_content('Le contenu de votre message') 

 # Créer le serveur SMTP et se connecter à celui-ci 
smtp_server = smtplib.SMTP('smtp.example.com', 587) # Remplacer par votre serveur SMTP et le port approprié  
smtp_server.starttls() # Activer la connexion sécurisée  
smtp_server.login('adresse_email@example.com', 'mot_de_passe') # Connectez-vous au serveur avec votre adresse email et votre mot de passe  

 # Envoyer le message  
smtp_server.send_message(message)  

 # Se déconnecter du serveur  
smtp_server.quit()