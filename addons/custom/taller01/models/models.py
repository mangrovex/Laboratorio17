# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class taller01(models.Model):
#     _name = 'taller01.taller01'
#     _description = 'taller01.taller01'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

