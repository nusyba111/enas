import statistics
from statistics import mode, mean

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import datetime



class Cash(models.Model):
    _inherit = 'account.bank.statement.cashbox'



class AccountBankStmtCashWizard(models.Model):
    _inherit = 'account.cashbox.line'

    config_id = fields.Many2one('pos.session',string ="Point Of Sale")



class AccountBankStmtCashWizard(models.Model):
    _inherit = 'pos.session'

    bank_statment_cashbox_id = fields.Many2one('account.bank.statement.cashbox',compute="get_default_bank_id")
    cash_box = fields.One2many('account.cashbox.line','config_id',related="bank_statment_cashbox_id.cashbox_lines_ids")
    account_emp = fields.Many2one('res.users', string='Accountant Employee')
    safety_emp = fields.Many2one('res.users', string='Security Employee')
    comment = fields.Text(string='Comment')
    note = fields.Text(string='Remark')
    user_id = fields.Many2one('res.users', string=' Casheir Employee')
    signature = fields.Char(string='Signature')
    total_wiz = fields.Float(string='total',related="bank_statment_cashbox_id.total")
    
    
    def get_default_bank_id(self):
        for rec in self:
            rec.bank_statment_cashbox_id = 0 
            cash_ids = self.env['account.bank.statement.cashbox'].search([])
            for line in cash_ids:
                if line.total == rec.cash_register_balance_end_real:
                    rec.bank_statment_cashbox_id = line.id 