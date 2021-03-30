# Copyright 2015 Anybox
# Copyright 2018 Camptocamp, ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale product set',
    'category': 'Sale',
    'license': 'AGPL-3',
    'author': 'Anybox, Odoo Community Association (OCA)',
    'version': '12.0.1.3.1',
    'website': 'https://github.com/OCA/sale-workflow',
    'summary': "Sale product set",
    'depends': [
        'barcodes',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/rule_product_set.xml',
        'data/default_barcode_pattern.xml',
        'views/product_set.xml',
        'wizard/product_set_add.xml',
        'views/sale_order.xml',
        'report/reports.xml',
        'report/templates.xml',
    ],
    'demo': [
        'demo/product_set.xml',
        'demo/product_set_line.xml',
    ],
    'installable': True,
}
