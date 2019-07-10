import urllib.parse
import requests
import pymysql
import config

def run():

	

	conn = pymysql.connect(host=config.dbHost, port=config.dbPort, user=config.dbUser, passwd=config.dbPasswd, db='jd_songkran')
	cur = conn.cursor()

	main_api = config.mainUrl + "/users/scores"
	cookie = config.cookie1
	headers = {'Cookie':cookie}

	xrange = [0,20,21,30,31,50,51,60,61]
	# xrange = [61]
	for x in xrange:		
		# ============= <POST SCORE>================
		response=requests.post(main_api,cookies=cookie).json()
		if response.get('success') :
			id = response.get('data').get('id')
			# print(str(id))
		else :
			print(str(response))
		# ============= </POST SCORE> ================

		# ============== <PUT SCORE> ================
		main_api = config.mainUrl + "/users/scores/"
		url = main_api + str(id)
		if x == 0: payload = "{\n\t\"us\": \"U2FsdGVkX18XUl0lqDiYkvMSYxZ30bGH2ORM8MpG1uo=\"\n}\n"
		if x == 20: payload = "{\n\t\"us\": \"U2FsdGVkX1+5BupzP0mtoBgqzsjBHcZEKr5g/ehkzuM=\"\n}\n"
		if x == 21: payload = "{\n\t\"us\": \"U2FsdGVkX1+mxrtONlocv59fzrbZM9thQdCkJLP7NOA=\"\n}\n"
		if x == 30: payload = "{\n\t\"us\": \"U2FsdGVkX1+jQ9HVjwyywRxmKMRIa2pYwi3LNlWzZAM=\"\n}\n"
		if x == 31: payload = "{\n\t\"us\": \"U2FsdGVkX1+pucAju57O0hRFN/3qSZTFul/WaZG1w5g=\"\n}\n"
		if x == 50: payload = "{\n\t\"us\": \"U2FsdGVkX1+RAksVls+hqZQGTQzxg84Q5SK9Zkr7tn0=\"\n}\n"
		if x == 51: payload = "{\n\t\"us\": \"U2FsdGVkX1/BYcRdUYELAoRpgIA3fT/0ARz8tcRvEy8=\"\n}\n"
		if x == 60: payload = "{\n\t\"us\": \"U2FsdGVkX1+6Q5dfzWgUshnnGr67jMo+5LYntgrj5eo=\"\n}\n"
		if x == 61: payload = "{\n\t\"us\": \"U2FsdGVkX1/RpKcivjJm1nIz3xUaielw877tlWLebOA=\"\n}\n"
		headers = {
		    'Content-Type': "application/json",
		    }

		response = requests.put(url, cookies=cookie, data=payload, headers=headers).json()
		if response.get('success') :
			print("[#94] PUT SCORE = " + str(x) + " >>> URL => " + url)
			if x == 0 and response.get('data').get('reward').get('message')=='10' : 
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			elif x == 20 and response.get('data').get('reward').get('message')=='10' :
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			elif x == 21 and response.get('data').get('reward').get('message')=='50' :
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			elif x == 30 and response.get('data').get('reward').get('message')=='50' :
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			elif x == 31 and response.get('data').get('reward').get('message')=='100' :
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			elif x == 50 and response.get('data').get('reward').get('message')=='100' :
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			elif x == 51 and response.get('data').get('reward').get('message')=='150' :
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			elif x == 60 and response.get('data').get('reward').get('message')=='150' :
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			elif x == 61 and response.get('data').get('reward').get('message')=='200' :
				print("[#94] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			else : print ("[#94] FAIL !! : " + str(response) + "\n")
		else :
			print(str(response)+"\n")
		# ============== </PUT SCORE> ================


		# ============= <SET DB BACK> ================
		cur.execute("DELETE FROM songkran_user_score WHERE id="+str(id))
		cur.execute("UPDATE songkran_user SET free_life='10', extra_life='10' WHERE username = 'jdc_jdyc_50'")
		conn.commit()		
		requests.delete(config.mainUrl + "/users",cookies=cookie)
		# ============= </SET DB BACK> ===============

	cur.close()	
	conn.close()
# run()