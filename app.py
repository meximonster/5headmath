from flask import Flask, render_template, request, flash
from wtforms import Form, FloatField, validators
import compute

app = Flask(__name__)
sumMessage = "Sum should always be between 19.5 and 29."

# Model
class InputForm(Form):
    al_lower = FloatField(label="Arch length :", validators=[validators.Optional()])
    s_lower = FloatField(label="Sum of incisor widths :", validators=[validators.InputRequired(), validators.NumberRange(min=19.5, max=29, message=sumMessage)])
    al_upper = FloatField(label="Arch length :", validators=[validators.Optional()])
    s_upper = FloatField(label="Sum of incisor widths :", validators=[validators.Optional(), validators.NumberRange(min=19.5, max=29, message=sumMessage)])

# View
@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        al_l = form.al_lower.data
        s_l = form.s_lower.data
        al_u = form.al_upper.data
        s_u = form.s_upper.data
        res = compute.check(al_l,al_u,s_u)
        slr = compute.switch(s_l)
        if res == "lower":
            xl = compute.compute_lower(al_l,s_l,slr)
            return render_template("view_output_lower.html", form=form, xl=xl, slr=slr, s_l=s_l)
        elif res == "upper":
            xu = compute.compute_upper(al_u, s_u, s_l,slr)
            return render_template("view_output_upper.html", form=form, xu=xu, slr=slr, s_l=s_l)
        elif res == "both":
            xl = compute.compute_lower(al_l,s_l,slr)
            xu = compute.compute_upper(al_u, s_u, s_l,slr)
            return render_template("view_output.html", form=form, xu=xu, xl=xl, slr=slr, s_l=s_l)
        else:
            flash("Not enough data to perform operations.", "error")
            return render_template("view_input.html", form=form)
    else:
        return render_template("view_input.html", form=form)

if __name__ == '__main__':
    app.secret_key = 'secret'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=8080, debug=True)
