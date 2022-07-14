from flask_wtf import FlaskForm
import wtforms as wf
from wtforms import validators


class UserForm(FlaskForm):
    username = wf.StringField("Пользыватель", validators=[wf.validators.DataRequired()])
    password = wf.PasswordField("Пароль", validators=[wf.validators.DataRequired(),
                                                      wf.validators.Length(min=8, max=30)
                                                      ])
    submit = wf.StringField("Ok")


class PostForm(FlaskForm):
    title = wf.StringField("Заголовок", validators=[wf.validators.DataRequired()])
    content = wf.TextAreaField("Текст Новости", validators=[wf.validators.DataRequired()])
    is_boom_news = wf.BooleanField("Супер новость")
    submit = wf.SubmitField("OK")




    def validate_password(self, password):
        if not super().validate():
            return False
        word = "A, E, I, O, U, Y, B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z"
        number = "1, 2, 3, 4, 5, 6, 7, 8, 9, 0"
        symbol = "!, @, #, $, %"
        if word and number and symbol not in password:
            raise validators.ValidationError("В пароле должны быть буквы и числа и спец символы")


