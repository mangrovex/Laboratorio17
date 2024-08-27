# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Plant Nursery',
    'version': '17.0.0.0.1',
    'category': 'Tools',
    'summary': 'Plants and Customers Management',
    'depends': ['base', 'web', 'mail', 'rating', 'utm', 'website', 'portal','sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        # 'data/ir_sequence_data.xml',
        # 'data/mail_template_data.xml',
        # 'data/plant_data.xml',
        'views/nursery_plant_views.xml',
        'views/nursery_customer_views.xml',
        'views/nursery_order_views.xml',
        # 'views/nursery_plant_templates.xml',
        # 'views/nursery_plant_quote_ask.xml',
        # 'views/assets.xml',
        # 'views/nursery_order_portal_templates.xml',

    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
