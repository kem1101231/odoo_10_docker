# -*- coding: utf-8 -*-
from odoo import http

# class PosTransPers(http.Controller):
#     @http.route('/pos_trans_pers/pos_trans_pers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_trans_pers/pos_trans_pers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_trans_pers.listing', {
#             'root': '/pos_trans_pers/pos_trans_pers',
#             'objects': http.request.env['pos_trans_pers.pos_trans_pers'].search([]),
#         })

#     @http.route('/pos_trans_pers/pos_trans_pers/objects/<model("pos_trans_pers.pos_trans_pers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_trans_pers.object', {
#             'object': obj
#         })