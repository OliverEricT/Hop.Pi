import time
import random
import logging
import RPI.GPIO as GPIO
import logging
import requests
### Begin. These probably need to be pulled.
# import beer_db
# import twitter_notify
# import slack_notify
# import ConfigParser
# import zope.event
### End

"""
Flowmeter code for BOOZER
"""

logger = logging.getLogger(__name__)
GPIO.setmode(GPIO.BCM)  # use real GPIO numbering

class FlowMeter():
  # Constants
	POUR_RESET = 1
	POUR_FULL = 3
	POUR_UPDATE = 5
	PINTS_IN_A_LITER = 2.11338
	SECONDS_IN_A_MINUTE = 60
	MS_IN_A_SECOND = 1000.0
	MINIMUM_POUR_VOL_LBL = "minimum_pour_vol"
	STANDALONE_MODE = False

	#################
	#    Members    #
	#################
	@property
	def MinimumPourVol(self):
		return self._minimum_pour_vol

	@MinimumPourVol.setter
	def MinimumPourVol(self, val = 0.075):
		self._minimum_pour_vol = val
	
	# _minimum_pour_vol = 0.23 ## This is the minimum amount of volume to be poured before it is registered as a complete pour.
	
	@property
	def IsMetric(self):
		return self._isMetric

	@IsMetric.setter
	def IsMetric(self,val = True):
		self._isMetric = val

	@property
	def Beverage(self):
		return self._beverage

	@Beverage.setter
	def Beverage(self,val = 'beer'):
		self._beverage = val

	@property
	def Enabled(self):
		return self._enabled

	@Enabled.setter
	def Enabled(self,val = True):
		self._enabled = val
	
	@property
	def Clicks(self):
		return self._clicks

	@Clicks.setter
	def Clicks(self,val = 0):
		self._clicks = val

	@property
	def LastClick(self):
		return self._lastClick

	@LastClick.setter
	def LastClick(self,val = 0):
		self._lastClick = val
	
	@property
	def Flow(self):
		return self._flow

	@Flow.setter
	def Flow(self,val = 0.0):
		self._flow = val

	
	@property
	def ThisPour(self):
		if (self.IsMetric):
			return round(self.ThisPour, 3)
		else:
			return round(self.thisPour * self.PINTS_IN_A_LITER, 3)

	@ThisPour.setter
	def ThisPour(self,val = 0.0):
		"""
		Sets the ThisPour variable
		:param val: volume in liters poured
		"""
		self._thisPour = val

	@property
	def TotalPour(self):
		return self._totalPour

	@TotalPour.setter
	def TotalPour(self,val = 0.0):
		"""
		Sets the TotalPour variable
		:param val: volume in liters poured
		"""
		self._totalPour = val

	@property
	def TapId(self):
		return self._tapId

	@TapId.setter
	def TapId(self,val = 0):
		self._tapId = val
	
	@property
	def Pin(self):
		return self._pin

	@Pin.setter
	def Pin(self,val = -1):
		self._pin = val

	@property
	def PreviousPour(self):
		return self._previous_pour

	@PreviousPour.setter
	def PreviousPour(self,val = 0.0):
		self._previous_pour = val

	@property
	def Config(self):
		self._config

	@Config.setter
	def Config(self,val = False):
		self._config = val
	
	@property
	def LastEventType(self):
		return self._lastEventType

	@LastEventType.setter
	def LastEventType(self,val = POUR_RESET):
		self._lastEventType = val

	@property
	def Logger(self):
		return self._logger

	@Logger.setter
	def Logger(self,val = logging.getLogger(__name__)):
		self._logger = val

	def __init__(self, isMetric, beverage, tap_id, pin, config, capacity=5, STANDALONE_MODE=False, minimum_pour_vol=None):
		"""
		Initializes the FlowMeter object.
		:param isMetric: metric or not?
		:param beverage: name of the beverage passing through the line
		:param tap_id: how shall i identify myself?
		:param pin: the GPIO pin to listen on
		"""
		self.IsMetric = isMetric
		self.Beverage = beverage
		self.Clicks = 0
		self.LastClick = int(time.time() * self.MS_IN_A_SECOND)
		self.Flow = 0.0
		self.ThisPour = 0.0
		self.TotalPour = 0.0
		self.Enabled = True
		self.TapId = tap_id
		self.Pin = pin
		self.Capacity = capacity
		self.Config = config # TODO: find a way to pull this out and make it decoupled from the config object
		self.STANDALONE_MODE = STANDALONE_MODE # TODO: change this since we shouldn't be updating a constant

		#TODO: Change this
		if minimum_pour_vol is not None:
			self.minimum_pour_vol = minimum_pour_vol

		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	def Update(self, currentTime=int(time.time() * MS_IN_A_SECOND)):
		"""Sets a timestamp of the last pour event.
		:param currentTime: timestamp of a long
		"""
		self.Clicks += 1
		# get the time delta
		clickDelta = max((currentTime - self.LastClick), 1)
		# calculate the instantaneous speed
		if (self.Enabled and clickDelta < 1000):
			hertz = self.MS_IN_A_SECOND / clickDelta

			flow = hertz / (self.SECONDS_IN_A_MINUTE * 7.5)  # In Liters per second
			instPour = (flow * (clickDelta / self.MS_IN_A_SECOND))  # * 1.265 #1.265

			self.ThisPour += instPour
			self.TotalPour += instPour
		# Update the last click
		self.LastClick = currentTime

		# Log it
		# logger.info("event-bus: registered tap " + str(self.get_tap_id()) + " successfully")
		self.Logger.info("Tap[%i] Pour Event: %s pints." %( self.TapId, str(round(self.TotalPour,3))))

	#TODO: Potentially change this up
	def ResetPourStatus(self):
		"""
		This will reset a pour to a cleared event. this is needed to properly track what beer has already been registered in the database.
		"""
		self.LastEventType = self.POUR_RESET

	def Clear(self):
		"""
		Clears an event.
		:return: nada
		"""
		self.thisPour = 0
		self.totalPour = 0

	def ListenForPour(self):
		"""
		"""
		currentTime = int(time.time() * self.MS_IN_A_SECOND)
		
		#TODO: Look into this function when parts arrive
		if self.ThisPour > 0.0:
			pour_size = round(self.ThisPour * self.PINTS_IN_A_LITER, 3)
			pour_size2 = round(self.ThisPour * self.PINTS_IN_A_LITER,2)  # IDK what is going on here but it works and I am afraid to break it
			if pour_size != self.PreviousPour:
				logger.debug(
					"Tap: %s\t Poursize: %s vs %s" % (str(self.TapId), str(pour_size), str(self.PreviousPour)))
				if pour_size2 < 0.05:
					return # ignore small events
				self.PreviousPour = pour_size
				self.LastEventType = self.POUR_UPDATE # set last event status for event bus in boozer

			## Test if the pour is above the minimum threshold and if so, register and complete the pour action.
			if (self.ThisPour > self.MinimumPourVol and currentTime - self.LastClick > 10000):  # 10 seconds of inactivity causes a tweet
				self.Logger.info("--- REGISTERING-FULL-POUR   %s vs %s " % (str(self.ThisPour), str(self.MinimumPourVol)) ) 
				self.RegisterNewPour(currentTime)
				self.LastEventType = self.POUR_FULL # set last event status for event bus in boozer
			else:
				logger.debug("--- Pour -> %s vs Threshold -> %s " % (str(self.ThisPour), str(self.MinimumPourVol)) ) 

			#TODO: Potentially remove this since I don't think we really need an event bus and I don't know what zope is
			zope.event.notify(self) # notify the boozer event bus that a new pour has been registered. 
								# it will check 'last_event_type' to decide to kick off actions related to a full pour up just update the database for a half/min pour.

	def RegisterNewPour(self, currentTime):
		"""
		"""
		# reset the counter
		self.ThisPour = 0.0

		# display the pour in real time for debugging
		if self.ThisPour > 0.05: self.Logger.debug("[POUR EVENT] " + str(self.TapId) + ":" + str(self.ThisPour))

		# reset flow meter after each pour (2 secs of inactivity)
		if (self.ThisPour <= self.MinimumPourVol and currentTime - self.LastClick > 2000): self.ThisPour = 0.0


def Main():
	# bring in config
	CONFIG_FILE = "./config.ini"
	config = ConfigParser.ConfigParser()
	config.read(CONFIG_FILE)
	# setup logging
	# do it
	testTapId = 4
	testTapGpioPin = 13
	test_tap = FlowMeter("not metric", "FlowmeterTestBeer", tap_id=testTapId, pin=testTapGpioPin, config=config, STANDALONE_MODE=True)

	logger = logging.getLogger()
	handler = logging.StreamHandler()
	formatter = logging.Formatter(
		'%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(logging.DEBUG)
	logger.setLevel(logging.INFO)

	# setup the flowmeter event bus
	GPIO.add_event_detect(test_tap.Pin, GPIO.RISING, callback=lambda *a: test_tap.Update(), bouncetime=20)
	logger.info("flowmeter.py listening for pours")
	while True:
		test_tap.ListenForPour()
		time.sleep(0.01)

# it's go time.
if __name__ == "__main__":
	Main()