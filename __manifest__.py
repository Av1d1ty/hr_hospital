{
    'name': 'HR Hospital',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menus.xml',
        'views/person_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/patient_contact_person_views.xml',
        'views/patient_diagnosis_views.xml',
        'views/disease_type_views.xml',
        'views/disease_views.xml',
    ],
    'author': "Av1d1ty",
    'category': 'HR',
    'description': """
        Manage hospital human resources.
    """,
    'application': True,
}
