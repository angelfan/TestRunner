# -*- coding: utf-8 -*-

from app import db


class QuestionCategory(db.Model):
    __tablename__ = 'question_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    datachange_createtime = db.Column(db.DateTime(True), server_default=db.func.now())
    datachange_lasttime = db.Column(db.DateTime(True), index=True, onupdate=db.func.now())

    def __repr__(self):
        return self.name


class QuestionAnswer(db.Model):
    __tablename__ = 'question_answer'

    id = db.Column(db.Integer, primary_key=True)
    question_category_id = db.Column(db.Integer, db.ForeignKey('question_category.id'), nullable=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    origin = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    datachange_createtime = db.Column(db.DateTime(True), server_default=db.func.now())
    datachange_lasttime = db.Column(db.DateTime(True), index=True, onupdate=db.func.now())

    @property
    def question_category(self):
        if not self.question_category_id:
            return None
        return QuestionCategory.query.get(self.question_category_id)

    @question_category.setter
    def question_category(self, category):
        self.question_category_id = category.id