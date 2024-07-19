# Módulo de Gestión de Inscripciones en Odoo 15

Este módulo permite gestionar inscripciones de alumnos, cursos, materias, profesores y horarios en un sistema educativo.

## Características Principales

*   **Gestión de Alumnos:** Registro y seguimiento de información de los alumnos.
*   **Gestión de Cursos:** Creación y administración de cursos, incluyendo materias, horarios y profesores asignados.
*   **Gestión de Materias:** Definición de materias con sus créditos y profesores asociados.
*   **Gestión de Profesores:** Registro y seguimiento de información de los profesores.
*   **Gestión de Inscripciones:** Proceso de inscripción de alumnos en cursos, con seguimiento del estado de las inscripciones.
*   **Gestión de Horarios:** Creación de horarios detallados para cada curso, con días, horas y salones.
*   **Seguridad Avanzada:** Control de acceso granular para diferentes roles (administrador, secretaria, profesor, alumno).

## Instalación

1.  **Descargar el Módulo:** Clona o descarga este repositorio en tu equipo.
2.  **Agregar al Addons Path:** Coloca la carpeta del módulo en el directorio `addons` de tu instancia de Odoo.
3.  **Actualizar la Lista de Módulos:** En Odoo, ve a "Aplicaciones" y haz clic en "Actualizar lista de módulos".
4.  **Instalar el Módulo:** Busca el módulo "Gestión de Inscripciones" y haz clic en "Instalar".

## Configuración

1.  **Asignar Usuarios a Grupos:**
    1.  **Asignar Usuarios a Grupos:**
        *   Edita cada usuario en Odoo y asígnalo a uno de los siguientes grupos según su rol:
        *   **Administrador de Educación:** Acceso completo a todas las funcionalidades del módulo.
        *   **Secretaría:** Puede gestionar alumnos, inscripciones y ver información de cursos, materias, profesores y horarios.
        *   **Profesor:** Puede ver información de alumnos, cursos, materias y horarios, y modificar sus propios datos y los horarios de sus cursos.
        *   **Alumno:** Puede ver información de cursos, materias y sus propias inscripciones, y modificar sus propios datos.

## Permisos y Acciones por Grupo

| Grupo de Usuarios           | Permisos                                                                                                                                                                                                                                                                                       | Acciones                                                                                                                                                                                                                                                                                           |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Administrador de Educación | Acceso completo a todos los modelos (alumnos, profesores, cursos, materias, inscripciones, horarios).                                                                                                                                                                                             | Puede crear, leer, modificar y eliminar cualquier registro en todos los modelos.                                                                                                                                                                                                               |
| Secretaría                  | Lectura de todos los modelos. Creación, lectura y modificación  de alumnos, cursos, profesores e inscripciones.                                                                                                                                                                                             | Puede gestionar la información de los alumnos e inscripciones. Puede ver la información de cursos, materias, profesores y horarios, y modificarlos, pero no eliminarlos.                                                                                                                                     |
| Profesor                   | Lectura de todos los modelos. Modificación de los horarios de sus cursos.                                                                                                                                                                                          | Puede ver la información de cursos, materias y horarios. Puede editar su propia información de contacto, las materias que imparte y los horarios de sus cursos.                                                                                                                             |
| Alumno                    | Lectura de cursos, materias y sus propias inscripciones.                                                                                                                                                                                            | Puede ver la información de los cursos disponibles, las materias que se imparten y los horarios.                                                    |


## Uso

1.  **Alumnos:**
    *   Crea nuevos alumnos en el menú "Contactos" -> "Alumnos".
    *   Inscribe alumnos en cursos desde el menú "Inscripciones".
2.  **Profesores:**
    *   Crea nuevos profesores en el menú "Contactos" -> "Profesores".
    *   Asigna profesores a cursos y materias.
3.  **Cursos:**
    *   Crea nuevos cursos en el menú "Cursos".
    *   Asigna materias, profesores y horarios a cada curso.
4.  **Materias:**
    *   Crea nuevas materias en el menú "Materias".
    *   Asigna profesores a cada materia.
5.  **Horarios:**
    *   Crea horarios para cada curso en el menú "Horarios".

## Consideraciones

*   Este módulo utiliza el modelo `res.partner` para almacenar información de alumnos y profesores.
*   Los cursos se gestionan como productos en Odoo, lo que te permite aprovechar funcionalidades como precios e inventario.
*   El módulo incluye reglas de seguridad para controlar el acceso a los diferentes modelos y acciones según el rol del usuario.

## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras errores o tienes sugerencias para mejorar el módulo, por favor abre un issue o envía un pull request.
