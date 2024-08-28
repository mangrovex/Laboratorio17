from odoo import fields, models, api


class NurseryOrder(models.Model):
    _name = 'nursery.order'
    _description = 'Description'

    name = fields.Char(
        string='# de orden')
