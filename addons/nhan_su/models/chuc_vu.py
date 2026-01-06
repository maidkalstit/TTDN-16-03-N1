# -*- coding: utf-8 -*-

from odoo import models, fields


class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Chức vụ'
    _rec_name = 'name'

    name = fields.Char('Tên chức vụ', required=True)
    ma_chuc_vu = fields.Char('Mã chức vụ')
    mo_ta = fields.Text('Mô tả công việc')