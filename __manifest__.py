# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Maple Products',
    'category': 'Maple-Vertical',
    'version': '1.0',
    'author': "Portall Solution inc.",
    'website': "portall.ca",
    'summary': 'Maple Product.',
    'description':
        """
Maple Product
================================================

This module provides only datas.
        """,
    'depends': [
        'sale',
        'stock',
    ],
    'data': [
        'data/product_attributes.xml',
        'data/product_categories.xml',
        'data/products.xml',
    ],
    'qweb': [
#        "static/src/xml/*.xml",
    ],
#    'bootstrap': True,  # load translations for login screen
    'installable': True,
    'application': False,
    'auto_install': False,
}

