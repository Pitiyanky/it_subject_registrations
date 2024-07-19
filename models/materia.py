from odoo import models, fields

class Materia(models.Model):
    _name = 'materia'
    _description = 'Materia'

    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción')
    creditos = fields.Integer('Créditos')
    profesor_ids = fields.Many2many('res.partner', string='Profesores', domain=[('tipo', '=', 'profesor')])
