from odoo import api, fields, models


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'
    _inherit = 'hospital.person'

    birthday = fields.Date()
    age = fields.Integer(compute='_compute_age', default=0)

    # passport
    nationality = fields.Char()
    document_no = fields.Integer()
    expiry_date = fields.Date()
    rntrc = fields.Integer()

    contact_person_ids = fields.Many2many('hospital.patient.contact.person')
    personal_doctor_id = fields.Many2one('hospital.doctor', index=True)

    @api.depends('birthday')
    # BUG craches when birthday is not set, event though the condition is not met
    def _compute_age(self):
        for patient in self:
            if patient.birthday:
                patient.age = (fields.Date.today() - patient.birthday).days / 365.2425

    # FIX does not work when the value is changed through a wizard
    @api.depends('personal_doctor_id')
    def _onchange_personal_doctor(self):
        if self.personal_doctor_id:
            self.env['hospital.doctor.personal.doctor.history'].create({
                'doctor_id': self.personal_doctor_id.id,
                'patient_id': self._origin.id,
                'assignment_date': fields.Date().today()
            })
