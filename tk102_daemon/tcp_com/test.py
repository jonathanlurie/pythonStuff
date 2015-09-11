from tcpMessageDecoder import *

from dbDataExchange import *


msg = "140321190607,+33624267358,GPRMC,180607.683,A,4335.9151,N,00127.1699,E,0.00,32.59,210314,,,A*5D,F,, imei:013227007709334,05,144.3,F:3.79V,0,139,21644,208,01,320F,1F24"
#msg = ""
msgDec = tcpMessageDecoder(msg)
#print(msgDec.toString())


if(msgDec.isMsgValid()):
	dbEx = dbDataExchange()
	dbEx.addRecord(msgDec)