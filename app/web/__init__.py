"""
存放所有web相关的通用代码
"""

from flask import jsonify, Blueprint

#创建蓝图，web
web = Blueprint('web',__name__)

from app.web import book