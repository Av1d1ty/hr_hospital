from odoo import fields, models


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'
    _inherit = 'hospital.person'

    specialty = fields.Many2one('hospital.doctor.specialty', required=True)
