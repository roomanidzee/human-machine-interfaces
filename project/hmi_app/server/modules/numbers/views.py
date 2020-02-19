# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    flash,
    render_template,
    redirect,
    request,
    url_for,
)

from server.modules.numbers.services import (
    FilesService,
    NumbersService,
    RedisService
)

numbers = Blueprint(
    'numbers_views',
    __name__,
    url_prefix='/numbers',
    template_folder='templates',
    static_folder='static'
)

file_service = FilesService('static/images')
numbers_service = NumbersService()
redis_service = RedisService()

@numbers.route(
    '/check_memory',
    methods=['GET']
)
def get_all_pictures():

    all_files = file_service.retrieve_all_files()

    file_paths = [
        url_for('numbers_views.static', filename = f'images/{elem}')
        for elem in all_files
    ]

    return render_template(
        'numbers/validate.html',
        elements = file_paths
    )


@numbers.route(
    '/get_images',
    methods=['GET']
)
def get_unique_images():

    all_files = file_service.retrieve_all_files()

    dict_for_save = numbers_service.create_dict(
        numbers=numbers_service.generate_random_numbers(),
        file_paths=[
            url_for('numbers_views.static', filename = f'images/{elem}')
            for elem in all_files
        ]
    )

    redis_service.save_dict(dict_for_save)

    return render_template(
        'numbers/index.html',
        result_dict = dict_for_save
    )


@numbers.route(
    '/validate_numbers',
    methods=['POST']
)
def validate_numbers():
    numbers = request.form['numbers']

    validate_result = redis_service.validate_for_keys(
        set(numbers.split(','))
    )

    formatted_result = [
        str(elem).replace('b', '').replace("\'", '')
        for elem in validate_result
    ]

    final_result = ','.join(formatted_result)

    if validate_result:
        flash(f'Wrong input! Missed: {formatted_result}')
        return redirect(
        url_for(
            'numbers_views.get_all_pictures'
        )
    )

    return redirect(
        url_for(
            'numbers_views.get_all_pictures'
        )
    )

