#-*- coding: utf-8 -*-
from openerp import models, fields
class Milibro(models.Model):
	_name= 'milibro'
	titol = fields.Char('Titol',size=150,  required=True)
	pagines =fields.Integer('Pagines')
	autor = fields.Char('Autor',size=150)
	editorial = fields.Char('Editorial',size=150)
