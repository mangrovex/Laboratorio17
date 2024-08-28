from odoo import fields, models, api


class CustomerTable(models.Model):
    _name = 'nursery.customer.table'
    _inherit = 'nursery.plants'
    _description = 'Description'

    is_client = fields.Boolean('es cliente')
