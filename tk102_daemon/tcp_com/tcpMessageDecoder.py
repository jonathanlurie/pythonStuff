class tcpMessageDecoder:
	
	m_msg = None
	m_lat = None
	m_lon = None
	m_alt = None
	m_date = None
	m_time = None
	m_dateUtc = None
	m_timeUtc = None
	m_speedKm = None
	m_batteryVolt = None
	m_bearing = None # angle orientation
	m_numberOfSatellites = None
	m_isMsgValid = None


	def __init__(self, msg):
	
		try:
			# spiting elements
			msgArray = msg.split(',')
			self.m_msg = msg
		
			# LATITUDE , the format is ddmm.mmmm
			latdd = float(msgArray[5][0:2])
			latmmmmm = float(msgArray[5][2:])
			self.m_lat = latdd + (latmmmmm / 60.0)
			if(msgArray[6] == "S"):
				self.m_lat *= -1

			# ALITUDE in m
			self.m_alt = float(msgArray[19])
			
			# LONGITUDE the format is dddmm.mmmm
			londdd = float(msgArray[7][0:3])
			lonmmmmm = float(msgArray[7][3:])
			self.m_lon = londdd + (lonmmmmm / 60.0)
			if(msgArray[8] == "W"):
				self.m_lon *= -1

			# BEARING in angle degree
			self.m_bearing = float(msgArray[10])
		
			# NUMBER OF SATELLITES
			self.m_numberOfSatellites = int(msgArray[18])
		
			# LOCAL DATE no hour
			self.m_date = "20" + str(msgArray[0][0:2]) + "-" + str(msgArray[0][2:4]) + "-" + str(msgArray[0][4:6])
		
			# LOCAL TIME
			self.m_time = str(msgArray[0][6:8]) + ":" + str(msgArray[0][8:10]) + ":" + str(msgArray[0][10:12])
		
			# UTC DATE no hour
			self.m_dateUtc = "20" + str(msgArray[11][4:6]) + "-" + str(msgArray[11][2:4]) + "-" + str(msgArray[11][0:2])

			# UTC TIME 
			self.m_timeUtc = str(msgArray[3][0:2]) + ":" + str(msgArray[3][2:4]) + ":" + str(msgArray[3][4:6])
		
			# SPEED in km
			self.m_speedKm =  float(msgArray[9]) * 1.852
		
			# BATTERY VOLT
			self.m_batteryVolt = float(msgArray[20][2:-1])
		
			self.m_isMsgValid = True
		
		except IndexError as e:
			print("WARNING message tcp incompatible: " + str(e.__str__() ))
			self.m_isMsgValid = False
			
			
	# return whether or not the original message is valid
	def isMsgValid(self):
		return self.m_isMsgValid
		
	def getMsg(self):
		return self.m_msg
		
	def getLatitude(self):
		return self.m_lat
			
	def getLongitude(self):
		return self.m_lon
			
	def getAltitude(self):
		return self.m_alt
	
	def getDate(self):
		return self.m_date
			
	def getTime(self):
		return self.m_time
			
	def getDateUTC(self):
		return self.m_dateUtc
			
	def getTimeUTC(self):
		return self.m_timeUtc
			
	def getSpeedKm(self):
		return self.m_speedKm
		
	def getBatteryVolt(self):
		return self.m_batteryVolt
			
	def getBearing(self):
		return self.m_bearing
			
	def getNumberOfSatellites(self):
		return self.m_numberOfSatellites
			
	def toString(self):
		s = "lat\t" + str(self.getLatitude()) + "\n"
		s += "lon\t" + str(self.getLongitude()) + "\n"
		s += "alt\t" + str(self.getAltitude()) + "\n"
		s += "date\t" + str(self.getDate()) + "\n"
		s += "time\t" + str(self.getTime()) + "\n"
		s += "dateUTC\t" + str(self.getDateUTC()) + "\n"
		s += "timeUTC\t" + str(self.getTimeUTC()) + "\n"
		s += "speed\t" + str(self.getSpeedKm()) + "\n"
		s += "battery\t" + str(self.getBatteryVolt()) + "\n"
		s += "bearing\t" + str(self.getBearing()) + "\n"
		s += "satellites\t" + str(self.getNumberOfSatellites()) + "\n"
		
		return s

# voir:
# http://www.gpspassion.com/forumsen/topic.asp?TOPIC_ID=135468
# pour le format


	
"""
things:

0       140321190607					<serial (local date and time)>
1       +33624267358					<admin cell number>
2       GPRMC
3       180607.683						<time_utc>
4       A										<status - a or v>
5       4335.9151						<lat>
6       N										<N or S>
7       00127.1699						<lng>
8       E										<E or W>
9       0.00									<speed in knots>
10      32.59								<bearing>
11      210314							<date utc>
12											<not used>
13											<not used>
14      A*5D								<mode - A, D, E, N, S - with checksum>
15      F									<signal quality F or L>
16											<alarm - move, speed, batterie, help me! or "">
17       imei:013227007709334	<IMEI>
18      05									<number of satellites>
19      144.3								<altitude in m>
20      F:3.79V							<batterie status with voltage>
21      0										<batterie mode 0 or 1>
22      139									<number of chars until field 22>
23      21644								<some crc>
24      208									<mobile country code>
25      01									<mobile network code>
26      320F								<location area code in hex>
27      1F24								<cell id in hex>
28											<firmware info>

"""






