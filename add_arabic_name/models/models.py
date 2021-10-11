# -*- coding: utf-8 -*-

from odoo import models, fields, api


class add_arabic_name(models.Model):
    _inherit = 'hr.employee'
    _description = 'add_arabic_name'
    arabic_name = fields.Char(string="Arabic Name", required=False, )