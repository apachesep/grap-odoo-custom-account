# Copyright (C) 2019-Today GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountFiscalPositionTaxTemplate(models.Model):
    _inherit = "account.fiscal.position.tax.template"

    active = fields.Boolean("Active", default=True)
