# -*- coding: utf-8 -*-

from odoo import models
from datetime import datetime, date

class HrContract(models.Model):
    _inherit = 'hr.contract'

    def _generate_work_entries(self, date_start, date_stop):
        # Convierte date_start y date_stop a datetime si son date
        if isinstance(date_start, date) and not isinstance(date_start, datetime):
            date_start = datetime.combine(date_start, datetime.min.time())
        if isinstance(date_stop, date) and not isinstance(date_stop, datetime):
            date_stop = datetime.combine(date_stop, datetime.max.time())
        return super()._generate_work_entries(date_start, date_stop) 