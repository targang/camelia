from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import (
    BooleanField,
    HiddenField,
    IntegerField,
    PasswordField,
    StringField,
    SubmitField,
    SelectField,
    RadioField,
)
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets.html5 import NumberInput

from . import app

# csrf = CSRFProtect(app)


class RegisterForm(FlaskForm):
    reg_email = StringField(
        "Эл. почта",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Адрес почты"},
    )
    reg_submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    login_email = StringField(
        "Эл. почта",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Адрес почты"},
    )
    login_password = PasswordField(
        "Пароль",
        validators=[
            DataRequired(),
            Length(min=6, message="Пароль должен быть не короче 6 символов"),
        ],
        render_kw={"placeholder": "******"},
    )
    login_remember = BooleanField("Запомнить меня", default="checked")
    login_submit = SubmitField("Войти")


class AddToCartForm(FlaskForm):
    product_id = HiddenField()
    product_count = IntegerField(
        "Количество",
        validators=[DataRequired()],
        widget=NumberInput(min=1),
        render_kw={"style": "width: 70px"},
    )
    submit_add = SubmitField("Добавить в корзину")


class CheckoutForm(FlaskForm):
    checkout_name = StringField(
        "Имя", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"},
    )
    checkout_surname = StringField(
        "Фамилия",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введите фамилию"},
    )
    checkout_phone = StringField(
        "Телефон",
        validators=[DataRequired()],
        render_kw={"placeholder": "Номер телефона"},
    )
    checkout_email = StringField(
        "Эл. почта",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Адрес почты"},
    )
    checkout_country = SelectField("Страна", choices=[(1, "Россия"), (2, "Украина")])
    checkout_city = SelectField("Населенный пункт")
    checkout_address = StringField("Адрес", validators=[DataRequired()])
    checkout_postcode = IntegerField("Индекс", validators=[DataRequired()])
    checkout_service = RadioField("Служба доставки", choices=[(1, "СДЭК"), (2, "Boxberry")])
    checkout_payment = RadioField("Способ оплаты", choices=[])
