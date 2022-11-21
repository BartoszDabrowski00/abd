from flask import Blueprint, render_template

from web.models.models import Complaint

complaint = Blueprint("Single complaint view", __name__)


@complaint.get("/complaints/<string:id>")
def show_complaint(id):
    complaint = Complaint.query.filter(Complaint.complaint_id == id).first()
    return render_template("complaint/index.html", complaint=complaint)
