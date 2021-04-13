from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
import compute

app = Flask(__name__)

# Model
class InputForm(Form):
    al_upper = FloatField(validators=[validators.InputRequired()])
    s_upper = FloatField(validators=[validators.InputRequired()])
    al_lower = FloatField(validators=[validators.InputRequired()])
    s_lower = FloatField(validators=[validators.InputRequired()])

# View
@app.route('/5headmath', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        al_u = form.al_upper.data
        s_u = form.s_upper.data
        al_l = form.al_lower.data
        s_l = form.s_lower.data
        xu = compute.compute_upper(al_u, s_u, s_l)
        xl = compute.compute_lower(al_l,s_l)
        return render_template("view_output.html", form=form, xu=xu, xl=xl)
    else:
        return render_template("view_input.html", form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
