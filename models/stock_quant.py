# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class QuantPackage(models.Model):
    """ Inherit stock package to add product dimensions to the package """
    _inherit = "stock.quant.package"

    height = fields.Float(string='Height',related='product_id.height',store=True)
    height_uom_id = fields.Many2one('uom.uom', string="Height Unit of Measure",
                                    default=lambda self: self.env.ref('uom.product_uom_millimeter'),
                                    related='product_id.height_uom_id',store=True)
    width = fields.Float(string='Width',related='product_id.width',store=True)
    width_uom_id = fields.Many2one('uom.uom', string="Width unit of Measure",
                                   default=lambda self: self.env.ref('uom.product_uom_millimeter'),
                                   related='product_id.width_uom_id',store=True)
    thickness = fields.Float(string='Thickness',related='product_id.thickness',store=True)
    thickness_uom_id = fields.Many2one('uom.uom', string="Thickness Unit of Measure",
                                       default=lambda self: self.env.ref('uom.product_uom_millimeter'),
                                       related='product_id.thickness_uom_id',store=True)




