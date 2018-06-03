# -*- coding: utf-8 -*-

from sqlalchemy import BigInteger, Column, String, BOOLEAN, DateTime, func
from sqlalchemy.dialects.mysql.json import JSON
from app import db
from .Module import  Module


class Interface(db.Model):
    __tablename__ = 'autotest_Interface'

    id = Column(BigInteger, primary_key=True)
    module_id = Column(BigInteger)
    interface_name = Column(String(200), nullable=False, index=True)
    interface_url = Column(String(200), nullable=False)
    interface_header = Column(JSON, nullable=True)
    # interface_query = Column(JSON, nullable=True)
    interface_body = Column(JSON, nullable=True)
    interface_method = Column(String(10), nullable=False)
    is_active = Column(BOOLEAN, nullable=False, default=True)
    datachange_createtime = Column(DateTime(True), server_default=func.now())
    datachange_lasttime = Column(DateTime(True), index=True, onupdate=func.now())

    @property
    def module(self):
        return Module.query.get(self.module_id)

    @module.setter
    def module(self, module):
        self.module_id = module.id

    @classmethod
    def get_all_oder_by_module(cls):
        return cls.query.filter_by(is_active=True).order_by(
            cls.module_id)
