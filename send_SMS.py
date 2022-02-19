import smtplib
from datetime import datetime
from webbrowser import get

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(message):
	# Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = ''
	auth = ('email', 'password')

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail(auth[0], to_number, message)



def get_date():
	today = datetime.today().weekday()

	date = datetime.today().strftime('%Y-%m-%d')

	print(today,date)


def select_message(today,date):

	if(today == 0):
		message = "Feed and Change Water for Peanut today Please!"
	elif(today == 1):
		message = "Feed Peanut Today Please!"
	elif(today == 2):
		message = "Feed Peanut Today Please!"
	elif(today == 3):
		message = "Feed and Water Peanut Today Please!"
	elif(today == 4):
		message = "Feed Peanut Today Please!"
	elif(today == 5):
		message = "Feed Peanut Today Please!"
	elif(today == 6):
		message = "Feed Peanut Today Please!"
	if(date == "2022-03-01" or date == "2022-03-15"):
		message = "Feed and Change Bedding Today Please!"

	send(message)

def main():

	select_message(2,"2022-03-01")

main()
