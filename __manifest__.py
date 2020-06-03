# -*- coding: utf-8 -*-
{
    'name': "odoo_document",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "42 N.E.R.D.S.",
    'website': "https://www.42nerds.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.0.3',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'report/din5008_report.xml',
        'data/report_layout.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}