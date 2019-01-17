from flask import Flask, render_template, request


from giphy import *

app=Flask(__name__)# curr file name

# index page: get puery
@app.route("/")
def index():
    return render_template("index.html")
    
# search page:
@app.route("/search",methods=["GET"])
def search():
    query=request.args.get('query')
    
    json_file = send_request(query)
    urls,titles,sources = json_parsing(json_file)
    
    return render_template("search.html",urls=urls,keyw=query,titles=titles,sources=sources)

@app.route("/trending",methods=["GET"])
def trending():
    json_file=trend_request(10)
    urls,titles,sources = json_parsing(json_file)
    return render_template("trending.html",urls=urls,titles=titles,sources=sources)


@app.route("/test")
def test_():
    try:
        pagenum=int(request.args["page"])
    except:
        pagenum=0
        print("page number error")
    print(pagenum)
    json_file=trend_request(24)
    urls,titles,sources = json_parsing(json_file)
    return render_template("test.html",urls=urls[pagenum*8:pagenum*8+8],titles=titles[pagenum*8:pagenum*8+8],sources=sources[pagenum*8:pagenum*8+8])
    
@app.route("/block")
def block():
    return render_template("block.html")