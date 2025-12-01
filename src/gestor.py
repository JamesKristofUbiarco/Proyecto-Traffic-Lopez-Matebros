from src.vehiculo import Vehiculo
from src.incidentes import Accidente, CondicionVial, Trafico, AlertaConductor

class GestorAvenida: #A estudiar
  def __init__(self):
      self.vehiculos = {}
      self.incidentes = []

  def actualizar_vehiculo(self,id_vehiculo ,pos, vel):
      # Nuevo vehiculo
      if id_vehiculo not in self.vehiculos:
        self.vehiculos[id_vehiculo] = Vehiculo(id_vehiculo)


      v = self.vehiculos[id_vehiculo]
      v.actualizar_datos(pos, vel)

      # Exceso de velocidad
      if vel > 80:   # cambiar dependiendo
          alerta = AlertaConductor(vel)
          alerta.generar_alerta()
          v.recibir_alerta(alerta)

  def reportar_incidente(self, tipo, ubicacion):
      if tipo.lower() in ["choque", "volcadura", "derrame"]:
          incidente = Accidente(tipo, ubicacion)
      elif tipo.lower() in ["bache", "obstrucción", "obstruccion"]:
          incidente = CondicionVial(tipo, ubicacion)
      else:
          incidente = Trafico(tipo, ubicacion)

      # Guardar incidente
      self.incidentes.append(incidente)

      # Generar alerta
      mensaje = incidente.generar_alerta()

      # Encontrar vehículos cercanos
      for v in self.vehiculos.values():#Limitar un poco el avisa
          v.pos[0]
          if (v.pos[0]>=ubicacion[0]-100 and v.pos[0]<=ubicacion[0]+100 and v.pos[1]>=ubicacion[1]-100 and v.pos[1]<=ubicacion[1]+100):

            v.recibir_alerta(incidente)
            continue


      return mensaje