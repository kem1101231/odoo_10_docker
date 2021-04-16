import logging
from datetime import timedelta
from functools import partial

import psycopg2
import pytz
import json

import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(dirname(abspath(__file__))))+'/pos_trans_pers/models/')

from odoo import api, fields, models, tools, _
from odoo.tools import float_is_zero
from odoo.exceptions import UserError
from odoo.http import request
import odoo.addons.decimal_precision as dp
from pos_order_ext import PosOrderExt
print(sys.path)


posExt = PosOrderExt()

'''
class PosOrderExt():
    _inherit = "pos.order"

    mech_id = fields.Many2one('res.partner',string='Mechanic')
'''

ouputdata = None

class PosOrderPersonel(models.Model):

    _name = "pos.order.personel"
    _description = "Point of Sale Orders Personel Included"
    _order = "id desc"

    order_id = fields.Integer(string='Order ID')
    pos_ref_id = fields.Char(string='POS Reference')
    mech_id = fields.Many2one('res.partner',string='Mechanic')
    omech_id = fields.Many2one('res.partner',string='Outside Mechanic')
    chckr_id = fields.Many2one('res.partner',string='Checker')
    packr_id = fields.Many2one('res.partner',string='Packer')

    @api.model
    def posExtDisData(self):
        posExt.displayData()

        self.env.cr.execute("select max(id)+1 from pos_order")
        ord_id = self.env.cr.fetchone()

        print(ord_id)

    @api.model
    def setPosExtMechData(self, datain):
        print(datain)
        posExt.setMechSelID(datain)
        print("Done add data mecha")
        posExt.displayData()

    @api.model
    def setPosExtOMecData(self, datain):
        print(datain)
        posExt.setOMecSelID(datain)
        print("Done add data omech")
        posExt.displayData()

    @api.model
    def setPosExtChckrData(self, datain):
        posExt.setChckSelID(datain)
        print("Done add data chckr")
        posExt.displayData()

    @api.model
    def setPosExtPackrData(self, datain):
        posExt.setPackrselID(datain)
        print("Done add data packr")
        posExt.displayData()

    @api.model
    def setOrdRefhData(self, datain):
        print(datain)
        posExt.setOrdRefID(datain)
        print("Done add data ord_id")
        posExt.displayData()


    @api.model
    def setPosExtDataToNone(self, datain):

        if (datain == 'mecha'):
            posExt.setMechSelIDToNone()
        if (datain == 'omech'):
            posExt.setOMecSelIDToNone()
        if (datain == 'chckr'):
            posExt.setChckSelIDToNone()
        if (datain == 'packr'):
            posExt.setPackrselIDToNone()

        print("Done setting data to null")
        posExt.displayData()

    @api.model
    def addData(self, dataList):

        jsonData = json.loads(dataList)
        self.env['pos.order.personel'].sudo().create({'mech_id': jsonData['mech_id'],'omech_id':jsonData['omec_id'], 'chckr_id': jsonData['chkr_id'],'packr_id': jsonData['pckr_id'],'order_id': 0,'pos_ref_id':'Order '+ jsonData['ord_id']})
        
        print("Data Saved -----------------------------------------------")
        
    @api.model
    def massAddData(self, dataList):
        print(dataList)
        jsonData = json.loads(dataList)
        for idxVal in jsonData:
            print(idxVal)
            val = jsonData[idxVal]
            self.env['pos.order.personel'].sudo().create({'mech_id': val['mech_id'],'omech_id': val['omec_id'], 'chckr_id': val['chkr_id'],'packr_id': val['pckr_id'],'order_id': 99,'pos_ref_id':'Order '+ idxVal})

        print("Save complete")    

    @api.model
    def testConnection(self):
        return True


    # This function contains the lines of code to potentially get the transaction data of the pos_order_personel model.
    # Note that this not yet been used except from this model.
    @api.model
    def get_pos_trans_data(self, ord_id):

        pos_ref = self.env['pos.order'].sudo().search([('pos_reference', '=', 'Order '+ str(ord_id))], limit=1)
        pos_trans = self.env['pos.order.personel'].sudo().search([('pos_ref_id', '=', 'Order '+ str(ord_id))], limit=1)
        pos_trans_rec = self.env['pos.order.personel'].sudo().search([('pos_ref_id', '!=', None),])

        print(pos_ref)
        print(pos_ref.id)
        print(ord_id)
        print('Order '+ str(ord_id))
        print(pos_trans)
        print(type(pos_trans))
        print(pos_trans.id)


        print(pos_trans.mech_id)
        print(pos_trans.omech_id)
        print(pos_trans.chckr_id)
        print(pos_trans.packr_id)

        print(pos_trans.mech_id.id)
        print(pos_trans.omech_id.id)
        print(pos_trans.chckr_id.id)
        print(pos_trans.packr_id.id)

        print("++++++++++++++++++++++++++++++++++++++++++++++s+++++++++++++++++++")

        print(pos_trans_rec)
        
       
        for pp in pos_trans_rec:
            print(pp.id)
            print(pp.pos_ref_id)
            print(pp.mech_id.name)
            print(pp.omech_id.name)
            print(pp.chckr_id.name)
            print(pp.packr_id.name)
        


        ouputdata = pos_trans
