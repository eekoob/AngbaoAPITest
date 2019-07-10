import urllib.parse
import requests
import pymysql
import config

def run():

	conn = pymysql.connect(host=config.dbHost, port=config.dbPort, user=config.dbUser, passwd=config.dbPasswd, db='jd_songkran')
	cur = conn.cursor()
	main_api = config.mainUrl + "/users/score-stats?gameRound="
	cookie = config.cookie1
	headers = {'Cookie':cookie}



	#97 #98
	cur.execute("UPDATE songkran_user_total_score SET total_score='0' WHERE username = 'jdc_jdyc_50' AND game_round='1'")
	conn.commit()
	# ============= <GET PERCENT>================
	response=requests.get(main_api + "1" , cookies=cookie).json()
	print("[#97 #98] Get Score Stat of Round 1. Set Score = 0. Percent beat should be 0.0")
	if response.get('success') and response.get('code') == 0 and response.get('data').get('percentBeat') == 0.0 :
		print("[#97 #98] OK : " + str(response) + "\n")
	else :
		print("[#97 #98] FAIL !! : " + str(response) + "\n")
	# ============= </GET PERCENT> ================


	#97 #98
	cur.execute("UPDATE songkran_user_total_score SET total_score='0' WHERE username = 'jdc_jdyc_50' AND game_round='2'")
	conn.commit()
	# ============= <GET PERCENT>================
	response=requests.get(main_api + "2" , cookies=cookie).json()
	print("[#97 #98] Get Score Stat of Round 2. Set Score = 0. Percent beat should be 0.0")
	if response.get('success') and response.get('code') == 0 and response.get('data').get('percentBeat') == 0.0 :
		print("[#97 #98] OK : " + str(response) + "\n")
	else :
		print("[#97 #98] FAIL !! : " + str(response) + "\n")
	# ============= </GET PERCENT> ================


	#97 #98
	cur.execute("UPDATE songkran_user_total_score SET total_score='0' WHERE username = 'jdc_jdyc_50' AND game_round='3'")
	conn.commit()
	# ============= <GET PERCENT>================
	response=requests.get(main_api + "3" , cookies=cookie).json()
	print("[#97 #98] Get Score Stat of Round 3. Set Score = 0. Percent beat should be 0.0")
	if response.get('success') and response.get('code') == 0 and response.get('data').get('percentBeat') == 0.0 :
		print("[#97 #98] OK : " + str(response) + "\n")
	else :
		print("[#97 #98] FAIL !! : " + str(response) + "\n")
	# ============= </GET PERCENT> ================


	#99
	cur.execute("UPDATE songkran_user_total_score SET total_score='200' WHERE username = 'jdc_jdyc_50' AND game_round='1'")
	conn.commit()
	# ============= <GET PERCENT>================
	cookieFake = {'pt_pin':'jdc_jdyc_50','pt_key':'AAFcnCxsADAV4OnmgPLQf_AAA_sjOCWRQoBs2Nz2Jq61kG1Hnl8296HBVs74hr9j7TfAdr5oFI7ZtP_E'}
	response=requests.get(main_api + "1" , cookies=cookieFake).json()
	print("[#99] Get Score Stat of Round 1 NO VALID COOKIE. Set Score = 200. Should fail 401")
	if not response.get('success') :
		if response.get('code') == 401 :
			print("[#99] OK : " + str(response) + "\n")
	else :
		print("[#99] FAIL !! : " + str(response) + "\n")
	# ============= </GET PERCENT> ================

	cur.close()	
	conn.close()
# run()

