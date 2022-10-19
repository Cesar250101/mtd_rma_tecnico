# -*- coding: utf-8 -*-
from odoo import http

# class MtdRmaTecnico(http.Controller):
#     @http.route('/mtd_rma_tecnico/mtd_rma_tecnico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mtd_rma_tecnico/mtd_rma_tecnico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mtd_rma_tecnico.listing', {
#             'root': '/mtd_rma_tecnico/mtd_rma_tecnico',
#             'objects': http.request.env['mtd_rma_tecnico.mtd_rma_tecnico'].search([]),
#         })

#     @http.route('/mtd_rma_tecnico/mtd_rma_tecnico/objects/<model("mtd_rma_tecnico.mtd_rma_tecnico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mtd_rma_tecnico.object', {
#             'object': obj
#         })