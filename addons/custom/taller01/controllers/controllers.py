# -*- coding: utf-8 -*-
# from odoo import http


# class Taller01(http.Controller):
#     @http.route('/taller01/taller01', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taller01/taller01/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('taller01.listing', {
#             'root': '/taller01/taller01',
#             'objects': http.request.env['taller01.taller01'].search([]),
#         })

#     @http.route('/taller01/taller01/objects/<model("taller01.taller01"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taller01.object', {
#             'object': obj
#         })

