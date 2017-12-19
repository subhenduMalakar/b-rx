import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import requests





for k in range(0,1000):
	p=0
	
	main_api='https://bittrex.com/api/v1.1/public/getmarketsummaries'
	print("-------------------------------")
	json_data=requests.get(main_api).json()
	for x in range(0,267):
		carp=json_data['result'][x]['MarketName']
		a = open(x+'.txt', 'a')
		values=json_data['result'][x]['Last']
		a.write(str(x+1)+'/'+carp','+str(values)+'\n')
		print("-------------------"+"k="+str(k)+"a="+str(x)+" "+carr)
		p=p+1

		
		a.close()
	time.sleep(2)
