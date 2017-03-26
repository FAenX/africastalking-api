from africastalking import AfricasTalkingGateway as client
username = ""
apikey   = ""
to      = ""
message = "
#sender = "mimi for mp"
gateway = client.AfricasTalkingGateway(username, apikey)

try:   
    results = gateway.sendMessage(to, message)#,sender)    
    for recipient in results:
			print recipient
			print ('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
															recipient['status'],
															recipient['messageId'],
                                                            recipient['cost']))

except client.AfricasTalkingGatewayException, e:
   print 'Encountered an error while sending: %s' % str(e)
