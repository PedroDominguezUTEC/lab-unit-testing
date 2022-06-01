# Formato: DD-MM-YYYY
import datetime


class DateFormatException(Exception):
  pass


class DateException(Exception):
  pass


class Verificador:
  def __init__(self, f_nacimiento, f_consulta):
    self.f_nacimiento = self.__respeta_formato(f_nacimiento)
    self.f_consulta = self.__respeta_formato(f_consulta)
    
  def __respeta_formato(self, fecha_string):
    temp = fecha_string.split('-')
    if len(temp) != 3:
      raise DateFormatException("Tienes que ingresar 3 valores")
    
    for i in range(3):
      try:
        temp[i] = int(temp[i])
      except ValueError:
        raise DateFormatException("Las fechas no son números")
      
    try:
      temp = datetime.date(temp[2], temp[1], temp[0])
    except ValueError:
      raise DateFormatException("La fecha no existe")

    return temp
  
    
  def determinar_mayoria_edad(self):
    f_nacimiento = self.f_nacimiento
    f_consulta = self.f_consulta
    
    if self.f_nacimiento > self.f_consulta:
      raise DateException
    
    dias = (f_consulta - f_nacimiento).days
    
    if  dias//365 > 17:
      return True
    return False