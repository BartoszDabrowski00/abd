from flask import Blueprint, render_template

from web.models.models import Driver

driver = Blueprint("Single driver view", __name__)


@driver.get("/drivers/<string:login>")
def show_driver(login):
    driver = Driver.query.filter(Driver.login == login).first()
    return render_template("drivers/index.html", driver=driver)
