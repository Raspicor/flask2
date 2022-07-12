from flask import Flask, render_template

app = Flask(__name__)
topics = [
    { 'id' : 1, 'title' : 'html', 'body':'html is !'},
    { 'id' : 2, 'title' : 'css', 'body':'css is !'},
    { 'id' : 3, 'title' : 'js', 'body':'js is !'}
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
    
if __name__ == '__main__':
    app.run(debug = True)