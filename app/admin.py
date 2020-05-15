import os
import random

from flask import url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField

from . import app
from .models import Category, Product, db

admin = Admin(app)


class ProductView(ModelView):
    form_extra_fields = {
        "image": ImageUploadField("Изображение", base_path=app.static_folder)
    }
    form_widget_args = {"imagepath": {"readonly": True, "style": "visibility: hidden"}}
    column_labels = {
        "imagepath": "",
        "vendor_code": "Артикул",
        "title": "Название",
        "description": "Описание",
        "price": "Цена",
        "weight": "Вес",
    }

    def _change_path_data(self, _form):
        try:
            storage_file = _form.image.data

            if storage_file is not None:
                ext = storage_file.filename.split(".")[-1]
                path = f"{_form.vendor_code.data}-image.{ext}"

                savedpath = os.path.join(app.static_folder, "img", "products", path)
                storage_file.save(savedpath)
                _form.imagepath.data = f"img/products/{path}"

                del _form.image

        except Exception as ex:
            pass

        return _form

    def edit_form(self, obj=None):
        return self._change_path_data(super(ProductView, self).edit_form(obj))

    def create_form(self, obj=None):
        return self._change_path_data(super(ProductView, self).create_form(obj))


admin.add_view(ProductView(Product, db.session, name="Товары"))
admin.add_view(ModelView(Category, db.session, name="Категории"))
