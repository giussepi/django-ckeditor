# -*- coding: utf-8 -*-
""" ckeditor_uploader' settings """

from django.conf import settings


CKEDITOR_UPLOADER_RENAME_IMAGES = getattr(
    settings, 'CKEDITOR_UPLOADER_RENAME_IMAGES', False)
