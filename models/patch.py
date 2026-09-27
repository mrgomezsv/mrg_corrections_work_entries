# -*- coding: utf-8 -*-

def patch_generate_work_entries():
    from datetime import datetime, date
    try:
        from odoo.addons.hr_work_entry_contract.models import hr_contract
        if hasattr(hr_contract, 'HrContract') and hasattr(hr_contract.HrContract, '_generate_work_entries'):
            original_method = hr_contract.HrContract._generate_work_entries
            
            def safe_generate_work_entries(self, date_start, date_stop, *args, **kwargs):
                if isinstance(date_start, date) and not isinstance(date_start, datetime):
                    date_start = datetime.combine(date_start, datetime.min.time())
                if isinstance(date_stop, date) and not isinstance(date_stop, datetime):
                    date_stop = datetime.combine(date_stop, datetime.max.time())
                return original_method(self, date_start, date_stop, *args, **kwargs)
            
            hr_contract.HrContract._generate_work_entries = safe_generate_work_entries
    except Exception:
        pass

# Ejecutar el parche al cargar el módulo
patch_generate_work_entries()