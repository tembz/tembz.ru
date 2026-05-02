from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("main.html")

@main.route("/bk/docs")
def report_html():
    return render_template("report.html")

@main.route("/bk/schedule/docs")
def schedule_docs():
    return render_template("schedule-docs.html")

@main.route("/bk/docs/methods")
def docs_html():
    return render_template("doc.html")

@main.route("/bk/docs/errors")
def errors_html():
    return render_template("doc_errors.html")

