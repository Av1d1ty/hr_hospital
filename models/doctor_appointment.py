from odoo import api, fields, models


class DoctorAppointment(models.Model):
    _name = 'hospital.doctor.appointment'
    _description = 'Doctor appointment'

    name = fields.Char(compute='_compute_name')
    doctor_id = fields.Many2one('hospital.doctor', required=True)
    patient_id = fields.Many2one('hospital.patient', required=True)
    date = fields.Date(required=True)
    time = fields.Float(required=True)
    diagnosis_id = fields.Many2one('hospital.patient.diagnosis')
    recommendations = fields.Text()

    @api.depends('doctor_id', 'date')
    def _compute_name(self):
        for a in self:
            if a.doctor_id.full_name and a.date and a.time:
                a.name = f'{a.date} {a.doctor_id.full_name}/ {a.patient_id.surname}'
