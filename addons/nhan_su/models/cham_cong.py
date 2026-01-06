# -*- coding: utf-8 -*-

from odoo import models, fields


class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm công'
    _rec_name = 'ngay'

    nhan_vien_id = fields.Many2one(
        comodel_name='nhan_vien',
        string='Nhân viên',
        ondelete='cascade',
        required=True
    )
    ngay = fields.Date('Ngày', required=True)
    gio_vao = fields.Float('Giờ vào')
    gio_ra = fields.Float('Giờ ra')
    trang_thai = fields.Selection(
        selection=[
            ('present', 'Có mặt'),
            ('absent', 'Vắng mặt'),
            ('late', 'Đi muộn'),
            ('early', 'Về sớm'),
        ],
        string='Trạng thái',
        default='present'
    )