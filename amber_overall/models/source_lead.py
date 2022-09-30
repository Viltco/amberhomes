

from odoo import api, fields, models, _


class SourceLead(models.Model):
    _name = "source.lead"
    _description = "Source Lead"
    _rec_name = 'name'

    name = fields.Char(string='Name')
