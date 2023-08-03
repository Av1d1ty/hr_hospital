from odoo import fields, models


class ContactPerson(models.Model):
    _name = 'hospital.patient.contact.person'
    _description = 'Contact person'
    _inherit = 'hospital.person'

    relation = fields.Selection(selection=[
        ('mother', 'Mother'),
        ('father', 'Father'),
        ('son', 'Son'),
        ('daughter', 'Daughter'),
        ('relative', 'Relative'),
        ('friend', 'Friend'),
        ('other', 'Other'),
    ], required=True)
