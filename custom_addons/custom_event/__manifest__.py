# -*- coding: utf-8 -*-
{
    'name': "Custom Event",

    'summary': "Odoo Challenger Custom Event",

    'description': """
        Odoo Challenger Custom Event
    """,

    'author': "Shamim Hossen Razu",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        'security/event_security.xml',
        'security/ir.model.access.csv',
        'data/custom_event_data.xml',
        'views/views.xml',
        'views/custom_event_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}
