# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Rma(models.Model):
    _inherit = 'repair.order'
    _description = 'Ordenes de Reparación'

    employee_id = fields.Many2one(comodel_name= 'hr.employee', string='Empledo')
    