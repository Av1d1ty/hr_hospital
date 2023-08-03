from odoo import api, fields, models


class Person(models.AbstractModel):
    _name = 'hospital.person'
    _description = 'Abstract model of a person'
    _rec_name = 'full_name'

    name = fields.Char(required=True)
    surname = fields.Char(required=True)
    patronymic = fields.Char()
    full_name = fields.Char(compute='_compute_full_name')

    phone_number = fields.Char(copy=False)
    email = fields.Char(copy=False)
    photo = fields.Image(copy=False)
    sex = fields.Selection(selection=[
        ('M', 'Male'),
        ('F', 'Female'),
    ], required=True)

    @api.depends('name', 'surname', 'patronymic')
    def _compute_full_name(self):
        for person in self:
            person.full_name = f'{person.name} {person.surname} {person.patronymic or ""}'
