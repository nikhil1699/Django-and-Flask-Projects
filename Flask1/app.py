from flask import Flask,jsonify,request
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/Hey')
def HeyGirls():
    GirlsJson={
        'Pretty':'Akansha Jha',
        'Nice':'Riya Maniar',
        'More Girls':[
            {
                'Arrogant girls':'Arti Chahar',
                'Bad girls':'Anjali Mishra'
            },
            {
                'Intelligent Girls':'Namrata Kushwaha',
                'Hyper Girls':'Bansari Akbari'
            },
            {
                'My Crush':'Nithika Benny'
            }
        ]
        
    }
    return jsonify(GirlsJson)
@app.route('/love',methods=['POST'])
def iLove():
    dataDict=request.get_json()
    crush1=dataDict['crush1']
    crush2=dataDict['crush2']
    final="I wanna be with {} and {} ".format(crush1,crush2)
    retJson={
        "final":final
    }
    return jsonify(retJson),200

@app.route('/ByeBABE')
def bye():
    c=2+2
    for i in range(1,5):
        c=c+i
    #d=5/0
    return "c is now {}".format(c)   

if __name__=="__main__":
    app.run(debug=True)

