# webapp.py for simple web app demo
# reference https://blog.csdn.net/yang9520/article/details/79740374


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return 'Hello, the route to the /hello route...'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'The User inputed is: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'You just input the number %d under /post path...' % post_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0') # listen to all the requests