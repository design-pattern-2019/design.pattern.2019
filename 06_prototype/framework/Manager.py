class Manager:
  __showcase = {}

  def register(self, name, proto):
    self.__showcase[name] = proto

  def create(self, protoname):
    p = self.__showcase[protoname]
    return p.createClone()