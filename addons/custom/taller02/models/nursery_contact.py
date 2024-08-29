from odoo import fields, models, api


class NurseryContact(models.Model):
    _inherit = 'res.partner'
    _description = 'Modelo Cliente'

    is_client = fields.Boolean(
        string='Is client',
        required=False)
    is_planter = fields.Boolean(
        string='Is Planter',
        required=False)
    planter_capacity = fields.Integer(
        string='Capacity')
    planter_height = fields.Integer(
        string='Height')
    drainage_holes = fields.Integer(
        string='Drainage holes',
        required=False)
    planter_color = fields.Integer(
        string='Planter color',
        required=False)
    planter_shape = fields.Char(
        string='Planter shape',
        required=False)