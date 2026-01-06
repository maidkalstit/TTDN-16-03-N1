# -*- coding: utf-8 -*-

from odoo import models, fields


class LichSuCongTac(models.Model):
    _name = 'lich_su_cong_tac'
    _description = 'Lịch sử công tác'
    _rec_name = 'vi_tri_cu'

    nhan_vien_id = fields.Many2one(
        comodel_name='nhan_vien',
        string='Nhân viên',
        ondelete='cascade',
        required=True
    )
    tu_ngay = fields.Date('Từ ngày', required=True)
    den_ngay = fields.Date('Đến ngày')
    vi_tri_cu = fields.Char('Vị trí cũ', required=True)
    phong_ban_cu = fields.Char('Phòng ban cũ')
    mo_ta = fields.Text('Mô tả')