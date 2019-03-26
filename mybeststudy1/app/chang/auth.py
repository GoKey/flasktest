from app.chang import chang

@chang.route('/hello')
def hello():
    return "嘻嘻嘻"