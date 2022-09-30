# -*- coding: utf-8 -*-
{
    'name': "Amber Overall",

    'summary': """
        Amber Homes Overall Functionalities""",

    'description': """
        Amber Homes Overall Functionalities
    """,

    'author': "Musadiq Fiaz Chaudhary",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'all',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/lead_views.xml',
        'views/partner_views.xml',
        'views/source_views.xml',
    ],

}
