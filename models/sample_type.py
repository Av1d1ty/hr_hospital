from odoo import fields, models


class SampleType(models.Model):
    _name = 'hospital.sample.type'
    _description = 'Sample type'

    name = fields.Char(required=True)
    sample_ids = fields.One2many('hospital.sample', 'sample_type_id')
