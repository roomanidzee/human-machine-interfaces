# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
)

from server.modules.numbers import services

numbers = Blueprint(
    'numbers_views',
    __name__,
    url_prefix='/numbers',
    template_folder='templates'
)

@numbers.route(
    '/check_memory',
    methods=['GET']
)
def get_all_pictures():
    file_service = services.files.FilesService('images')

    return render_template(
        'numbers/validate.html',
        elements = file_service.retrieve_all_files()
    )


@numbers.route(
    '/get_images',
    methods=['GET']
)
def get_unique_images():
    numbers_services = services.numbers.NumbersService()
    redis_service = services.redis.RedisService()
    file_service = services.files.FilesService('images')

    all_files = file_service.retrieve_all_files()

    dict_for_save = numbers_services.create_dict(
        numbers=numbers_services.generate_random_numbers(),
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

    redis_service = services.redis.RedisService()

    validate_result = redis_service.validate_for_keys(
        set(numbers.split(','))
    )

    return redirect(
        url_for(
            'get_all_pictures',
            validate_result=validate_result
        )
    )

