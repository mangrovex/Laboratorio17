from odoo import fields, models, api


class NurseryPlants(models.Model):
    _name = 'nursery.plants'
    _description = 'Modelo planta'

    name = fields.Char(
        string='Nombre de la planta')
    price = fields.Float(
        string='Precio',
        required=True)
