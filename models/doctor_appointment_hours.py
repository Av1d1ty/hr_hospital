from odoo import fields, models


class DoctorAppointmentHours(models.Model):
    _name = 'hospital.doctor.appointment.hours'
    _description = 'Appointment hours'
    _rec_name = 'value'
    _order = 'value'

    value = fields.Float(required=True)
