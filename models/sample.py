from odoo import fields, models


class Sample(models.Model):
    _name = 'hospital.sample'
    _description = 'Sample for medical tests'

    name = fields.Char(required=True)
    sample_type_id = fields.Many2one('hospital.sample.type')
