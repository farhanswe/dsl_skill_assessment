# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class skill_assessment(models.Model):
#     _name = 'skill_assessment.skill_assessment'
#     _description = 'skill_assessment.skill_assessment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
