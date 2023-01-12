# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
import csv, base64, io

class ItemMaster(models.Model):
    _name = 'item.master'
    _description = 'Item Master'

    name = fields.Char(string='Nama Item', required=True)
    component_id = fields.Many2one('component.master', string='Nama Komponen', required=True)
    percentage = fields.Float(string='Bobot Persentase Komponen (%)', digits=(4,2), required=True)
    processing_start_date = fields.Date(string='Tanggal Mulai Pengerjaan', required=True)
    finished_real_date = fields.Date(string='Real Tanggal Selesai', required=True)

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
            'store_fname': base64.b64encode(data_record),
            'mimetype': 'text/csv',
        }
        data_id = self.env['ir.attachment'].sudo().create(ir_values)
        # print(ir_values)
        self.import_csv(data_id)
  




    # def import_csv(self, csv_file):

    #     try:
    #         csvfile = open(csv_file, newline='')
    #         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #         next(spamreader)
    #     except FileNotFoundError as e:
    #         print("Eweuh file na", str(e))
    #     except csv.Error as e:
    #         print("Teu kabaca", str(e))
        
    #     for row in spamreader:
    #         record = {
    #             'name'                  : row[0],
    #             'component_name'        : row[1],
    #             'percentage'            : row[2],
    #             'processing_start_date' : row[3],
    #             'finished_real_date'    : row[4],
    #         }
    #         self.env['item.master'].create(record)

    # def action_import_csv(self):

    #     with open('test.csv', newline='') as outfile:
    #         data_file = outfile.read()
    #         spamreader = csv.reader(outfile, delimiter=' ', quotechar='|')
    #         for row in spamreader:
    #             print(', '.join(row))

    #     data_bytes = data_file.encode('utf-8')
    #     data_record = base64.b64encode(data_bytes)
    #     ir_values = {
    #         'name': 'test.csv',
    #         'type': 'binary',
    #         'datas': data_record,
    #         'store_fname': data_record,
    #         'mimetype': 'text/csv',
    #     }
    #     data_id = self.env['ir.attachment'].sudo().create(ir_values)
    #     self.import_csv(data_id)

        
        
        
        
        
        
        
        
        # outfile = open('test.csv', 'r')
        # file_base64 = base64.b64encode(bytes(outfile.read(), encoding='utf8'))
        # outfile.close()
        # attachment = {
        #     'name'          : 'new-data.csv',
        #     'datas'         : file_base64,
        #     # 'datas_fname'   : 'new-data.csv',
        # }
        # attachment_id = self.env['ir.attachment'].create(attachment)
        # print(attachment_id.datas)
        