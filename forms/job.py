from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    team_leader = IntegerField("TeamLead ID")
    work_size = IntegerField("Объем работы")
    collaborators = StringField('Cотрудники')
    is_finished = BooleanField("Завершена")
    submit = SubmitField('Применить')
