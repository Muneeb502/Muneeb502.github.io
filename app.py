from flask import Flask, request, jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route("/submitform", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            subject = request.form["subject"]
            message = request.form["message"]

            with sql.connect("portfoliodata.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO student (name, email, subject, message) VALUES (?, ?, ?, ?)",
                            (name, email, subject, message))
                con.commit()

            return jsonify({"message": "Form has been submitted. Thank you for your feedback!"})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Only POST method is allowed for this endpoint."}), 405

if __name__ == "__main__":
    app.run(debug=True)
