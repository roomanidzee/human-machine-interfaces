# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    flash,
    render_template,
    redirect,
    request,
    url_for,
)

from server.modules.file_manager.services.factory import process_command

file_manager = Blueprint(
    'file_manager_views',
    __name__,
    url_prefix='/file_manager',
    template_folder='templates',
    static_folder='static'
)

@file_manager.route(
    '/index',
    methods=['GET']
)
def show_page():

    return render_template(
        'file_manager/index.html',
        elem = process_command('list')
    )

@file_manager.route(
    '/process',
    methods=['POST']
)
def submit_command():
    command = request.form['command']

    return render_template(
        'file_manager/index.html',
        elem = process_command(command)
    )
