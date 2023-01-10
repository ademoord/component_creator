# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

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

# class CustomImport(models.Model):
#     _name = 'custom.import'
#     _description = 'Custom Import'

#     item_name = fields.Char(string='Nama Item', required=True)
#     component_name = fields.Many2one('component.master', string='Nama Komponen')
#     start_time = fields.Datetime(string='Tanggal Mulai Pengerjaan', required=True)
#     processing_time = fields.Float(string='Processing Time', required=True)
#     component_percentage = fields.Float(string='Bobot Persentase Komponen (%)', digits=(4,2), required=True)

#     @api.model
#     def create(self, vals):
#         if 'component_name' not in vals or not vals['component_name']:
#             component = self.env['component.master'].create({'name': 'Komponen Baru'})
#             vals['component_name'] = component.id
#         return super().create(vals)

