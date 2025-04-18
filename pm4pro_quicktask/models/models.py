# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pm4pro_quicktask(models.Model):
#     _name = 'pm4pro_quicktask.pm4pro_quicktask'
#     _description = 'pm4pro_quicktask.pm4pro_quicktask'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
