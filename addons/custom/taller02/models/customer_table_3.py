from odoo import fields, models, api


class CustomerTable3(models.Model):
    _inherit = 'nursery.plants'
    _description = 'Description'

    is_culinary = fields.Char('es comestible')
