from application import app

@app.route('/', methods=["GET"])
def index():
    return 'Register Metadata'