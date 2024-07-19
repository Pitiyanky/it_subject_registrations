from odoo import models, fields, api
from datetime import date, timedelta

class Alumno(models.Model):
    _inherit = 'res.partner'

    fecha_nacimiento = fields.Date('Fecha de Nacimiento')
    edad = fields.Integer(compute='_calcular_edad', string='Edad', store=True)
    
    @api.depends('fecha_nacimiento')
    def _calcular_edad(self):
        for alumno in self:
            hoy = date.today()
            nacimiento = alumno.fecha_nacimiento
            if nacimiento:  # Verificar si la fecha de nacimiento está definida
                edad_dias = hoy - nacimiento
                alumno.edad = edad_dias // timedelta(days=365)  # Divide los días por 365 para obtener años
            else:
                alumno.edad = 0
