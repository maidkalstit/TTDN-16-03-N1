from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ma_dinh_danh'

    name = fields.Char("Tên nhân viên")
    ma_dinh_danh = fields.Char("Mã định danh", required=True, unique=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    so_bhxh = fields.Char("Số BHXH")
    dia_chi_thuong_tru = fields.Char("Địa chỉ thường trú")
    luong_co_ban = fields.Float("Lương cơ bản")
    chuc_vu_id = fields.Many2one(
        comodel_name='chuc_vu',
        string='Chức vụ'
    )
    phong_ban_ids = fields.Many2many(
        'phong_ban',
        'phong_ban_nhan_vien_rel',
        'nhan_vien_id',
        'phong_ban_id',
        string="Phòng ban"
    )
    # One2many relations
    lich_su_cong_tac_ids = fields.One2many(
        comodel_name='lich_su_cong_tac',
        inverse_name='nhan_vien_id',
        string='Lịch sử công tác'
    )
    chung_chi_ids = fields.One2many(
        comodel_name='chung_chi',
        inverse_name='nhan_vien_id',
        string='Chứng chỉ'
    )
    cham_cong_ids = fields.One2many(
        comodel_name='cham_cong',
        inverse_name='nhan_vien_id',
        string='Chấm công'
    )