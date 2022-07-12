from flask import Flask, render_template, request, redirect

app = Flask(__name__)
nextid = 4
topics = [
    { 'id' : 1, 'title' : 'html', 'body':'html is ?'},
    { 'id' : 2, 'title' : 'css', 'body':'css is ?'},
    { 'id' : 3, 'title' : 'js', 'body':'js is ?'}
]

def template(contents, content):
    return f'''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href = "/">WEB</a></h1>
                <ol>
                    {contents}
                </ol>
                {content}
                <ul>
                    <li><a href = "/create/">create</a></li>
                </ul>
            </body>
        </html>
        '''

def get_content():
    li_tags = ''
    for topic in topics:
        li_tags = li_tags + f'<li><a href = "/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return li_tags

@app.route('/')
def index():
    return template(get_content(), '<h2>Welcome</h2>Hello, Web!')

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(get_content(), f'<h2>{title}</h2>{body}')

@app.route('/create/',methods = ['GET', 'POST'])
def create():
    global nextid
    if request.method  == 'GET':    
        content = '''
            <form action = "/create/" method = "POST">
                <p><input type = "text" name = "title" placeholder = "tilte"></p>
                <p><textarea name = "body" placeholder = "body"></textarea></p>
                <p><input type = "submit" value = "create"></p>
            </form>
        '''
        return template(get_content(), content)

    elif request.method  == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_topic = {'id' : nextid, 'title' : title, 'body' : body}
        topics.append(new_topic)
        url = f'/read/{str(nextid)}/'
        nextid = nextid + 1
        return redirect(url)

if __name__ == '__main__':
    app.run(debug = True)