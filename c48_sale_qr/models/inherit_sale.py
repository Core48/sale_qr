from odoo import api, fields, models, _

class InheritQuotatins(models.Model):
    _inherit = 'sale.order'

    qr = fields.Binary(string='QR')
