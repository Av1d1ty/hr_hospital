from datetime import datetime
from odoo import fields, models


class DiagnosisFilter(models.TransientModel):
    _name = 'hospital.diagnosis.filter'
    _description = 'Diagnosis filter'

    year = fields.Selection(selection='_get_year_selection', required=True,
                            default=fields.Date().today().year)
    month = fields.Selection(selection='_get_month_selection', required=True,
                            default=fields.Date().today().month)

    def _get_year_selection(self):
        return [(year, str(year)) for year in range(2020, fields.Date().today().year + 1)]

    def _get_month_selection(self):
        return [
            (1, 'January'), (2, 'February'), (3, 'March'),
            (4, 'April'), (5, 'May'), (6, 'June'),
            (7, 'July'), (8, 'August'), (9, 'September'),
            (10, 'October'), (11, 'November'), (12, 'December')
        ]

    def print_report(self):
        target_date_ceiling = datetime(int(self.year), int(self.month), 31)
        target_date_floor = datetime(int(self.year), int(self.month), 1)
        diagnoses = self.env['hospital.patient.diagnosis'].search_read([
            ('diagnosis_date', '>', target_date_floor),
            ('diagnosis_date', '<', target_date_ceiling),
        ])

        disease_count = {}
        for diagnosis in diagnoses:
            # indexing like that is definitely a wrong move
            disease_count[diagnosis['disease_id'][1]] = disease_count.get(diagnosis['disease_id'][1], 0) + 1

        data = {
            'year': self.year,
            'month': dict(self._get_month_selection())[int(self.month)],
            'disease_count': disease_count,
        }

        return self.env.ref('hr_hospital.hospital_disease_report').report_action(self, data=data)
