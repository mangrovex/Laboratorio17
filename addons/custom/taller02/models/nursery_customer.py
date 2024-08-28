from odoo import fields, models, api


class NurseryCustomer(models.Model):
    _name = 'nursery.customer'
    _description = 'Modelo Cliente'

    name = fields.Char(
        string='Nombre del cliente',
        required=True)
    email = fields.Char(
        string='Email',
        help='Correo donde le llega las promociones, catalogos y facturas',
        required=False)
