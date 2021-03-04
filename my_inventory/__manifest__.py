# -*- coding: utf-8 -*-
{
    'name': "Gestión inventario",  # Module title
    'summary': "Gestiona con facilidad tu inventario",  # Module subtitle phrase
    'description': """LLeva la cuenta del inventario de tus locales, con un seguimiento centralizado""",  # You can also rst format
    'author': "A19Boscoso",
    'website': "http://www.google.com",
    'category': 'Inventory',
    'version': '12.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/gestor_loc.xml',
        'views/gestor_loc_inv.xml',
        'views/gestor_loc_inv_item.xml',
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
