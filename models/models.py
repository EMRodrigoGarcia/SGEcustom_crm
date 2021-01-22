from odoo import models, fields


class Visit(models.Model):
     _name = 'custom_crm.visit'
     _description = 'Visit'

     name = fields.Char(string='Descripción')
     customer = fields.Char(string='Cliente')
     date = fields.Datetime(string='Fecha')
     type = fields.Selection([('P', 'Presentacion'), ('W', 'Whatsapp'), ('T', 'Telefónica')], string = 'Tipo', required=True)
     done = fields.Boolean(string='Realizado', readonly=True)