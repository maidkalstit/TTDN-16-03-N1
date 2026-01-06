# -*- coding: utf-8 -*-

from odoo import models, fields


class ChungChi(models.Model):
    _name = 'chung_chi'
    _description = 'Chứng chỉ'
    _rec_name = 'ten_chung_chi'

    nhan_vien_id = fields.Many2one(
        comodel_name='nhan_vien',
        string='Nhân viên',
        ondelete='cascade',
        required=True
    )
    ten_chung_chi = fields.Char('Tên chứng chỉ', required=True)
    noi_cap = fields.Char('Nơi cấp')
    ngay_cap = fields.Date('Ngày cấp')
    ngay_het_han = fields.Date('Ngày hết hạn')
    hinh_anh = fields.Binary('Hình ảnh')