# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2020 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models, fields, api, _
from datetime import datetime, timedelta
import json
import pytz
import ast

import logging
_logger = logging.getLogger(__name__)

LOCAL_TZ = 'Europe/Stockholm'

class edi_message(models.Model):
    _inherit='edi.message'

    #obj = False    
    @api.one
    def unpack(self):
        if self.edi_type.id == self.env.ref('edi_af_krom_postcode.asok_postcode').id:
            # decode string and convert string to tuple, convert tuple to dict
            body = json.loads(self.body.decode("utf-8"))

            # Get values
            match_area = body.get('ArPostnummerGiltigForKrom')
            if match_area:
                self.env['res.partner'].browse(self.res_id).match_area = match_area  #always true
            else:
                pass       
        else:
            super(edi_message, self).unpack()

    @api.one
    def pack(self):
        if self.edi_type.id == self.env.ref('edi_af_krom_postcode.asok_postcode').id:
            if not self.model_record or self.model_record._name != 'res.partner':
                raise Warning("Appointment: Attached record is not an res.partner'! {model}".format(model=self.model_record and self.model_record._name or None))

            obj = self.model_record  #res.partner
            path = "ais-bos-regelverk/api/Krom/ArPostnummerGiltigForKrom"
            self.body = self.edi_type.type_mapping.format(
                path=path,   #boolean
                postnummer = obj.zip,            
            )
            _logger.info("Path on l66: %s" % path )
            envelope = self.env['edi.envelope'].create({
                'name': 'KROM postcode request',
                'route_id': self.route_id.id,
                'route_type': self.route_type,
                'edi_message_ids': [(6, 0, [self.id])]})
        else:
            super(edi_message, self).pack()