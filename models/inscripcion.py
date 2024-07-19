from odoo import models, fields, api

class Inscripcion(models.Model):
    _name = 'inscripcion'
    _description = 'Inscripción'

    alumno_id = fields.Many2one('res.partner', string='Alumno', domain=[('tipo', '=', 'alumno')], required=True)
    curso_id = fields.Many2one('curso', string='Curso', required=True)
    fecha_inscripcion = fields.Date('Fecha de Inscripción', default=fields.Date.today)

    state = fields.Selection(selection=[
       ('draft', 'Borrador'),
        ('done', 'Confirmada'),
        ('cancel', 'Cancelada')
   ], string='Estado', required=True, readonly=True, copy=False,
   tracking=True, default='draft')
    
    @api.model
    def create(self, vals):
        res = super(Inscripcion, self).create(vals)
        if res.state == 'done':
            res.curso_id.alumnos_ids = [(4, res.alumno_id.id)]
        return res

    def write(self, vals):
        res = super(Inscripcion, self).write(vals)
        for inscripcion in self:
            if inscripcion.state == 'done':
                inscripcion.curso_id.alumnos_ids = [(4, inscripcion.alumno_id.id)]
            else:
                inscripcion.curso_id.alumnos_ids = [(3, inscripcion.alumno_id.id)]
        return res

    def action_confirmar(self):
        self.write({'state': 'done'})

    def action_cancelar(self):
        self.write({'state': 'cancel'})

    def action_borrador(self):
        self.write({'state': 'draft'})