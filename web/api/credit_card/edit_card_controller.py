from flask import Blueprint, render_template, request

from web import db
from web.models.models import CreditCard

edit_card = Blueprint("Edit credit card view", __name__)


@edit_card.get("/cards/<string:number>/edit")
def show_edit_credit_card_panel(number):
    credit_card = CreditCard.query.filter(CreditCard.card_number == number).first()
    return render_template("card_edit/index.html", credit_card=credit_card, edit_card=edit_card_action)


@edit_card.post("/card/edit")
def edit_card_action():
    session = db.session
    credit_card = CreditCard.query.filter(CreditCard.card_number == request.form.get('card_number')).first()
    if credit_card:
        if cvc := request.form.get('cvc', ''):
            credit_card.cvc = cvc
        if expiration := request.form.get('expiration', ''):
            credit_card.expiration_date = expiration
        session.add(credit_card)
    session.commit()
    return render_template("credit_card/index.html", card=credit_card)
