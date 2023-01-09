# -*- coding: utf-8 -*-
# from odoo import http


# class ComponentCreator(http.Controller):
#     @http.route('/component_creator/component_creator', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/component_creator/component_creator/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('component_creator.listing', {
#             'root': '/component_creator/component_creator',
#             'objects': http.request.env['component_creator.component_creator'].search([]),
#         })

#     @http.route('/component_creator/component_creator/objects/<model("component_creator.component_creator"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('component_creator.object', {
#             'object': obj
#         })
