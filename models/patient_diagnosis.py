from odoo import api, fields, models


class PatientDiagnosis(models.Model):
    _name = 'hospital.patient.diagnosis'
    _description = "Patient's diagnosis"

    name = fields.Char(compute='_compute_diagnosis_name')
    doctor_id = fields.Many2one('hospital.doctor', required=True)
    patient_id = fields.Many2one('hospital.patient', required=True)
    # Can one diagnosis have multiple diseases?
    disease_id = fields.Many2one('hospital.disease', required=True)
    prescription = fields.Text()
    diagnosis_date = fields.Date(default=fields.Date().today())

    comment_required = fields.Boolean()
    mentor_note = fields.Text()
    approved = fields.Boolean()

    @api.depends('disease_id', 'patient_id')
    def _compute_diagnosis_name(self):
        for diagnosis in self:
            if diagnosis.patient_id and diagnosis.disease_id:
                diagnosis.name = f'{diagnosis.patient_id.full_name}: {diagnosis.disease_id.name}'

    # @api.model
    # def create(self, vals):
    #     doctor = self.env['hospital.doctor'].browse(vals['doctor_id'])
    #     if doctor.is_intern:
    #         vals['comment_required'] = True
    #     return super().create(vals)

    # @api.onchange('mentor_note')
    # def _onchange_mentor_note(self):
    #     print('----------------------------')
    #     print(self.env._uid, self._origin.id)
    #     print(self._origin.id.mentor_id)
    #     if self.env._uid != self._origin.id.mentor_id:
    #         raise exceptions.AccessError(
    #             "Mentor's note may only be changed by the mentor."
    #         )
