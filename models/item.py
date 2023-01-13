# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
import csv
import base64
import io
import logging

_logger = logging.getLogger(__name__)

class ItemMaster(models.Model):
    _name = 'item.master'
    _description = 'Item Master'

    name = fields.Char(string='Nama Item', required=True)
    component_id = fields.Many2one('component.master', string='Nama Komponen', required=True)
    percentage = fields.Float(string='Bobot Persentase Komponen (%)', digits=(4,2), required=True)
    processing_start_date = fields.Date(string='Tanggal Mulai Pengerjaan', required=True)
    finished_real_date = fields.Date(string='Real Tanggal Selesai', required=True)
    # attachment_ids = fields.Many2one(comodel_name='ir.attachment', string='Bismillah')

    @api.constrains('percentage')
    def _check_percent(self):
        print('_check_percent')
        if self.percentage > 100:
            raise exceptions.ValidationError("Maaf, bobot persentase harus dalam range 0-100%.")
        
    def import_csv(self, attachment):
       csv_data = base64.b64decode(attachment.datas).decode('utf-8')
       csv_file = io.StringIO(csv_data)
     
       reader = csv.reader(csv_file)
       next(reader)
       for row in reader:
           record = {
               'id'                    : row[0],
               'name'                  : row[1],
               'component_id'          : row[2],
               'percentage'            : row[3],
               'processing_start_date' : row[4],
               'finished_real_date'    : row[5],
           }
           existing_rec = self.env['item.master'].browse(record['id'])
           if not existing_rec:
               self.env['item.master'].create(record)

    def action_import_csv(self):
        outfile = open('test.csv', 'rb')
        data_record = outfile.read()
        ir_values = {
            'name': 'test.csv',
            'datas': base64.b64encode(data_record),
            'type': 'binary',
            'store_fname': 'test.csv',
            'mimetype': 'text/csv',
        }

        data_id = self.env['ir.attachment'].sudo().create(ir_values)
        self.import_csv(data_id)
        

