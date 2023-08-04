from odoo import api, exceptions, fields, models


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    _inherit = 'hospital.person'

    specialty = fields.Many2one('hospital.doctor.specialty', required=True)
    is_intern = fields.Boolean()
    mentor_id = fields.Many2one('hospital.doctor')

    @api.constrains('mentor_id')
    def _check_mentor_is_not_intern(self):
        for doctor in self:
            if doctor.mentor_id.id and doctor.mentor_id.is_intern:
                raise exceptions.ValidationError(
                    'An intern cannot be chosen as a mentor.'
                )
