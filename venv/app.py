from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/single-blog')
def singleblog():
    return render_template('single-blog.html')
@app.route('/list')
def list():
    return render_template('list.html')


@app.route("/sololeveling", methods=['POST', 'GET'])
def sololeveling():
    volno = request.form.get("chapter")
    return render_template('sololeveling.html', volno=volno)

@app.route("/oyasumipunpun", methods=['POST', 'GET'])
def oyasumipunpun():
    volno = request.form.get("chapter")
    return render_template('oyasumipunpun.html', volno=volno)

@app.route("/spyxfamily", methods=['POST', 'GET'])
def spyxfamily():
    volno = request.form.get("chapter")
    return render_template('spyxfamily.html', volno=volno)

@app.route("/bleach", methods=['POST', 'GET'])
def bleach():
    volno = request.form.get("chapter")
    return render_template('bleach.html', volno=volno)

@app.route("/tokyoghoul", methods=['POST', 'GET'])
def tokyoghoul():
    volno = request.form.get("chapter")
    return render_template('tokyoghoul.html', volno=volno)


if __name__ == '__main__':
    app.run(debug=True)