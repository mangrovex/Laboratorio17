# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import random

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import email_split, email_split_and_format


class NurseryOrder(models.Model):
    _name = 'nursery.order'
    _description = 'Plant Order'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char(
        'Reference',
        default=lambda self: _('New'),
        required=True)
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsible',
        index=True,
        required=True,
        default=lambda self: self.env.user)
    date_open = fields.Date(
        'Confirmation date',
        readonly=True)
    customer_id = fields.Many2one(
        "nursery.customer",
        string='Customer',
        index=True, required=True)
    line_ids = fields.One2many(
        'nursery.order.line', 'order_id', string='Order Lines')
    amount_total = fields.Float(
        'Amount', compute='_compute_amount_total', store=True)
    company_id = fields.Many2one(
        'res.company', string='Company', related='user_id.company_id',
        readonly=True, store=True)
    currency_id = fields.Many2one(
        'res.currency', string='Currency', related='company_id.currency_id',
        readonly=True, required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),
        ('cancel', 'Canceled'),
    ], default='draft', index=True, group_expand="_expand_states")
    last_modification = fields.Datetime(readonly=True)

    @api.depends('line_ids.price')
    def _compute_amount_total(self):
        for order in self.line_ids:
            self.amount_total = sum(order.mapped('price'))

    # def _compute_access_url(self):
    #     super(Order, self)._compute_access_url()
    #     for order in self:
    #         order.access_url = '/my/order/%s' % order.id

    # def action_confirm(self):
    #     if self.state != 'draft':
    #         return
    #     self.activity_feedback(['mail.mail_activity_data_todo'])
    #     return self.write({
    #         'state': 'open',
    #         'date_open': fields.Datetime.now(),
    #     })

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         if 'company_id' in vals:
    #             vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code(
    #                 'plant.order') or _('New')
    #         else:
    #             vals['name'] = self.env['ir.sequence'].next_by_code('plant.order') or _('New')
    #     res = super(Order, self).create(vals)
    #     res.activity_schedule(
    #         'mail.mail_activity_data_todo',
    #         user_id=self.env.ref('base.user_demo').id,
    #         date_deadline=fields.Date.today() + relativedelta(days=1),
    #         summary=_('Pack the order'))
    #     return res

    # def write(self, values):
    #     # helper to "YYYY-MM-DD"
    #     values['last_modification'] = fields.Datetime.now()
    #     return super(NurseryOrder, self).write(values)
    #
    # def unlink(self):
    #     # self is a recordset
    #     for order in self:
    #         if order.state == 'done':
    #             raise UserError("You can not delete confirmed orders")
    #
    #     return super(Order, self).unlink()
    #
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]
    #
    # def action_get_ratings(self):
    #     action = self.env['ir.actions.act_window'].for_xml_id('rating', 'action_view_rating')
    #     return dict(
    #         action,
    #         domain=[('res_id', 'in', self.ids), ('res_model', '=', 'nursery.order')],
    #     )
    #
    # def action_send_rating(self):
    #     rating_template = self.env.ref('plant_nursery.mail_template_plant_order_rating')
    #     for order in self:
    #         order.rating_send_request(rating_template, force_send=True)
    #
    # def rating_get_partner_id(self):
    #     if self.customer_id.partner_id:
    #         return self.customer_id.partner_id
    #     return self.env['res.partner']
    #
    # def message_new(self, msg_dict, custom_values=None):
    #     if custom_values is None:
    #         custom_values = {}
    #
    #     if custom_values.get('category_id', False):
    #         domain = [('category_id', '=', custom_values.pop('category_id'))]
    #         custom_values.pop
    #     else:
    #         domain = []
    #
    #     # find or create customer
    #     email = email_split(msg_dict.get('email_from', False))[0]
    #     name = email_split_and_format(msg_dict.get('email_from', False))[0]
    #     customer = self.env['nursery.customer'].find_or_create(email, name)
    #
    #     # happy Xmas
    #     plants = self.env['nursery.plant'].search(domain)
    #     plant = self.env['nursery.plant'].browse([random.choice(plants.ids)])
    #     custom_values.update({
    #         'customer_id': customer.id,
    #         'line_ids': [(4, plant.id)],
    #     })
    #
    #     return super(Order, self).message_new(msg_dict, custom_values=custom_values)


class OrderLine(models.Model):
    _name = 'nursery.order.line'
    _description = 'Plant Order Line'
    _order = 'order_id DESC'
    _rec_name = 'order_id'

    order_id = fields.Many2one(
        'nursery.order', string='Order',
        index=True, ondelete='cascade', required=True)
    plant_id = fields.Many2one(
        'nursery.plant', string='Plant',
        index=True, ondelete='cascade', required=True)
    price = fields.Float('Price')

    @api.onchange('plant_id')
    def _onchange_plant_id(self):
        if self.plant_id:
            self.price = self.plant_id.price

    @api.model
    def create(self, values):
        if 'price' not in values:
            values['price'] = self.env['nursery.plant'].browse(values['plant_id']).price
        return super(OrderLine, self).create(values)
