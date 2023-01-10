# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
import csv, base64

class ItemMaster(models.Model):
    _name = 'item.master'
    _description = 'Item Master'

    name = fields.Char(string='Nama Item', required=True)
    component_name = fields.Many2one('component.master', string='Nama Komponen', required=True)
    percentage = fields.Float(string='Bobot Persentase Komponen (%)', digits=(4,2), required=True)
    processing_start_date = fields.Date(string='Tanggal Mulai Pengerjaan', required=True)
    finished_real_date = fields.Date(string='Real Tanggal Selesai', required=True)

    @api.constrains('percentage')
    def _check_percent(self):
        print('_check_percent')
        if self.percentage > 100:
            raise exceptions.ValidationError("Maaf, bobot persentase harus dalam range 0-100%.")

    
    def import_csv(self, csv_file):

        print(csv_file)
        print(csv_file)
        print(csv_file)

        with open(csv_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))

        reader = csv.reader(test)
        next(reader)
        for row in reader:
            record = {
                'name'                  : row[0],
                'component_name'        : row[1],
                'percentage'            : row[2],
                'processing_start_date' : row[3],
                'finished_real_date'    : row[4],
            }
            self.env['item.master'].create(record)

    def action_import_csv(self):

        outfile = open('/mnt/c/Temp/new-data.csv', 'r')
        file_base64 = base64.b64encode(bytes(outfile.read(), encoding='utf8'))
        outfile.close()
        attachment = {
            'name'          : 'new-data.csv',
            'datas'         : file_base64,
            # 'datas_fname'   : 'new-data.csv',
        }
        attachment_id = self.env['ir.attachment'].create(attachment)
        print(attachment_id.datas)
        csv_file = attachment_id.datas.decode('base64')
        self.import_csv(csv_file)


