from odoo import models, fields

class ContactoTipo(models.Model):
    _inherit = 'res.partner'
    #Usado unicamnete para separa alumnos de profesores
    tipo = fields.Selection([
        ('alumno', 'Alumno'),
        ('profesor', 'Profesor'),
        ('otro', 'Otro')
    ], string='Tipo de Contacto', default='otro')
