from odoo import models, fields

class Profesor(models.Model):
    _inherit = 'res.partner'

    materia_ids = fields.Many2many('materia', string='Materias Impartidas')
