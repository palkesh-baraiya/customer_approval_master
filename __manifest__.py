# -*- coding: utf-8 -*-
{
    'name' : 'Customer Approval',
    'version' : '1.0',
    'summary': 'This module will allow you to Approval of Customer and maintain Approval history',
    'category': 'base',
    'website': '',
    'author': 'Palkesh',
    'depends' : ['base', 'sale_management', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/partner_views.xml',
        'views/sale_views.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
