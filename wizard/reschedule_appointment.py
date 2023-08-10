from odoo import fields, models


class RescheduleAppointment(models.TransientModel):
    _name = 'hospital.doctor.appointment.reschedule'
    _description = 'Reschedule Appointment'

    appointment_id = fields.Many2one('hospital.doctor.appointment', required=True)
    date = fields.Date(required=True)
    time = fields.Float(required=True)
    doctor_id = fields.Many2one('hospital.doctor', required=True)

    def reschedule(self):
        self.appointment_id.date = self.date
        self.appointment_id.time = self.time
        self.appointment_id.doctor_id = self.doctor_id
