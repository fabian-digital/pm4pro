# -*- coding: utf-8 -*-
# from odoo import http


# class Pm4proQuicktask(http.Controller):
#     @http.route('/pm4pro_quicktask/pm4pro_quicktask', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pm4pro_quicktask/pm4pro_quicktask/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pm4pro_quicktask.listing', {
#             'root': '/pm4pro_quicktask/pm4pro_quicktask',
#             'objects': http.request.env['pm4pro_quicktask.pm4pro_quicktask'].search([]),
#         })

#     @http.route('/pm4pro_quicktask/pm4pro_quicktask/objects/<model("pm4pro_quicktask.pm4pro_quicktask"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pm4pro_quicktask.object', {
#             'object': obj
#         })
