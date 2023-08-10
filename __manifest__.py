{
    'name': 'HR Hospital',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'wizard/doctor_change_batch_views.xml',
        'wizard/reschedule_appointment_views.xml',
        'wizard/diagnosis_filter_views.xml',

        'views/hospital_menus.xml',
        'views/person_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/patient_contact_person_views.xml',
        'views/patient_diagnosis_views.xml',
        'views/disease_type_views.xml',
        'views/disease_views.xml',
        'views/doctor_appointment_views.xml',
        'views/doctor_personal_doctor_history_views.xml',
        'views/medical_test_views.xml',
        'views/medical_test_type_views.xml',
        'views/sample_views.xml',
        'views/sample_type_views.xml',
        'views/doctor_schedule_views.xml',
        'views/doctor_appointment_hours_views.xml',

        'report/disease_report.xml',
    ],
    'author': "Av1d1ty",
    'category': 'HR',
    'description': """
        Manage hospital human resources.
    """,
    'application': True,
}
