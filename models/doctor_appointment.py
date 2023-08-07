from odoo import api, exceptions, fields, models


class DoctorAppointment(models.Model):
    _name = 'hospital.doctor.appointment'
    _description = 'Doctor appointment'

    name = fields.Char(compute='_compute_name')
    doctor_id = fields.Many2one('hospital.doctor', required=True)
    patient_id = fields.Many2one('hospital.patient', required=True)
    date = fields.Date(required=True)
    time = fields.Float(required=True)

    test_ids = fields.One2many('hospital.medical.test', 'appointment_id', string='Medical tests')
    diagnosis_id = fields.Many2one('hospital.patient.diagnosis')
    recommendations = fields.Text()

    done = fields.Boolean()

    @api.depends('doctor_id', 'date')
    def _compute_name(self):
        for a in self:
            if a.doctor_id.full_name and a.date and a.patient_id.surname:
                a.name = f'{a.date} {a.doctor_id.full_name}/ {a.patient_id.surname}'

    def write(self, vals):
        diagnosis_id = vals.get('diagnosis_id')
        if diagnosis_id:
            self.test_ids.diagnosis_id = diagnosis_id
        return super().write(vals)

    @api.constrains('date', 'time')
    def _check_date_time_available(self):
        if self.date and self.time and self.doctor_id:
            day_schedule = self.env['hospital.doctor.schedule'].search(domain=[
                ('doctor_id', '=', self.doctor_id.id),
                ('appointment_date', '=', self.date),
            ])
            available_hours = day_schedule.mapped('appointment_hours').mapped('value')
            if int(self.time) not in available_hours:
                raise exceptions.UserError("The time is not available in the doctor's schedule.")

    @api.constrains('date', 'time')
    def _check_time_taken(self):
        if self.date and self.time:
            minimal_appointment_duration_hours = 0.25
            time_ceiling = self.time + minimal_appointment_duration_hours
            time_floor = self.time - minimal_appointment_duration_hours
            matching_time = self.search(domain=[
                ('doctor_id', '=', self.doctor_id.id),
                ('date', '=', self.date),
                ('time', '<=', time_ceiling),
                ('time', '>=', time_floor),
                ('id', '!=', self.id),
            ])
            if matching_time:
                raise exceptions.UserError(
                    'Time slot is already taken.'
                )

    @api.constrains('date', 'time', 'doctor_id')
    def _check_not_done(self):
        if self.done:
            raise exceptions.UserError(
                'Date, time and doctor cannot be changed after the appointment has been completed.'
            )

    @api.ondelete(at_uninstall=False)
    def _unlink_except_with_diagnosis(self):
        if any(record.diagnosis_id for record in self):
            raise exceptions.UserError(
                'Cannot delete an appointment with a diagnosis.'
            )
