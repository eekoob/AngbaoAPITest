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



	#90
	cur.execute("UPDATE songkran_user SET free_life='1', extra_life='0', send_life='0', receive_life='0' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)
	# ============= <POST SCORE>================
	response=requests.post(main_api,cookies=cookie).json()
	if response.get('success') :
		id = response.get('data').get('id')
		# print(str(id))
	else :
		print(str(response)+"\n")
	# ============= </POST SCORE> ================

	# ============== <PUT SCORE> ================
	main_api = config.mainUrl + "/users/scores/"
	url = main_api + str(id-1)
	payload = "{\n\t\"us\": \"U2FsdGVkX1+mxrtONlocv59fzrbZM9thQdCkJLP7NOA=\"\n}\n" # SCore=21
	headers = {
	    'Content-Type': "application/json",
	    }

	response = requests.put(url, cookies=cookie, data=payload, headers=headers).json()
	print("[#90] PUT SCORE = 21 to wrong score_id. " + " >>> URL => " + url)
	if not response.get('success') :
		if response.get('code') == 700 :
			print("[#90] OK : CODE = " + str(response.get('code')) + " MESSAGE = " + response.get('message') + "\n")
		else : print ("[#90] FAIL !! : " + str(response) + "\n")
	else :
		print("[#90] " + str(response) + "\n")
	# ============== </PUT SCORE> ================
	cur.execute("DELETE FROM songkran_user_score WHERE id="+str(id))
	cur.execute("UPDATE songkran_user SET free_life='1', extra_life='0', send_life='0', receive_life='0' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)


	#95 #96
	cur.execute("UPDATE songkran_user SET free_life='1', extra_life='1', send_life='0', receive_life='0' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)
	xrange = [150, 151]
	for x in xrange:		
		# ============= <POST SCORE>================
		response=requests.post(main_api,cookies=cookie).json()
		if response.get('success') :
			id = response.get('data').get('id')
			# print(str(id))
		else :
			print(str(response)+"\n")
		# ============= </POST SCORE> ================

		# ============== <PUT SCORE> ================
		main_api = config.mainUrl + "/users/scores/"
		url = main_api + str(id)
		if x == 150: payload = "{\n\t\"us\": \"U2FsdGVkX18I+dsHYZ7YrAWgpBVzvaLQzK3gbWO5OdU=\"\n}\n"
		if x == 151: payload = "{\n\t\"us\": \"U2FsdGVkX191zPXhwkzihXvc7UuKtkYTSgPiZF+UslM=\"\n}\n"

		headers = {
		    'Content-Type': "application/json",
		    }

		response = requests.put(url, cookies=cookie, data=payload, headers=headers).json()
		print("[#95 #96] PUT SCORE = " + str(x) + " >>> URL => " + url)
		if response.get('success') :
			if x == 150 and response.get('data').get('reward').get('message')=='200' : 
				print("[#95] OK : RECEIVE JD Point = " + response.get('data').get('reward').get('message') + "\n")
			else : print ("[#95] FAIL !! : " + str(response) + "\n")
		elif not response.get('success') :
			if x == 151 and not (response.get('success')) and response.get('code')==701 :
				print("[#96] OK : " + response.get('message') + "\n")
			else : print ("[#96] FAIL !! : " + str(response) + "\n")
		else :
			print(" [#95, #96] " + str(response) + "\n")
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

