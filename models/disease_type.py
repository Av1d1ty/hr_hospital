from odoo import api, fields, models


class DiseaseType(models.Model):
    _name = 'hospital.disease.type'
    _description = 'Catalog of disease types'
    _parent_name = 'parent_id'
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(required=True, index=True)
    complete_name = fields.Char(compute='_compute_complete_name', recursive=True, store=True)
    parent_id = fields.Many2one('hospital.disease.type', ondelete='cascade')
    parent_path = fields.Char(unaccent=False, index=True)
    child_ids = fields.One2many('hospital.disease.type', 'parent_id')

    disease_ids = fields.One2many('hospital.disease', 'type', string='Diseases')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = f'{category.parent_id.name} / {category.name}'
            else:
                category.complete_name = category.name
