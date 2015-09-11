import MySQLdb
import _mysql_exceptions
# documentation at http://mysql-python.sourceforge.net/MySQLdb-1.2.2/

import dbInit

from tcpMessageDecoder import *

class dbDataExchange:
	
		def __init__(self):
			a = 1
		
		# PRIVATE
		# query something in SQL and return the result
		def _querySomething(self, q):
			
			result = None
			
			try:
				db = MySQLdb.connect(host = dbInit.dbHost,		# your host, usually localhost
					user = dbInit.dbUser,					# your username
					passwd = dbInit.dbPasswd,		# your password
					db = dbInit.dbName)					# name of the data base

				# you must create a Cursor object. It will let
				#  you execute all the queries you need
				cur = db.cursor() 

				# Use all the SQL you like
				cur.execute(q)
		
				# for updates
				db.commit()
				db.close()

				result = cur.fetchall()
			
				
			# if a table does not exist for example
			except _mysql_exceptions.ProgrammingError as e:
				print("ERROR: programming error: " + str(e.__str__() ) )
			
			except _mysql_exceptions.OperationalError as e:
				print("ERROR: probleme operationnel: " + str(e.__str__() ))
				
			return result
			
		# build an UPDATE query from a list of entries and a list of values
		# return this query as a string
		def _buildInsertQuery(self, tableID, entries, values):
		
			# must have a value for each entry
			if(len(entries) != len(values)):
				return None
	
			q = "INSERT INTO " + tableID + " ( "
			
			for i in range(0, len(entries)):
				q += entries[i] 
				if(i != (len(entries) - 1) ):
					q += ", "
				q += " "

			q += ") VALUES ("
			
			for i in range(0, len(entries)):
				q += "'" + str(values[i]) + "'"  
				if(i != (len(entries) - 1) ):
					q += ", "
				q += " "
			q += ")"
				
			return q
	
		# check into the database and
		# return the current trip ID as a string
		def getCurrentTripID(self):
			q = "SELECT CURRENT_TRIP_ID FROM settings"
			result = self._querySomething(q)
			return str(result[0][0])
			
		# set the trip ID in the database
		# does not return anything
		def setCurrentTripID(self, tripID):
			q = request_updateCurrentTripId = "UPDATE settings SET CURRENT_TRIP_ID='" + str(tripID) + "'"
			self._querySomething(q)
		
		
		# takes a tcpMessageDecoder object and save it in the database
		def addRecord(self, tcpMsgDcdr):
			entries = ["message", "latitude", "longitude", "altitude", "date", "time", "dateUTC", "timeUTC", "speedKm", "batteryVolt", "bearing", "numberOfSatellites", "tripId"]
			values = []
			values.append(tcpMsgDcdr.getMsg() )
			values.append(tcpMsgDcdr.getLatitude() )
			values.append(tcpMsgDcdr.getLongitude() )
			values.append(tcpMsgDcdr.getAltitude() )
			values.append(tcpMsgDcdr.getDate() )
			values.append(tcpMsgDcdr.getTime() )
			values.append(tcpMsgDcdr.getDateUTC() )
			values.append(tcpMsgDcdr.getTimeUTC() )
			values.append(tcpMsgDcdr.getSpeedKm() )
			values.append(tcpMsgDcdr.getBatteryVolt() )
			values.append(tcpMsgDcdr.getBearing() )
			values.append(tcpMsgDcdr.getNumberOfSatellites() )
			
			values.append( self.getCurrentTripID()) 
			
			tableID = "records"
			
			q = self._buildInsertQuery(tableID, entries, values)
			self._querySomething(q)
			


# testing it		
#dbdex = dbDataExchange()
#dbdex.setCurrentTripID("helloTruc")
#print dbdex.getCurrentTripID()
