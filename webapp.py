# webapp.py for simple web app demo
# reference https://blog.csdn.net/yang9520/article/details/79740374


from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def information_page():
    return render_template('index.html'), 200

# secret_key used by session
# import os
# os.urandom(24)
app.secret_key = b'\xf70u\x8e7\xd5\xe6<\xd4\x1c\x0f\x13lPl\x9fe\xab\x93\xe4{\xe5v\xa0'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return "you logged in as: %s" % session['username']

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('information_page'))

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



from flask import request

with app.test_request_context('/postmethod', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/postmethod'
    assert request.method == 'POST'



from flask import abort, redirect, url_for

@app.route('/try404')
def index():
    return redirect(url_for('pagenotfound'))

@app.route('/pagenotfound')
def pagenotfound():
    abort(404)


from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0') # listen to all the requests