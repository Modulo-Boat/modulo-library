from geographiclib.geodesic import Geodesic
from modulo import Modulo

def get_bearing(boat_lat, boat_long, dest_lat, dest_long)
 return Geodesic.WGS84.Inverse(boat_lat, boat_long, boat_lat, boat_long)['azi1']

def calculate_angle(heading, bearing):
  diff = bearing - heading
  if diff < 0:
    return calculate_angle(heading, bearing+360)
  if diff > 360:
    return calculate_angle(heading+360, bearing)
  if diff > 180:
    return diff - 360
  return diff

def main():
  boat = Modulo('192.168.1.109')
  gps = boat.gps
  imu = boat.imu

  while True:
    print(
      calculate_angle(
        imu.heading, get_bearing(gps.latitude, gps.longitude)
      )
    )
    