from marshmallow_sqlalchemy import ModelSchema
from .models import Article

""" Schemas to connect the models with the views
"""


class ArticleSchema(ModelSchema):
    class Meta:
        model = Article
