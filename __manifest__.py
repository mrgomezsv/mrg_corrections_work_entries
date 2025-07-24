# -*- coding: utf-8 -*-
{
    'name': 'Corrección de Tipo de Fecha para Odoo 16',
    'version': '16.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Corrige errores de tipo en generación de work entries y manejo de nombres para Odoo 16',
    'description': """
        Corrige múltiples errores en Odoo 16:
        1. AssertionError: assert isinstance(date_start, datetime) en generación de work entries
        2. IndexError: list index out of range en calc_afp_name_tr
        Soluciones implementadas mediante herencia sin modificar archivos originales.
    """,
    'author': 'Mario Roberto Gomez',
    'website': 'https://mrgomezsv.github.io',
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