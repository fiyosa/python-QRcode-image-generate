from json import load

class setup:
  def __init__(self):
    try:
      with open('system.json') as f:
        data = load(f)
        cek_system = 1
        if (len(data) == 10):
          for x in data:
            if not x in ["sn", "digit", "loop", "start", "stop", "port", "pic_text", "computer", "test", "test_sn"]:
              cek_system = 0
        else:
          cek_system = 0
        self.data = data
        self.cek_system = cek_system
    except:
      self.cek_system = 0
  
  def check(self):
    return self.cek_system

  def system(self):
    return self.data
      
# if __name__ == "__main__":
#   setup = setup()
#   print(setup.check())
#   system = setup.system()
#   print(system['digit'])
