# -*- coding: utf-8 -*-
#
#   file: /home/andromeda/Projects/Odoo/R01/custom_addons/component_creator/__manifest__.py
#   author: $andromeda
#   desc: Default manifest module information file   
#
{
    'name': "Component Creator",
    'version': '1.0.0',
    'category': 'Component',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Component Creator is a simple Master Component creator that helps
        user to create components and define the desired processing time
        from scratch.
    """,
    'depends': ['base'],
    'sequence': -100,
    'author': "andromeda",
    'data': [
        'security/ir.model.access.csv',
        'views/component_creator_views.xml',
        # 'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
    'demo': [],
}
