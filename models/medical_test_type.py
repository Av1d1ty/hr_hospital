from odoo import api, fields, models


class MedicalTestType(models.Model):
    _name = 'hospital.medical.test.type'
    _description = 'Medical test type'
    _parent_name = 'parent_id'
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(required=True, index=True)
    complete_name = fields.Char(compute='_compute_complete_name', recursive=True, store=True)
    parent_id = fields.Many2one('hospital.medical.test.type', ondelete='cascade')
    parent_path = fields.Char(unaccent=False, index=True)
    child_ids = fields.One2many('hospital.medical.test.type', 'parent_id')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = f'{category.parent_id.name} / {category.name}'
            else:
                category.complete_name = category.name
