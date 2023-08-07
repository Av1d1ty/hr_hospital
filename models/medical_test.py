from odoo import fields, models


class MedicalTest(models.Model):
    _name = 'hospital.medical.test'
    _description = 'Medical test'
    _rec_name = 'test_type_id'

    patient_id = fields.Many2one('hospital.patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor who prescribed", required=True)
    test_type_id = fields.Many2one('hospital.medical.test.type')
    sample_id = fields.Many2one('hospital.sample')
    appointment_id = fields.Many2one('hospital.doctor.appointment')
    conclusion = fields.Text()
    diagnosis_id = fields.Many2one('hospital.patient.diagnosis')

    # recursion problem
    # def write(self, vals):
    #     diagnosis_id = vals.get('diagnosis_id')
    #     if diagnosis_id:
    #         self.appointment_id.diagnosis_id = diagnosis_id
    #     return super().write(vals)
