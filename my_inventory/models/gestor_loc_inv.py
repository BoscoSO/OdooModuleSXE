# -*- coding: utf-8 -*-
from odoo import api, models, fields
from datetime import datetime, timedelta



class GestorLocInv(models.Model):
    _name = 'gestor.loc.inv'
    _description = 'Inventory'

    def _fecha_por_defecto(self):
        return datetime.now().strftime('%Y-%m-%d') 

    name = fields.Char('Nombre', required=True)
    description = fields.Html('Descripción', sanitize=True, strip_style=False)
    fecha_inicio = fields.Date('Fecha de registro',default=_fecha_por_defecto)
    inventory_id = fields.Many2one('gestor.loc', string='Localización', ondelete='cascade')
    item_ids = fields.One2many('gestor.loc.inv.item',  inverse_name='item_id',string='Items', ondelete='cascade')

    currency_id = fields.Many2one('res.currency', string='Currency')


    @api.multi
    def valor_total(self):
        for record in self:
            total=0.0
            for item in record.item_ids:
                total += item.price * item.units_stock
            record.valor_total_inv=total


    valor_total_inv = fields.Monetary('Valor total del inventario',compute=valor_total,store=False,currency_field='currency_id')

    #valor_total_inv = fields.Float('Valor total del inventario', compute=valor_total,store=False)
    