from odoo import api, fields, models

class Company(models.Model):
    _inherit = 'res.company'

    ceos = fields.Char(string='CEOs', store=True, readonly=False)
    company_registry_id = fields.Char(string='Company Reg No', store=True, readonly=False)
    corporation_location = fields.Char(string='Location of Corporation', store=True, readonly=False)
    fax = fields.Char(string='Fax', store=True, readonly=False)
    in_liquidation = fields.Boolean(string='In Liquidation', store=True, readonly=False)
    vat_national = fields.Char(string='National Tax ID', store=True, readonly=False)