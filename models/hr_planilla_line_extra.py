# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class HrPlanillaLineExtra(models.Model):
    _inherit = 'hr.planilla.line.extra'

    def calc_afp_name_tr(self):
        """
        Override del método calc_afp_name_tr para manejar casos donde last_name_parts
        está vacío o tiene menos elementos de los esperados.
        """
        try:
            # Llamar al método original
            result = super().calc_afp_name_tr()
            return result
        except IndexError as e:
            # Si hay error de índice, manejar el caso de forma segura
            _logger.warning("IndexError en calc_afp_name_tr para planilla line %s: %s", self.id, str(e))
            
            # Crear un resultado por defecto
            holder = {}
            employee_name = self.nomina_id.employee_id.name or ""
            
            # Dividir el nombre de forma segura
            name_parts = employee_name.split() if employee_name else []
            
            if len(name_parts) >= 2:
                # Si hay al menos 2 partes, usar la primera como apellido
                holder["apellidos"] = [name_parts[0], name_parts[1] if len(name_parts) > 1 else ""]
            elif len(name_parts) == 1:
                # Si solo hay una parte, usarla como apellido
                holder["apellidos"] = [name_parts[0], ""]
            else:
                # Si no hay nombre, usar valores por defecto
                holder["apellidos"] = ["", ""]
            
            # Agregar otros campos necesarios si existen
            if hasattr(self, 'nomina_id') and self.nomina_id:
                holder["nombres"] = employee_name
                holder["dui"] = getattr(self.nomina_id.employee_id, 'dui', '') or ""
                holder["nit"] = getattr(self.nomina_id.employee_id, 'nit', '') or ""
            
            return holder
        except Exception as e:
            # Capturar cualquier otro error inesperado
            _logger.error("Error inesperado en calc_afp_name_tr para planilla line %s: %s", self.id, str(e))
            
            # Retornar estructura mínima
            return {
                "apellidos": ["", ""],
                "nombres": "",
                "dui": "",
                "nit": ""
            } 