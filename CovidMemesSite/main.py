from flask import Flask, render_template, request
import praw


#insert id, secret, agent
reddit = praw.Reddit(
    client_id='', 
    client_secret='', 
    user_agent='',
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
  
@app.route('/random')
def random():
    p = 'i.redd.it'
    while True:
        random = reddit.subreddit('covid19memes').random()
        if p in str(random.url):
            return render_template('index.html', random = random.url)
            break

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
