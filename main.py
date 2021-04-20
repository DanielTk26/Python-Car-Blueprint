class Car(object):
  
  def __init__(self, model, color, speed_limit):
      self.color = color
      self.company = company
      self.speed_limit = speed_limit
      self.model = model

  def start(self):
      print("Started")
  
  def stop(self):
      print("Stopped")
 
  def accelerate(self):
      print("Accelarating...")
      "accelarator functionality here"

  def change_gear(self, gear_type):
      print("Gear Changed")
      "gear related functionality here"


audi = Car("A6", "red", "audi", 80)

print (audi.start())