# -*- coding: utf-8 -*-
{
    'name': "Odoo Document",

    'summary': """
        Custom template for German business documents""",

    'description': """
        TODO
    """,

    'author': "42 N.E.R.D.S.",
    'website': "https://www.42nerds.com",

    'category': 'Uncategorized',
    'version': '0.0.1',

    'depends': ['account', 'base'],

    'data': [
        'report/din5008_report.xml',
        'data/report_layout.xml',
        'views/res_company.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}