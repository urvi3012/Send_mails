import smtplib, ssl 

smtp_server = 'smtp.gmail.com'
port = 465

sender = 'sample_mail'
password = 'password'

context = ssl.create_default_context()

'''

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender, password)
	print("done")
'''

try:
	server = smtplib.SMTP(smtp_server, port)
	server.ehlo()
	server.starttls(context=context)
	server.ehlo()
	server.login(sender,password)
	print("2 done")

except Exception as e:
	print(e)
	
finally:
	server.quit()


