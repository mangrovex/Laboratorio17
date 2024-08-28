# -*- coding: utf-8 -*-
{
    'name': "test01",

    'summary': "Jardin botanico",

    'description': """
Venta de plantas
    """,

    'author': "Manuel Vega Ulloa",
    'website': "https://www.manexware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'custom',
    'version': '17.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','website','portal'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/nursery_plants_views.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

