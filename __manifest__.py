# -*- coding: utf-8 -*-
{
    'name': 'Corrección de Tipo de Fecha en Work Entries',
    'version': '20.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Corrige tipos en generación de work entries y nombres',
    'description': """
        Corrige:
        1. Tipos de fecha en generación de work entries
        2. Manejo seguro de nombres en calc_afp_name_tr
    """,
    'author': 'Mario Roberto Gomez',
    'website': 'https://mrgomezsv.github.io',
    'license': 'LGPL-3',
    'depends': [
        'hr_work_entry_contract',
        'hr_payroll',
        'treming_sv_payroll',
    ],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
