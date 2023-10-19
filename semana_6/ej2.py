email = 'misupergmail@gmail-com,otrocorreo@gmail-com,unacuentamas@gmail-com'

#reemplazar '-' por '.'
email_correcto = email.replace('-', '.')

# dividir la cadena en una lista
email_individual = email_correcto.split(',')

for email in email_individual:
    print(email)