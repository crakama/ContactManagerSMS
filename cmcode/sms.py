
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

class SMS():
	contactlist = ['+254721949259', '+254737882875']
	msg = "Lets meet at Hogwarts"
	v = ",".join(contactlist)
	# Specify your login credentials
	username = "johnkariuki"
	apikey   = "00b63f212d6431ef6695409ec668e28f354f6387ab854dc5167667df8f60a1a5"
	# Specify the numbers that you want to send to in a comma-separated list
	# Please ensure you include the country code (+254 for Kenya in this case)
	to      = "+254728590438, +254737882875,+254721949259"
	# And of course we want our recipients to know what we really do
	message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
	# Create a new instance of our awesome gateway class
	gateway = AfricasTalkingGateway(username, apikey)
	# Any gateway errors will be captured by our custom Exception class below, 
	# so wrap the call in a try-catch block
	try:
	    # Thats it, hit send and we'll take care of the rest.
	    
	    results = gateway.sendMessage(to, msg)
	    
	    for recipient in results:
	        # status is either "Success" or "error message"
	        print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
	                                                            recipient['status'],
	                                                            recipient['messageId'],
	                                                            recipient['cost'])
	except AfricasTalkingGatewayException, e:
	    print 'Encountered an error while sending: %s' % str(e)
