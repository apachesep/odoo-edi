# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
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

{
    'name': 'EDI AF Appointment',
    'version': '0.1',
    'category': 'edi',
    'summary': 'EDI AF Appointment - support for appointments ',
    'licence': 'AGPL-3',
    'description': """ """,
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': [
        'edi_route',
        'calendar_af', 
        'edi_route_ipf', 
        'af_security'],
    'external_dependencies': {
    },
    'data': [
        'security/ir.model.access.csv',
        'data/edi_route_data.xml',
        'data/edi.ace_queue.csv',
        'data/edi.ace_errand.csv',
        'views/edi_af_appointment_views.xml',
        'views/edi_message_view.xml',
        'data/res_users.xml'
    ],
    'application': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4s:softtabstop=4:shiftwidth=4:
