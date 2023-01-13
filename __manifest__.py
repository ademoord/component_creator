# -*- coding: utf-8 -*-
{
    'name': "Component Creator",
    'summary': "The Component Creator Module",
    'description': """
        Component Creator is a simple Master Component creator that helps
        user to create components and define the desired processing time
        from scratch.
    """,
    'author': "andromeda",
    'website': "www.alkeba.id",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Alkeba Component',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'sequence': -100,

    # always loaded
    # 'qweb': ['qweb.xml'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/component_master_views.xml',
        'views/item_master_views.xml',
        # 'views/import_csv_views.xml',
    ],
    'js': [
        'static/src/import_csv_button.js'
    ],
    
    'installable': True,
    'auto_install': False,
    'application': True,
    # 'assets': {},
    'license': 'LGPL-3',

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
