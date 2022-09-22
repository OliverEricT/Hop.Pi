import time
import json
import requests
import logging
import sys
import os
import glob

class TempSensor():
	SENSOR_DS18B20 = "ds18b20"
	SENSOR_HTTP = "http"
	DEGREES = "°"

	@property
	def SensorProtocol(self):
		return self._sensorProtocol

	@SensorProtocol.setter
	def SensorProtocol(self,val):
		self._sensorProtocol = val

	@property
	def SensorId(self):
		return self._sensorId

	@SensorId.setter
	def SensorId(self,val):
		self._sensorId = val

	@property
	def SensorUrl(self):
		return self._sensorUrl

	@SensorUrl.setter
	def SensorUrl(self,val):
		self._sensorUrl = val

	@property
	def IsMetric(self):
		return self._IsMetric

	@IsMetric.setter
	def IsMetric(self,val):
		self._IsMetric = val

	@property
	def Logger(self):
		return self._logger

	@Logger.setter
	def Logger(self,val):
		self._logger = val

	@property
	def Temperature(self):
		if self.SensorProtocol == self.SENSOR_HTTP:
			return self._GetTemperatureByHttp()
		else:
			return self.ReadDS18B20Sensor(self.SensorId)

	@property
	def Fahrenheit(self):
		if self.IsMetric:
			return self.ToFahrenheit(self.Temperature)
		else:
			return self.Temperature

	@property
	def Celsius(self):
		if self.IsMetric:
			return self.Temperature
		else:
			return self.ToCelsius(self.Temperature)

	def __init__(self, sensor_protocol=None, sensor_id=None, sensor_url=None, isMetric=False):
		"""
		"""
		self.Logger = logging.getLogger(__name__)
		self.Logger.info("beertemps initializing")

		self.SensorProtocol = sensor_protocol
		if self.SensorProtocol == self.SENSOR_DS18B20:
			os.system('modprobe w1-gpio')
			os.system('modprobe w1-therm')
			if sensor_id is None: 
				self.SensorId = self.GetDS18B20SensorIds()[0] # if user does not specify, just pick the first one.
			else:
				self.SensorId = sensor_id
		elif self.SensorProtocol != self.SENSOR_HTTP:
			self.Logger.error("Configuration error. temperature sensor_protocol must map to DS18B20 or HTTP")
			sys.exit(1)

		self.SensorUrl = sensor_url
		self.IsMetric = isMetric

	def _GetTemperatureByHttp(self):
		try:
			r = requests.get(self.SensorUrl)
			if r.status_code == 200:
				if self.IsMetric:
					return r.text
				else:
					return self.ToFahrenheit(int(r.text))
			else:
				self.Logger.error("error: temperature sensor received http_code %i" % r.status_code)
		except:
			self.Logger.error("Temperature. Unable to get temperature from sensor_url: %s" % self.sensor_url)

	def ToFahrenheit(self,temperature):
		return (temperature * 9.0 / 5.0 + 32.0)

	def ToCelsius(self,temp):
		return ((temp - 32) / 1.80000)

	def ReadDS18B20Sensor(self,sensor_id):
		lines = self.ReadTempRaw(sensor_id)
		return self.ProcessRawDS18B20Data(lines, sensor_id)

	def GetDS18B20SensorIds(self):
		base_dir = '/sys/bus/w1/devices/'
		NUM_SENSORS = len(glob.glob(base_dir + '28*'))
		sensor_ids=[]
		for x in range(0,NUM_SENSORS):
			device_folder = glob.glob(base_dir + '28*')[x]
			id = device_folder.replace("/sys/bus/w1/devices/",'')
			sensor_ids.append(id)
			self.Logger.info("discovered sensor id %s " % str(id))
		return sensor_ids

	def ProcessRawDS18B20Data(self, lines, sensor_id):
		while lines[0].strip()[-3:] != 'YES': # TODO: wtf is this shit
			time.sleep(0.2)
			lines = self.read_temp_raw(sensor_id)
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			if self.IsMetric:
				return temp_c
			else:
				return self.ToFahrenheit(temp_c)

	def ReadTempRaw(self, sensor_id):
		base_dir = '/sys/bus/w1/devices/'
		device_folder = glob.glob(base_dir + sensor_id)[0]
		device_file = device_folder + '/w1_slave'
		f = open(device_file, 'r')
		lines = f.readlines()
		f.close()
		return lines

def Main():
	t = TempSensor(sensor_protocol="ds18b20")
	print("Read in: %s " % str(t.Temperature()))

if __name__ == "__main__":
	Main()