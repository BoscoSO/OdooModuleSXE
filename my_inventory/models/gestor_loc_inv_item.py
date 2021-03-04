# -*- coding: utf-8 -*-
from odoo import api, models, fields
from odoo.exceptions import ValidationError

class GestorLocInvItem(models.Model):
    _name = 'gestor.loc.inv.item'
    _description = 'Item'

    name = fields.Char('Nombre', required=True)
    description = fields.Html('Descripción', sanitize=True, strip_style=False)
    units_stock= fields.Integer('Unidades',default=0)
    
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Monetary('Precio item',currency_field='currency_id')

    item_image = fields.Binary('Referencia')
    
    item_id = fields.Many2one('gestor.loc.inv', string='Inventario', ondelete='cascade')

    @api.multi
    def reponer_stock(self):
        self.units_stock+=10


    @api.multi
    def valor_units(self):
        for record in self:
            record.total_value_perunits=record.units_stock*record.price


    total_value_perunits = fields.Monetary('Valor total ',compute=valor_units,store=False,currency_field='currency_id')

    @api.constrains('units_stock')
    def _check_book_id(self):
         for record in self:
            if record.units_stock<0:
                raise models.ValidationError('No es una cantidad válida') 
