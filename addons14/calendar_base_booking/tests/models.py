# Copyright 2020 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models


class ResPartner(models.Model):
    _inherit = ["bookable.mixin", "res.partner"]
    _name = "res.partner"
