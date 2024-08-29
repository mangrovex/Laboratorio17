# -*- coding: utf-8 -*-
{
    'name': "Taller02",
    'summary': "Nursery Plants",
    'description': """ Nursery Plants """,
    'author': "Manexware S.A.",
    'website': "https://www.manexware.com",
    'category': 'Uncategorized',
    'version': '17.0.0.0.1',
    'depends': ['base','web','website','portal','kw_partner_dob','sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/nursery_plants_views.xml',
        'views/nursery_contact_views.xml',
    ],
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
