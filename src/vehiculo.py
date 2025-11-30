class Vehiculo:
  def init(self, id):
      self.id = id
      self.pos = None
      self.vel = 0
      self.alertas = []

  def actualizar_datos(self, pos, vel):
      self.pos = pos
      self.vel = vel

  def recibir_alerta(self, alerta):
      print(f"[Vehículo {self.id}] ALERTA RECIBIDA: {alerta.mensaje}")

      print(f"[Vehículo {self.id}] -> Mostrando alerta al conductor.\n")