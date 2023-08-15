from dateutil.relativedelta import relativedelta
from odoo import api, exceptions, fields, models


class FillSchedule(models.TransientModel):
    _name = 'hospital.doctor.schedule.fill'
    _description = 'Fill doctor schedule'

    date_from = fields.Date(required=True)
    doctor_id = fields.Many2one('hospital.doctor')

    monday = fields.Many2many('hospital.doctor.appointment.hours', relation='hours_schedule_fill_mon')
    tuesday = fields.Many2many('hospital.doctor.appointment.hours', relation='hours_schedule_fill_tue')
    wednesday = fields.Many2many('hospital.doctor.appointment.hours', relation='hours_schedule_fill_wed')
    thursday = fields.Many2many('hospital.doctor.appointment.hours', relation='hours_schedule_fill_thi')
    friday = fields.Many2many('hospital.doctor.appointment.hours', relation='hours_schedule_fill_fri')
    saturday = fields.Many2many('hospital.doctor.appointment.hours', relation='hours_schedule_fill_sat')
    sunday = fields.Many2many('hospital.doctor.appointment.hours', relation='hours_schedule_fill_sun')

    @api.constrains('date_from')
    def _check_monday(self):
        if self.date_from.weekday() != 0:
            raise exceptions.ValidationError("Date must be a Monday.")

    def update_schedule(self):
        # Doesn't work, eh
        weekdays = ('monday', 'tuesday', 'wednesday', 'thursday',
                    'friday', 'saturday', 'sunday')

        # for day in weekdays:
        #     tmp = self._fields[day].mapped('value')
        #     print(tmp)

        target_date = self.date_from
        week_schedule = {}
        for i, day in enumerate(weekdays):
            week_schedule[target_date + relativedelta(days=i)] = self[day].ids
# __AUTO_GENERATED_PRINT_VAR_START__
        print('-'*9 + '\n', 'week_schedule:', week_schedule, '\n' + '-'*9) # __AUTO_GENERATED_PRINT_VAR_END__
        # week_schedule = {
        #     target_date: self.monday.ids,
        #     target_date + relativedelta(days=1): self.tuesday.ids,
        #     target_date + relativedelta(days=2): self.wednesday.ids,
        #     target_date + relativedelta(days=3): self.thursday.ids,
        #     target_date + relativedelta(days=4): self.friday.ids,
        #     target_date + relativedelta(days=5): self.saturday.ids,
        #     target_date + relativedelta(days=6): self.sunday.ids,
        # }

        for day, hours in week_schedule.items():
            if not hours:
                continue

            day_schedule = self.env['hospital.doctor.schedule'].search([
                ('doctor_id', '=', self.doctor_id.id),
                ('appointment_date', '=', day),
            ])

            if day_schedule:
                day_schedule.appointment_hours = hours
            else:
                self.env['hospital.doctor.schedule'].create({
                    'doctor_id': self.doctor_id.id,
                    'appointment_date': day,
                    'appointment_hours': hours,
                })
