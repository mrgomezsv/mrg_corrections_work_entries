# -*- coding: utf-8 -*-
{
    'name': 'Corrección de Tipo de Fecha para Odoo 16',
    'version': '16.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Corrige error de tipo en generación de work entries para Odoo 16',
    'description': """
        Corrige el error AssertionError: assert isinstance(date_start, datetime)
        en la generación de work entries en Odoo 16, mediante herencia.
    """,
    'author': 'Mario Roberto Gomez',
    'website': 'https://mrgomezsv.github.io',
    'depends': [
        'hr_work_entry_contract',
        'hr_payroll',
    ],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
} 