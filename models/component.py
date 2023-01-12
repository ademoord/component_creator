# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class ComponentMaster(models.Model):
    _name = 'component.master'
    _description = 'Component Master'

    component_ids = fields.One2many('item.master', 'component_id', string='Nama Komponen', required=True)
    # name = fields.Char(string='Nama Komponen', required=True)
    process_time = fields.Float(string='Waktu Pengerjaan Komponen', required=True)