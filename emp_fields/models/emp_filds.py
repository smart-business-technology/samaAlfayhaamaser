# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee_fields(models.Model):
    _inherit = 'hr.employee'
    elhadaf = fields.Char(string="الهدف", required=False, )
    perc_hadaf = fields.Char(string="نسبة الهدف(%)", required=False, )
    elahad = fields.Char(string="العهد", required=False, )
    instrument_no = fields.Char(string="Instrument No", required=False, )
    amount = fields.Char(string="amount", required=False, )
    notes = fields.Text(string="الملاحظات", required=False, )
    wosolat_ids = fields.One2many(comodel_name="wosolat.wosolat", inverse_name="emp_ids", string="دفتر الوصولات", required=False, )
    # from1 = fields.Float(string="من",  required=False, )
    # from2 = fields.Float(string="من",  required=False, )
    # from3 = fields.Float(string="من",  required=False, )
    # to1 = fields.Float(string="الي",  required=False, )
    # to2 = fields.Float(string="الي",  required=False, )
    # to3 = fields.Float(string="الي",  required=False, )
    # date1 = fields.Date(string=" تاريخ الاستلام", required=False, )
    # date2 = fields.Date(string=" تاريخ الاستلام", required=False, )
    # date3 = fields.Date(string=" تاريخ الاستلام", required=False, )

class wosolat(models.Model):
    _name = 'wosolat.wosolat'
    from1 = fields.Float(string="من",  required=False, )
    to1 = fields.Float(string="الي",  required=False, )
    date1 = fields.Date(string=" تاريخ الاستلام", required=False, )
    emp_ids = fields.Many2one(comodel_name="hr.employee", string="", required=False, )