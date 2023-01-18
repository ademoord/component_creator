# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
import csv, base64

class ServiceMaster(models.Model):
    _name = 'service.master'
    _description = 'Service Master'
    
    name = fields.Char(string="Nama Layanan", required=True)
    emp_sum = fields.Float(string="Jumlah Keperluan Karyawan", required=True)
    desc = fields.Char(string="Deskripsi Layanan", required=True)
    
    def import_csv(self, attachment):
       csv_data = base64.b64decode(attachment.datas).decode('utf-8')
       
       vals = {}       
       with open('test.csv', 'r') as csvfile:
           csvreader = csv.reader(csvfile)
           next(csvreader)
           for row in csvreader:
               vals = {
                'id'                    : row[0],
                'name'                  : row[1],
                'component_id'          : row[2],
                'percentage'            : row[3],
                'processing_start_date' : row[4],
                'finished_real_date'    : row[5],                 
               }
               existing_rec = self.env['item.master'].browse(vals['id'])
               if existing_rec:
                   self.env['item.master'].create(vals)