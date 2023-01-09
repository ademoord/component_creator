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
