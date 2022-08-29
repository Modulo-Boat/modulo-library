import redis
import json

class Imu():
  def __init__(self, redis):
    self.redis = redis
    self.accelerometer = self.Accelerometer()
    self.gyroscope = self.Gyroscope()
    self.compass = self.Compass()

    pubsub = self.redis.pubsub()
    pubsub.subscribe(**{'imu_accelerometer': self.accelerometer.update})
    pubsub.subscribe(**{'imu_gyroscope': self.gyroscope.update})
    pubsub.subscribe(**{'imu_compass': self.compass.update})
    thread = pubsub.run_in_thread(sleep_time=0.001)
  
  class Accelerometer():
    def __init__(self):
      self.x, self.y, self.z = None, None, None
      self.pitch, self.roll = None, None

    def update(self, message):
      data = json.loads(message['data'].decode('utf8').replace("'", '"'))
      self.x = data['x']
      self.y = data['y']
      self.z = data['z']
      self.pitch = data['pitch']
      self.roll = data['roll']
  
    @property  
    def dict(self):
      return {'x': self.x, 'y': self.y, 'z': self.z, 'pitch': self.pitch, 'roll': self.roll}

  class Gyroscope():
    def __init__(self):
      self.x, self.y, self.z = None, None, None

    def update(self, message):
      data = json.loads(message['data'].decode('utf8').replace("'", '"'))
      self.x = data['x']
      self.y = data['y']
      self.z = data['z']
    
    @property  
    def dict(self):
      return {'x': self.x, 'y': self.y, 'z': self.z}

  class Compass():
    def __init__(self):
      self.x, self.y, self.z = None, None, None
      self.heading = None

    def update(self, message):
      data = json.loads(message['data'].decode('utf8').replace("'", '"'))
      self.x = data['x']
      self.y = data['y']
      self.z = data['z']
      self.heading = data['heading']
    
    @property  
    def dict(self):
      return {'x': self.x, 'y': self.y, 'z': self.z, 'heading': self.heading}


      