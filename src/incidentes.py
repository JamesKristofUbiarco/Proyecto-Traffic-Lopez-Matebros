class Incidente:
  def init(self, tipo, pos):
      self.tipo = tipo
      self.pos = pos
      self.mensaje = ""

  def tunel(self): # verificar donde hay tuneles
    tunel1={"inicio_x":10, "inicio_y":10, "fin_x":20, "fin_y":20,"nombre":"Tunel Sur"}
    tunel2={"inicio_x":50, "inicio_y":22, "fin_x":65, "fin_y":30,"nombre":"Tunel Norte"}
    tuneles=[tunel1,tunel2]
    for t in tuneles:
      if self.pos[1]>=t["inicio_y"] and self.pos[1]<=t["fin_y"] and self.pos[0]>=t["inicio_x"] and self.pos[0]<=t["fin_x"]:
        return  t["nombre"]
      else:
        return "No se"
  def generar_alerta(self):
      pass



class Accidente(Incidente):
  def init(self, tipo, ubicacion):
      super().init(tipo, ubicacion)
  def generar_alerta(self):
      self.mensaje = "¡ALERTA DE ACCIDENTE! Tipo: " + self.tipo
      T_in=super().tunel()
      if "tunel" in T_in.lower():
          self.mensaje += " Instrucción: Encienda luces y vaya con cuidado"
      return self.mensaje


class CondicionVial(Incidente):
    def init(self, tipo, ubicacion):
        super().init(tipo, ubicacion)
    def generar_alerta(self):
        self.mensaje = "¡PRECAUCIÓN VIAL! Detalle: " + self.tipo
        T_in=super().tunel()
        if "tunel" in T_in.lower():
            self.mensaje += " Instrucción: Encienda luces y revise el camino con cuidado"
        return self.mensaje


class Trafico(Incidente):
    def init(self, tipo, ubicacion):
        super().init(tipo, ubicacion)

    def generar_alerta(self):
        base = "ALERTA DE TRÁFICO: " + self.tipo
        T_in=super().tunel()
        if "tunel" in T_in.lower():
            base += " Instrucción: Encienda luces y apague motor si la detención es larga."

        self.mensaje = base
        return self.mensaje


class AlertaConductor(Incidente):
    def init(self, vel):
        self.vel = vel


    def generar_alerta(self):
        self.mensaje = f"EXCESO DE VELOCIDAD: {self.vel} km/h"
        return self.mensaje
