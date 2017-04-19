#-*- coding: utf-8 -*-
from openerp import models, fields
class taller_propietari(models.Model):
	_name='taller.propietari'
	nom= fields.Char('Nombre',size=150,required=True)
	telefon=fields.Integer('Telefono',size=9)
	adreca=fields.Char('Adreca',size=50)
	_rec_name='nom'
class taller_cotxes (models.Model):
	_name='taller.cotxes'
	tipus=fields.Selection([('cotxe','Cotxe'),('moto','Moto'),('camion','Camion')])
	marca=fields.Char('Marca',size=50)
	modelo=fields.Char('Model',size=50)
	color=fields.Char('Color',size=10)
	portes=fields.Integer('Portes')
	matricula=fields.Char('Matricula',size=7)
	numbastidor=fields.Char('NumBastidor',size=20)
	combustible=fields.Selection([('gasolina','Gasolina'),('diesel','Diesel'),('electrico','Electrico')])
	comentaris=fields.Text('Comentaris')
	fecha=fields.Date('Fecha Entrada')
	reparat=fields.Boolean('Reparat?')
	fechaSalida=fields.Date('Fecha Salida')
	propietari= fields.Many2one('taller.propietari','Propietari',ondelete='cascade')
	_rec_name="matricula"
	def change_color(self):
		for record in self:
			if record.reparat==True:
				record.colorKanban=1
			elif record.reparat==False:
				record.colorKanban=2
	colorKanban=fields.Integer('Index Color',compute='change_color')
class taller_mecanic (models.Model):
	_name="taller.mecanic"
	dni=fields.Integer('Dni',size=9)
	nomMecanic=fields.Char('NomMecanic',size=50)
	cognomMecanic=fields.Char('CognomMecanic',size=50)
	rep=fields.Many2many(comodel_name='taller.cotxes',
				relation='reparacion',
				column1='dni',
				column2='matricula')
