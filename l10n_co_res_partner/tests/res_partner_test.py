# -*- coding: utf-8 -*-

from odoo.tests import common

class TestResPartner(common.TransactionCase):


	def test_create_res_partner_dv(self):
		test_check_dev_ = self.env['res.partner']._check_dv('1113310128')
		self.assertEquals(test_check_dev_, '1113310128-5', "Calculo digito verificador mal")



	def test_check_ident_num(self):
		test_check_ident_num_ = self.env['res.partner']._check_ident_num()
		self.assertIsNotNone(test_check_ident_num_, '1113310128', "Calculo digito verificador mal")


	def test_check_doc_type(self):
		test_check_doc_type_ = self.env['res.partner']._checkDocType()
		self.assertIsNotNone(test_check_doc_type_, '1113310128', "Calculo digito verificador mal")
