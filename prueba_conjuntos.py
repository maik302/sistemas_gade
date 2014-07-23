#! /usr/bin/env python
# -*- encoding: utf-8 -*-

###
#
# prueba_conjuntos.py
# Pruebas sobre el tipo conjuntos de python. Previo al sistema de cuadre de
# horarios.
#
# @author : Michael Woo
#
###

# Clase que define un horario: Dia y Hora.
class horario:
    def __init__(self,dia,hora):
    # Verificaciones:
    # - dia pertence al conjunto de dias disponibles
    # - hora esta entre [1,10]
        self.dia = dia
        self.hora = hora

    def __str__(self):
        representacion = "Horario: Día - "+str(self.dia)+";"
        representacion += " Hora - "+str(self.hora)
        return representacion
        
# Diccionario que define el horario total disponible. El conjunto Universo - U.
U = { 'lun1' : horario('LUN',1),
      'lun2' : horario('LUN',2),
      'lun3' : horario('LUN',3),     
      'lun4' : horario('LUN',4),
      'lun5' : horario('LUN',5),
      'lun6' : horario('LUN',6),
      'lun7' : horario('LUN',7),
      'lun8' : horario('LUN',8),
      'lun9' : horario('LUN',9),
      'lun10' : horario('LUN',10),

      'mar1' : horario('MAR',1),
      'mar2' : horario('MAR',2),
      'mar3' : horario('MAR',3),     
      'mar4' : horario('MAR',4),
      'mar5' : horario('MAR',5),
      'mar6' : horario('MAR',6),
      'mar7' : horario('MAR',7),
      'mar8' : horario('MAR',8),
      'mar9' : horario('MAR',9),
      'mar10' : horario('MAR',10),

      'mie1' : horario('MIE',1),
      'mie2' : horario('MIE',2),
      'mie3' : horario('MIE',3),     
      'mie4' : horario('MIE',4),
      'mie5' : horario('MIE',5),
      'mie6' : horario('MIE',6),
      'mie7' : horario('MIE',7),
      'mie8' : horario('MIE',8),
      'mie9' : horario('MIE',9),
      'mie10' : horario('MIE',10),

      'jue1' : horario('JUE',1),
      'jue2' : horario('JUE',2),
      'jue3' : horario('JUE',3),     
      'jue4' : horario('JUE',4),
      'jue5' : horario('JUE',5),
      'jue6' : horario('JUE',6),
      'jue7' : horario('JUE',7),
      'jue8' : horario('JUE',8),
      'jue9' : horario('JUE',9),
      'jue10' : horario('JUE',10),

      'vie1' : horario('VIE',1),
      'vie2' : horario('VIE',2),
      'vie3' : horario('VIE',3),     
      'vie4' : horario('VIE',4),
      'vie5' : horario('VIE',5),
      'vie6' : horario('VIE',6),
      'vie7' : horario('VIE',7),
      'vie8' : horario('VIE',8),
      'vie9' : horario('VIE',9),
      'vie10' : horario('VIE',10)
    }

if __name__ == '__main__':

    x = { 'lun1' : horario('LU',1),
          'mar1' : horario('MA',1),
          'mie1' : horario('MI',1)
        }
    x1 = horario('LU',1)
    x2 = horario('MA',3)
    x3 = horario('LU',1)
    x4 = horario('VI',7)

    c1 = set([x['lun1'],x['mar1']])
    c2 = {x['lun1']}

    print("Conjunto1")
    for i in c1:
        print(i)

    print("Conjunto2")
    for i in c2:
        print(i)

    print("Diccionario")
    for i in x.itervalues():
        print(i)

    #NOTA: La interseccion solo trabaja con instancias.
    print("Interseccion")
    for i in (c1 & c2):
        print(i)
