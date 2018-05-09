# -*- coding: utf-8 -*-

from sqlalchemy import BigInteger, Column, String, BOOLEAN, DateTime, func
from app import db


class Testcasegroup(db.Model):

    __tablename__ = 'autotest_testcasegroup'

    id = Column(BigInteger, primary_key=True)
    module_id = Column(BigInteger, index=True, nullable=False)
    testcase_group_name = Column(String(200), nullable=False)
    testcase_type = Column(BigInteger, index=True, nullable=False,)
    testcase_desc=Column(String(500), nullable=False)
    is_active = Column(BOOLEAN, nullable=False)
    datachange_createtime = Column(DateTime(True), server_default=func.now())
    datachange_lasttime = Column(DateTime(True), index=True, onupdate=func.now())

    def __init__(self, module_id, testcase_group_name,testcase_type,testcase_desc,
                 is_active=True, datachange_createtime=None, datachange_lasttime=None, **kwargs):
        kwargs["module_id"] = module_id
        kwargs["testcase_group_name"] = testcase_group_name
        kwargs["testcase_type"] = testcase_type
        kwargs["testcase_desc"] = testcase_desc
        kwargs["is_active"] = is_active
        kwargs["datachange_createtime"] = datachange_createtime
        kwargs["datachange_lasttime"] = datachange_lasttime

        super().__init__(**kwargs)
