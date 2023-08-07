from odoo import fields, models


class DoctorSchedule(models.Model):
    _name = 'hospital.doctor.schedule'
    _description = 'Doctor Schedule'
    _rec_name = 'doctor_id'

    doctor_id = fields.Many2one('hospital.doctor')
    appointment_date = fields.Date()
    appointment_hours = fields.Many2many('hospital.doctor.appointment.hours')

    _sql_constraints = [
        ('_check_unique_date', 'UNIQUE (appointment_date)',
         'Only one schedule can exist for a date.'),
    ]
