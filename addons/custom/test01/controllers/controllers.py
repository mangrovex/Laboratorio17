# -*- coding: utf-8 -*-
# from odoo import http


# class Test01(http.Controller):
#     @http.route('/test01/test01', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test01/test01/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test01.listing', {
#             'root': '/test01/test01',
#             'objects': http.request.env['test01.test01'].search([]),
#         })

#     @http.route('/test01/test01/objects/<model("test01.test01"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test01.object', {
#             'object': obj
#         })

