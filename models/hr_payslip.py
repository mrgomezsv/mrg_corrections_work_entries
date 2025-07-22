# -*- coding: utf-8 -*-

from odoo import models
from datetime import datetime, date
import logging

_logger = logging.getLogger(__name__)

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def _compute_worked_days_line_ids(self):
        for payslip in self:
            if payslip.contract_id:
                date_from = payslip.date_from
                date_to = payslip.date_to
                # Convertir a datetime si es necesario
                if isinstance(date_from, date) and not isinstance(date_from, datetime):
                    date_from = datetime.combine(date_from, datetime.min.time())
                if isinstance(date_to, date) and not isinstance(date_to, datetime):
                    date_to = datetime.combine(date_to, datetime.max.time())
                try:
                    payslip.contract_id._generate_work_entries(date_from, date_to)
                except Exception as e:
                    _logger.warning("Error generating work entries for payslip %s: %s", payslip.id, str(e))
        return super()._compute_worked_days_line_ids() 