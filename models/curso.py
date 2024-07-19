from odoo import models, fields, api
from odoo.exceptions import UserError

class Curso(models.Model):
    _name = 'curso'
    _inherit = 'product.template'
    _description = 'Modelo que registra los cursos que se imparten en la institución'

    profesor_ids = fields.Many2many('res.partner', 
                                    relation='curso_profesor_rel',  # Tabla intermedia para profesores
                                    column1='curso_id', 
                                    column2='profesor_id',
                                    string='Profesor',
                                    domain=[('tipo', '=', 'profesor')])


    alumnos_ids = fields.Many2many('res.partner', 
                                    relation='curso_alumno_rel',  # Tabla intermedia para alumnos
                                    column1='curso_id', 
                                    column2='alumno_id',
                                    string='Alumnos', domain=[('tipo', '=', 'alumno')])
    
    materia_ids = fields.Many2many('materia', string='Materias')
    horario_ids = fields.One2many('horario', 'curso_id', string='Horarios')
    # Campos adicionales que podrías necesitar
    fecha_inicio = fields.Date('Fecha de Inicio')
    fecha_fin = fields.Date('Fecha de Fin')
    capacidad_maxima = fields.Integer('Capacidad Máxima')

    #No permitira que hayan mas alumnos que la capacidad maxima del curso
    @api.constrains('alumnos_ids', 'capacidad_maxima')
    def _check_capacidad_maxima(self):
        for curso in self:
            if curso.alumnos_ids and curso.capacidad_maxima:
                if len(curso.alumnos_ids) > curso.capacidad_maxima:
                    raise UserError("Se ha excedido la capacidad máxima de alumnos para este curso.")
    
    @api.model
    def create(self, vals):
        # Crear el registro en product.template sin crear variantes de product.product
        context = dict(self.env.context, create_product_product=False)
        return super(Curso, self.with_context(context)).create(vals)

    def write(self, vals):
        # Escribir en product.template sin crear variantes de product.product
        context = dict(self.env.context, create_product_product=False)
        return super(Curso, self.with_context(context)).write(vals)

class Horario(models.Model):
    _name = 'horario'
    _description = 'Horario de Curso'

    curso_id = fields.Many2one('curso', string='Curso', required=True)  # Corregido
    dia_semana = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo')
    ], string='Día de la Semana', required=True)
    hora_inicio = fields.Float('Hora de Inicio', required=True)
    hora_fin = fields.Float('Hora de Fin', required=True)
    numero_salon = fields.Char('Número de Salón')