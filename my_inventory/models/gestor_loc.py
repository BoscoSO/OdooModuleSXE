# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)
class GestorLoc(models.Model):
    _name = 'gestor.loc'
    _description = 'Location'
    _order = 'name'

    name = fields.Char('Nombre', required=True)
    description = fields.Html('Descripción', sanitize=True, strip_style=False)
    posicion = fields.Char('Posición', required=True)
    inventory_ids = fields.One2many('gestor.loc.inv',  inverse_name='inventory_id',string='Inventarios',ondelete='cascade')
