# -*- coding: utf-8 -*-
{
    'name': "Odoo Document",

    'summary': """
        Custom template for German business documents""",

    'description': """
        Add a new document template as "42nerds" with a performat for this document template "DINA4".
        This document provides much more informations for invoices etc.
    """,

    'author': "42 N.E.R.D.S.",
    'website': "https://www.42nerds.com",

    'category': 'Sales',
    'version': '0.0.2',

    'depends': ['account', 'base', 'stock'],

    'data': [
        'report/din5008_report.xml',
        'report/report_stockpicking_operations.xml',
        'data/report_layout.xml',
        'views/res_company.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}