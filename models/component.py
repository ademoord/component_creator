# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class ComponentMaster(models.Model):
    _name = 'component.master'
    _description = 'Component Master'

    name = fields.Char(string='Nama Komponen', required=True)
    process_time = fields.Float(string='Waktu Pengerjaan Komponen', required=True)

