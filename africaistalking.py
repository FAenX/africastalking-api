from africastalking import AfricasTalkingGateway as client
username = "jayz"
apikey   = "1775011c1f6ad933a2fe8f72e87069becb392da555685f11385f6b57bfee913a"
to      = "+254712742551"
message = "we unaonaje"
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