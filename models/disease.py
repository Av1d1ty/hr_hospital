from odoo import fields, models


class Disease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease directory'

    name = fields.Char(required=True, index=True)
    disease_type_id = fields.Many2one('hospital.disease.type')
