# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date


class Partner(models.Model):
    _inherit = 'res.partner'

    customer_status = fields.Selection([('draft', 'Draft'), ('approved', 'Approved')], required=True, default='draft')
    approval_user_id = fields.Many2one(string="Approval User", comodel_name='res.users')
    approval_date = fields.Date(string="Approval Date")

    # Function for Customer Approval
    def set_to_approved(self):
        self.ensure_one()
        self.write({
        	'customer_status': 'approved',
        	'approval_user_id' : self.env.user.id,
        	'approval_date' : date.today()
        })

    # Function for Rest to Draft
    def rest_to_draft(self):
        self.ensure_one()
        self.write({
        	'customer_status': 'draft',
        	'approval_user_id' : None,
        	'approval_date' : ''
        })