# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo.tools.safe_eval import safe_eval
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class AccountJournal(models.Model):
    _inherit = 'account.journal'
    branch_id = fields.Many2one('res.branch', 'Branch')



class account_move(models.Model):
    _inherit = 'account.move'
    branch_id = fields.Many2one('res.branch', 'Branch', )


class account_move_line(models.Model):
    _inherit = 'account.move.line'
    branch_id = fields.Many2one('res.branch', 'Branch', )


class AccountPayment(models.Model):
    _inherit = "account.payment"
    branch_id = fields.Many2one('res.branch', string='Branch', )
