# -*- coding: utf-8 -*-
{
    "name": "Core48 Sale QR",
    "summary": """Core48 Sale Order QR""",
    'author': "Core48",
    'website': "https://core48.com",
    'license': 'LGPL-3',
    'category': 'sale',
    "version": "17.0.0.1",
    "depends": [
        'sale_management'
            ],
    "data": [
        "views/inherit_sale.xml",
        "views/inherit_report.xml" 
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
