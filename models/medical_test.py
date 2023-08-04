from odoo import fields, models


class MedicalTest(models.Model):
    _name = 'hospital.medical.test'
    _description = 'Medical test'
    _rec_name = 'test_type_id'

    patient_id = fields.Many2one('hospital.patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor who prescribed", required=True)
    test_type_id = fields.Many2one('hospital.medical.test.type')
    sample_id = fields.Many2one('hospital.sample')
    conclusion = fields.Text()
