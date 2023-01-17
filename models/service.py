# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class ServiceMaster(models.Model):
    _name = 'service.master'
    _description = 'Service Master'
    
    name = fields.Char(string="Nama Layanan", required=True)
    emp_sum = fields.Float(string="Jumlah Keperluan Karyawan", required=True)
    desc = fields.Char(string="Deskripsi Layanan", required=True)
    
    # def test_import(self):
    #     cfile = open('test.csv', 'rb')
    #     data_record = outfile.read()
    #     ir_values = {
    #         'name': 'test.csv',
    #         'datas': base64.b64encode(data_record),
    #         'type': 'binary',
    #         'res_model': 'item_master',
    #         'store_fname': base64.b64encode(data_record),
    #         'mimetype': 'text/csv',
    #     }
    #     data_id = self.env['ir.attachment'].sudo().create(ir_values)
    #     self.import_csv(data_id)