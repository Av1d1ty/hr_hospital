from odoo import fields, models


class Disease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease directory'

    name = fields.Char()
    type = fields.Many2one('hospital.disease.type')
