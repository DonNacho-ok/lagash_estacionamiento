from datetime import datetime
from datetime import timedelta
import patente

"""
datetimeobj2 = datetime(2019, 12, 8, 15, 30, 0)
timestamp = datetimeobj.strftime("%d-%m-%Y %H:%M:%S")
timestamp2 = datetimeobj2.strftime("%d-%m-%Y %H:%M:%S")
diff = datetimeobj2 - datetimeobj
print(diff)
horas = ((diff.total_seconds())/60)//60
print(horas)
facturado= 115 * horas
print(facturado)
"""
datetimeobj = datetime.now()
datetimeobj2 = datetime(2019, 12, 8, 15, 30, 0)

unaPatente = patente.Patente("XSW-985", datetimeobj, "", 0)

lista_patentes = []

lista_patentes.append(unaPatente)
print(lista_patentes[0])
print(lista_patentes[0].toStringLite())
lista_patentes[0].setFechaEgreso(datetimeobj2)
print(lista_patentes[0].toStringComplete())
diff = (lista_patentes[0].getFechaEgreso() - lista_patentes[0].getFechaIngreso())
totalhoras = ((diff.total_seconds()/60)//60)
print(totalhoras)
factura = ((diff.total_seconds()/60)//60) * 115
lista_patentes[0].setTotalFacturado(factura)
print(lista_patentes[0].toStringComplete())
