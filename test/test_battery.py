from modulo import Modulo
from datetime import datetime
import csv
import time

boat = Modulo('192.168.1.100')
battery = boat.battery

with open('battery.csv', 'w', newline='') as csvfile:
  fieldnames = ['datetime', 'percentage', 'voltage','capacity', 'current', 'remaining_sec']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  try:
    while True:
      data = {
        'datetime': datetime.now(),
        'percentage': battery.percentage,
        'voltage': battery.voltage,
        'capacity': battery.capacity,
        'current': battery.current,
        'remaining_sec': battery.remaining_sec
      }
      writer.writerow(data)
      print(data)
      print()
      time.sleep(60)
  except KeyboardInterrupt:
    pass