# -*- coding: utf-8 -*-
{
    'name': "it_subject_registrations",

    'summary': """
        Módulo para Gestión de Inscripciones de Alumnos en Odoo
       """,

    'description': """
        Modulo para gestionar inscripciones de nuevos alumnos en un sistema educativo. 
       El módulo permitirá la creación de inscripciones, la gestión de alumnos, materias, cursos y profesores.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/it_subject_registrations_security.xml',
        'security/ir.model.access.csv',
        'views/alumno.xml',
        'views/curso.xml',
        'views/inscripcion.xml',
        'views/materia.xml',
        'views/profesor.xml',
        'views/horario.xml',
        'views/menus.xml',
    ],
}
