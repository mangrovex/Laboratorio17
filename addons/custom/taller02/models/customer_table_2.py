from odoo import fields, models, api


class CustomerTable2(models.Model):
    _name = 'nursery.plants'
    _inherit = 'nursery.plants'
    _description = 'Description'

    plant_type = fields.Char('Tipo de planta')
