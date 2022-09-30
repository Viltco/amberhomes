from odoo import models, fields, api,_
from odoo.exceptions import ValidationError , UserError


class CRMLeadInh(models.Model):
    _inherit = "crm.lead"
    
    mobile_2 = fields.Char(string='Mobile No.2')
    proj_prop = fields.Char(string='Location')

    source_lead_id = fields.Many2one('source.lead', string="Source")

    lead_type = fields.Selection([
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
    ], string="Type", readonly=False)

    lead_state = fields.Selection([
        ('interested', 'Interested'),
        ('call_back', 'Call Back'),
        ('invalid_number', 'Invalid Number'),
        ('wrong_number', 'Wrong Number'),
        ('language_barrier', 'Language Barrier'),
        ('do_not_call', 'Do Not Call'),
    ], string="Lead Status", readonly=False)

    transaction_type = fields.Selection([
        ('sale', 'Sale'),
        ('rent', 'Rent'),
    ], string='Transaction Type')

    budget_from = fields.Integer(string='Budget From')
    budget_to = fields.Integer(string='Budget To')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.mobile_2 = self.partner_id.mobile_2

