#-*- coding: utf-8 -*-
from openerp import models, fields
class Milibro2(models.Model):
	_inherit= 'milibro'
	isbn = fields.Char('ISBN',size=15,required=True)
	preu = fields.Float('Preu',(3,2))
	resum = fields.Text('Resum')
	data = fields.Date('Fecha')
