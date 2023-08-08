from odoo import fields, models


class DoctorSpecialty(models.Model):
    _name = 'hospital.doctor.specialty'
    _description = 'Medical specialty'

    name = fields.Char('Title', required=True, index=True)
