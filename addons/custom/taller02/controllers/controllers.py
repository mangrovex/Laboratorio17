# -*- coding: utf-8 -*-
# from odoo import http


# class Taller02(http.Controller):
#     @http.route('/taller02/taller02', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taller02/taller02/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('taller02.listing', {
#             'root': '/taller02/taller02',
#             'objects': http.request.env['taller02.taller02'].search([]),
#         })

#     @http.route('/taller02/taller02/objects/<model("taller02.taller02"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taller02.object', {
#             'object': obj
#         })

