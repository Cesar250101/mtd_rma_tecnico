# -*- coding: utf-8 -*-
{
    'name': "mtd_rma_tecnico",

    'summary': """
        Agregar a la RMA un campo many2one con los empleados""",

    'description': """
        Agregar a la RMA un campo many2one con los empleados 
        y se agrega el emplado al reporte RMA
    """,

    'author': "Method ERP",
    'website': "https://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','repair'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}