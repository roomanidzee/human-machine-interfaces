# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
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
    template_folder='templates'
)

file_service = FilesService('images')
numbers_service = NumbersService()
redis_service = RedisService()

@numbers.route(
    '/check_memory',
    methods=['GET']
)
def get_all_pictures():

    return render_template(
        'numbers/validate.html',
        elements = file_service.retrieve_all_files()
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
            str(elem)
            for elem in all_files
        ]
    )

    redis_service.save_dict(dict_for_save)

    return render_template(
        'numbers/index.html',
        elements = list(dict_for_save.values())
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

    return redirect(
        url_for(
            'numbers_views.get_all_pictures',
            validate_result=validate_result
        )
    )

