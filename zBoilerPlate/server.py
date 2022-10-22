from flask_app import app
from flask_app.controllers import db_query_controller, posting_and_session_controller, routing_practice_controller


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'NOPE, TRY AGAIN'
if __name__ == "__main__":
  app.run(debug=True, port=5000)