from modulo import Modulo

boat = Modulo('127.0.0.1')

message = None
while True:
  if message != boat.gps.get_message():
    message = boat.gps.get_message()
    print(message)