# -*- coding: utf-8 -*-
{
    'name': "POS Transaction Personel",

    'summary': """
        POS Mechanic, Checker and Packer selector """,

    'description': """
        Mechanic, Checker and Packer selector on a POS sale transaction,\n
        The module's model was updated that it added a field (pos_ref_id) which is a reference to the pos_reference field of pos.order model.\n
        The field was an auto generated string containing a session number and the transaction number which is in the form 'Order 00000-000-0000'.\n
        Every sale holds a unique pos_reference whethere saved online or cached locally.\n
        
        To access the transaction data namely: Mechanic (mech_id), Outside Mechanic (omec_id), Checker (chckr_id), Packer (packr_id),\n
        the pos_reference value from pos.order model is to be retreived first.\n
        Then fetch the transaction data from the pos_trans_pers model using the earlier retrieved value of pos_reference through the pos_ref_id field of the pos_trans_pers model.\n
        The resulting data will or should contain the transaction data that you wish to access.\n
 
    """,

    'author': "KNeCo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded

    'data': [

        'views/main_display.xml',
    ],
    # only loaded in demonstration mode

    'installable': True,
    'application': True,

    'qweb': [
        'static/src/xml/pos_edited.xml',
        'views/main_display.xml',

    ],
}