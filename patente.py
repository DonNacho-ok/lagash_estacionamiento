class Patente():

    def __init__(self, patente, fingreso, fegreso, total):
        self.Patente = patente
        self.FechaIngreso = fingreso
        self.FechaEgreso = fegreso
        self.TotalFacturado = total

    def setPatente(self, paten):
        self.Patente = paten

    def setFechaIngreso(self, fingre):
        self.FechaIngreso = fingre

    def setFechaEgreso(self, fegre):
        self.FechaEgreso = fegre

    def setTotalFacturado(self, tot):
        self.TotalFacturado = tot

    def getFechaEgreso(self):
        return self.FechaEgreso

    def getFechaIngreso(self):
        return self.FechaIngreso

    def getPatente(self):
        return self.Patente

    def getTotalFacturado(self):
        return self.TotalFacturado

    def toStringLite(self):
        return '{}, {}'.format(self.Patente, self.FechaIngreso)

    def toStringComplete(self):
        return '{}, {}, {}, {}'.format(self.Patente, self.FechaIngreso, self.FechaEgreso, self.TotalFacturado)
