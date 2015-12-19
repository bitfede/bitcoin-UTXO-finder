
import json
import requests
import logging

logging.captureWarnings(True)

print("Hello User!")
print("This program will use the Blockchain.info API to retrieve any unspent outputs for a given bitcoin address")

#example address
print("Please input the BTC addres you want to verify:") ,
address = raw_input()

#send request to blockchain.info APIs , will retrieve a JSON document with all the transactions
resp = requests.get('https://blockchain.info/unspent?active=%s' % address)

#store the list into utxo_list
utxo_list = json.loads(resp.text)["unspent_outputs"]

print(" ")
print("FORMAT:") , ("  [ Transaction ID : Index Number - Balance available to spend (in BTC)  ]")
print(" ")

total = 0
total = int(total)
#for each json object in the list of json objects we will now pretty print the important elements
for utxo in utxo_list:
	#print transactions ID : index number - balance available to spend
	print("%s:%d - %f BTC" % (utxo['tx_hash'], utxo['tx_output_n'], float(utxo['value']) / 100000000))
	print(" ")
	total = total + utxo['value'] + 0

print("Total BTC available to spend: %f" % (float(total) / 100000000) )
print("------")