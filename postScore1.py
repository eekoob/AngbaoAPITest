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

	#77
	xrange = [1]
	for x in xrange:		
		# ============= <POST SCORE>================
		response=requests.post(main_api,cookies=cookie).json()
		if response.get('success') :
			id = response.get('data').get('id')
			print("[#77] POST SCORE = 0 >>> URL => " + main_api + " ID=" + str(id))
			# CHECK in DB
			cur.execute("SELECT * FROM songkran_user_score WHERE id="+str(id))
			
			for row in cur:
				if row[3] == 0 :
					print("[#77] OK : SCORE = " + str(row[3]) + "\n")	
		else :
			print(str(response)+"\n")
		# ============= </POST SCORE> ================
		cur.execute("DELETE FROM songkran_user_score WHERE id="+str(id))
		conn.commit()

	#78
	xrange = [1]
	for x in xrange:		
		# ============= <POST SCORE>================
		response=requests.post(main_api,cookies=cookie).json()
		if response.get('success') :
			id = response.get('data').get('id')
			print("[#78] POST SCORE = 0 >>> URL => " + main_api + " ID=" + str(id))
			# CHECK in DB
			cur.execute("SELECT * FROM songkran_user_score WHERE id="+str(id))
			
			for row in cur:
				if row[3] == 0 :
					print("[#78] OK : SCORE = " + str(row[3]) + "\n")	
		else :
			print(str(response)+"\n")
		# ============= </POST SCORE> ================
		cur.execute("DELETE FROM songkran_user_score WHERE id="+str(id))
		conn.commit()


		# ============= <SET DB BACK> ================
		cur.execute("UPDATE songkran_user SET free_life='10', extra_life='10' WHERE username = 'jdc_jdyc_50'")
		conn.commit()		
		requests.delete(config.mainUrl + "/users",cookies=cookie)
		# ============= </SET DB BACK> ===============

	cur.close()	
	conn.close()
# run()