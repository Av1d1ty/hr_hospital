from odoo import fields, models


class DoctorSchedule(models.Model):
    _name = 'hospital.doctor.schedule'
    _description = 'Doctor Schedule'
    _rec_name = 'doctor_id'

    doctor_id = fields.Many2one('hospital.doctor', required=True)
    appointment_date = fields.Date(required=True)
    appointment_hours = fields.Many2many('hospital.doctor.appointment.hours', required=True)

    _sql_constraints = [
        ('_check_unique_date', 'UNIQUE (doctor_id, appointment_date)',
         'Only one schedule can exist for a date.'),
    ]
