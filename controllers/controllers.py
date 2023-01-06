# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons/componentCreator(http.Controller):
#     @http.route('/custom_addons/component_creator/custom_addons/component_creator', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/component_creator/custom_addons/component_creator/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/component_creator.listing', {
#             'root': '/custom_addons/component_creator/custom_addons/component_creator',
#             'objects': http.request.env['custom_addons/component_creator.custom_addons/component_creator'].search([]),
#         })

#     @http.route('/custom_addons/component_creator/custom_addons/component_creator/objects/<model("custom_addons/component_creator.custom_addons/component_creator"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/component_creator.object', {
#             'object': obj
#         })
