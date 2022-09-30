from odoo import models, fields, api,_
from odoo.exceptions import ValidationError , UserError


class ResPartnerInh(models.Model):
    _inherit = "res.partner"
    
    mobile_2 = fields.Char(string='Mobile No.2')
    note = fields.Text(string='Note')

    partner_type = fields.Selection([
        ('is_buyer', 'Buyer'),
        ('is_seller', 'Seller'),
        ('is_tenat', 'Tenant'),
        ('is_landlord', 'Landlord'),
    ], string="Partner Type")
