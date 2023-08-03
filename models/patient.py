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

    @api.depends('birthday')
    def _compute_age(self):
        for patient in self:
            if patient.birthday:
                patient.age = (fields.Date.today() - patient.birthday).days / 365.2425
