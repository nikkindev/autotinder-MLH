from flask import Flask, render_template, abort, redirect, url_for
from clarifai_basic import ClarifaiCustomModel
import random


app = Flask(__name__)

app.debug=True

faces=["ZiH44Kzb.jpg", "b4lTCFnb.jpg", "6gF7qgfb.jpg", "YESoPwVb.jpg", "kmAHkQ5b.jpg", "1DUCmWJb.jpg", "HyiIBJLb.jpg", "NLNjsbeb.jpg", "nNw8uQQb.jpg", "ixTZhxXb.jpg", "ywX2l1eb.jpg", "2GKbAiGb.jpg", "lQU2zrOb.jpg", "QbdI47cb.jpg", "6OT9wRVb.jpg", "evnJaGlb.jpg", "DwUAfPZb.jpg", "9MQg5M9b.jpg", "EYuO4Nab.jpg", "VmZAYbRb.jpg", "jTDBg2kb.jpg", "YB0VCJLb.jpg", "Cj41gzCb.jpg", "y00gcypb.jpg", "1I77YUlb.jpg", "pJfU2x6b.jpg", "h73iEIAb.jpg", "V4e9zuTb.jpg", "XcquXNFb.jpg", "RKEAkmvb.jpg", "FGMZAuJb.jpg", "FKqwa7ab.jpg", "LcTp602b.jpg", "erwpGnYb.jpg", "KuxtEDDb.jpg", "Ct2RLrsb.jpg", "wCCGu4Hb.jpg", "9wzZjUob.jpg", "y2Ikzrpb.jpg", "77NQF0gb.jpg", "BsxRcirb.jpg", "D1NDO2gb.jpg", "ETsYcD6b.jpg", "YJ3yqfHb.jpg", "lq9AzDsb.jpg", "xmmrKrUb.jpg", "qSdA3Irb.jpg", "85W3KmYb.jpg", "p00Mt1Xb.jpg", "QsG5AC0b.jpg", "xM6hqBIb.jpg", "XPa3hlrb.jpg", "8zdVGRfb.jpg", "6Y6OoXVb.jpg", "gJ6xn2sb.jpg", "xTLL3xzb.jpg", "k8wKc3ub.jpg", "Xkh3uovb.jpg", "0rTBtd8b.jpg", "nov8jeeb.jpg"]
concept = ClarifaiCustomModel()

@app.route("/")
def hello():
    rand=random.choice(faces)
    try:
        result=concept.predict('http://i.imgur.com/r/%s'%(rand),'hot')
        yes_per=result['urls'][0]['score']*100
        no_per=100-yes_per 
    except:
        yes_per=50
        no_per=100-yes_per    
    return render_template('tinder.html',yes_per=yes_per,no_per=no_per,rand=rand)

@app.route("/<name>/<liked>")
def ilike(name,liked):
    try:
        if liked=='yes':
            concept.positive('http://i.imgur.com/r/%s'%(name),'hot')
        else:
            concept.negative('http://i.imgur.com/r/%s'%(name),'hot')
        concept.train('hot')
        return redirect(url_for('hello'))
    except:
        

if __name__ == "__main__":
    app.run()
