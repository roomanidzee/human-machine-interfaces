# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

index = Blueprint(
    'base_pages',
    __name__,
    url_prefix='/index',
    template_folder='templates',
    static_folder='static'
)

@index.route(
    '/',
    methods=['GET'],
)
def home_page():
    return render_template('home/index.html')
