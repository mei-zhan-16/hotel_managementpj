# -*- coding: utf-8 -*-

from odoo import fields,models



class HotelFloor(models.Model):

    _name = "hotel.floor"  #  ORM method 


    name = fields.Char(string="Hotel Floor")
    manager = fields.Char(string="Hotel Floor Manager")

