from odoo import fields, models


class PersonalDoctorHistory(models.Model):
    _name = 'hospital.doctor.personal.doctor.history'
    _description = 'Personal doctor history'
    _rec_name = 'doctor_id'

    doctor_id = fields.Many2one('hospital.doctor', required=True, index=True)
    patient_id = fields.Many2one('hospital.patient', required=True, index=True)
    assignment_date = fields.Date(default=fields.Date().today())
