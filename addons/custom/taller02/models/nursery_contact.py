from odoo import fields, models, api


class NurseryContact(models.Model):
    _inherit = 'res.partner'
    _description = 'Modelo Cliente'

    is_client = fields.Boolean(
        string='Is client',
        required=False)