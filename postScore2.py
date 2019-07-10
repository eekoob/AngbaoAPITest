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




	#79
	cur.execute("UPDATE songkran_user SET free_life='0', extra_life='0', send_life='0', receive_life='3' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)
	# ============= <POST SCORE>================
	response=requests.post(main_api,cookies=cookie).json()
	if not response.get('success') :
		print("[#79] POST SCORE (free=0, extra=0, send=0, receive=3) >>> URL => " + main_api)
		# Check that it should fail for 105
		if response.get('code') == 105:
			print("[#79] OK : CODE = " + str(response.get('code')) + " MESSAGE = " + response.get('message') + "\n")	
	else :
		print(str(response)+"\n")
	# ============= </POST SCORE> ================

	#80
	cur.execute("UPDATE songkran_user SET free_life='0', extra_life='0', send_life='0', receive_life='2' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)
	# ============= <POST SCORE>================
	response=requests.post(main_api,cookies=cookie).json()
	if not response.get('success') :
		print("[#80] POST SCORE (free=0, extra=0, send=0, receive=2) >>> URL => " + main_api)
		# Check that it should fail for 106
		if response.get('code') == 106:
			print("[#80] OK : CODE = " + str(response.get('code')) + " MESSAGE = " + response.get('message') + "\n")	
	else :
		print(str(response)+"\n")
	# ============= </POST SCORE> ================

	#81
	cur.execute("UPDATE songkran_user SET free_life='0', extra_life='1', send_life='0', receive_life='0' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)
	# ============= <POST SCORE>================
	response=requests.post(main_api,cookies=cookie).json()
	if response.get('success') :
		id = response.get('data').get('id')
		print("[#81] POST SCORE (free=0, extra=1, send=0, receive=0) >>> URL => " + main_api + " ID=" + str(id))
		# CHECK in DB
		cur.execute("SELECT * FROM songkran_user_score WHERE id="+str(id))
		
		for row in cur:
			if row[3] == 0 :
				print("[#81] OK : SCORE = " + str(row[3]) + "\n")		
	else :
		print(str(response)+"\n")
	# ============= </POST SCORE> ================
	cur.execute("DELETE FROM songkran_user_score WHERE id="+str(id))
	conn.commit()

	#82
	cur.execute("UPDATE songkran_user SET free_life='1', extra_life='0', send_life='0', receive_life='0' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)
	# ============= <POST SCORE>================
	response=requests.post(main_api,cookies=cookie).json()
	if response.get('success') :
		id = response.get('data').get('id')
		print("[#82] POST SCORE (free=1, extra=0, send=0, receive=0) >>> URL => " + main_api + " ID=" + str(id))
		# CHECK in DB
		cur.execute("SELECT * FROM songkran_user_score WHERE id="+str(id))
		
		for row in cur:
			if row[3] == 0 :
				print("[#82] OK : SCORE = " + str(row[3]) + "\n")		
	else :
		print(str(response)+"\n")
	# ============= </POST SCORE> ================
	cur.execute("DELETE FROM songkran_user_score WHERE id="+str(id))
	conn.commit()

	#84 (1)
	cur.execute("UPDATE songkran_user SET free_life='1', extra_life='1', send_life='0', receive_life='0' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)
	# ============= <POST SCORE>================
	response=requests.post(main_api,cookies=cookie).json()
	if response.get('success') :
		id = response.get('data').get('id')
		print("[#84] POST SCORE (free=1, extra=1, send=0, receive=0) >>> URL => " + main_api + " ID=" + str(id))
		# CHECK in DB
		cur.execute("SELECT * FROM songkran_user_score WHERE id="+str(id))
		for row in cur:
			if row[3] == 0 :
				print("[#84] OK : SCORE = " + str(row[3]))		
		cur.execute("SELECT * FROM songkran_user WHERE username='jdc_jdyc_50'")
		for row in cur:
			if row[4] == 0 :
				print("[#84] OK : extra_life decreased to " + str(row[4]) + "\n")	
	else :
		print(str(response)+"\n")
	# ============= </POST SCORE> ================
	cur.execute("DELETE FROM songkran_user_score WHERE id="+str(id))
	conn.commit()

	#84 (2)
	cur.execute("UPDATE songkran_user SET free_life='1', extra_life='0', send_life='0', receive_life='0' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)
	# ============= <POST SCORE>================
	response=requests.post(main_api,cookies=cookie).json()
	if response.get('success') :
		id = response.get('data').get('id')
		print("[#84] POST SCORE (free=1, extra=0, send=0, receive=0) >>> URL => " + main_api + " ID=" + str(id))
		# CHECK in DB
		cur.execute("SELECT * FROM songkran_user_score WHERE id="+str(id))
		for row in cur:
			if row[3] == 0 :
				print("[#84] OK : SCORE = " + str(row[3]))		
		cur.execute("SELECT * FROM songkran_user WHERE username='jdc_jdyc_50'")
		for row in cur:
			if row[3] == 0 :
				print("[#84] OK : free_life decreased to " + str(row[3]) + "\n")	
	else :
		print(str(response)+"\n")
	# ============= </POST SCORE> ================
	cur.execute("DELETE FROM songkran_user_score WHERE id="+str(id))
	conn.commit()



	# ============= <SET DB BACK> ================
	cur.execute("UPDATE songkran_user SET free_life='10', extra_life='10', send_life='0', receive_life='0' WHERE username = 'jdc_jdyc_50'")
	conn.commit()
	requests.delete(config.mainUrl + "/users",cookies=cookie)

	# ============= </SET DB BACK> ===============

	cur.close()	
	conn.close()
# run()
