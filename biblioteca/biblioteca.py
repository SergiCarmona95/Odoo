#-*- coding:utf-8 -*-
from openerp import models,fields
class biblioteca_autor(models.Model):
	_name='biblioteca.autor'
	cod=fields.Integer('Cod')
	nom=fields.Char('Nombre',size=50,required=True)
	cognoms=fields.Char('Cognom',size=50,required=True)
	nacionalitat=fields.Char('Nacionalitat',size=50,required=True)
	_rec_name='cod'
class biblioteca_llibre(models.Model):
	_name='biblioteca.llibre'
	isbn=fields.Char('ISBN',size=13,required=True)
	titol=fields.Char('Titol',size=50,required=True)
	editorial=fields.Char('Editorial',size=50,required=True)
	pagines=fields.Integer('Pagines')
	_rec_name='isbn'
class biblioteca_escriu(models.Model):
	_name='biblioteca.escriu'
	isbn=fields.Many2one('biblioteca_llibre','ISBN',ondelete='cascade')
	cod=fields.Many2one('biblioteca_autor','Cod',ondelete='casacade')
	date=fields.Date('Fecha')
class biblioteca_client(models.Model):
	_name='biblioteca.client'
	cod=fields.Integer('Cod')
	dni=fields.Char('Dni',size=9,required=True)
	nom=fields.Char('Nom',size=50,required=True)
	cognom=fields.Char('Cognoms',size=50,required=True)
class biblioteca_prestec(models.Model):
	_name='biblioteca.prestec'
	isbn=fields.Many2one('biblioteca_exemplar','ISBN',ondelete='cascade')
	num_exemplar=fields.Many2one('biblioteca_exemplar','Num Exemplar',ondelete='cascade')
	client=fields.Many2one('bibliteca_client','Client',cascade='ondelete')
	data_prestec=fields.Date('Data Prestec')
	tornat=fields.Boolean('Tornat?')
	data_retorn=fields.Date('Data Retorn')
class biblioteca_exemplar(models.Model):
	_name='biblioteca.exemplar'
	isbn=fields.Many2one('biblioteca_llibre','ISBN',cascade='ondelete')
	num=fields.Integer('Num')
	prestatge=fields.Integer('Prestatge')
