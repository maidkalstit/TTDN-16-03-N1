from odoo import models, fields, api

class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Bảng chứa thông tin phòng ban'
    _order = 'ma_phong_ban'
    _rec_name = 'ten_phong_ban'

    ten_phong_ban = fields.Text("Tên phòng ban", required=True)
    ma_phong_ban = fields.Char("Mã phòng ban", required=True)
    nhan_vien_ids = fields.Many2many('nhan_vien', 'phong_ban_nhan_vien_rel', 'phong_ban_id', 'nhan_vien_id', string="Nhân viên")