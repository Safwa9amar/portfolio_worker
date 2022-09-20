from flask import render_template, url_for, flash, redirect
from app.forms import RegForm
from app.models import Blog, BlogsSchema, FetchNotionApi
from app import app, db
from flask import jsonify
import json
data = [
    {
        'header': 'How To Use CSS Layers',
        'text': 'CSS layers change how the cascade works and it makes writing clean CSS code so much easier.',
        'tag': 'app',
        'img': 'https://e3arabi.com/wp-content/uploads/2021/02/css-framework.jpg'
    },

    {
        'header': 'How To Use CSS Layers',
        'text': 'CSS layers change how the cascade works and it makes writing clean CSS code so much easier.',
        'tag': 'app',
        'img': 'https://e3arabi.com/wp-content/uploads/2021/02/css-framework.jpg'
    },

]


@app.route('/')
def home():
    return render_template('home.html', data=data)


@app.route('/blogs')
def about():
    posts = Blog.query.all()
    post_schema = BlogsSchema(many=True)
    output = post_schema.dump(posts)
    return jsonify({"post": output})
    # return render_template('blogs_worker.html', posts = posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = RegForm()
    if form.validate_on_submit():
        en_notion = FetchNotionApi(form.en_notion_id.data)
        ar_notion = FetchNotionApi(form.ar_notion_id.data)
        darija_notion = FetchNotionApi(form.ar_darija_notion_id.data)
        print(json.loads(en_notion))
        post = Blog(
            header=form.header.data,
            tag=form.tag.data,
            resume=form.Resume.data,
            img_url=form.img.data,
            en_notion_id=form.en_notion_id.data,
            ar_notion_id=form.ar_notion_id.data,
            ar_darija_notion_id=form.ar_darija_notion_id.data,
            date_posted=form.date.data,
            en_notion = en_notion ,
            ar_notion = ar_notion ,
            darija_notion = darija_notion 
        )
        db.session.add(post)
        db.session.commit()
        print(post.date_posted)
        flash(f'Post added succesfully {form.header.data}', 'success')
        # return redirect(url_for('home'))
    else:
        flash(f'Failed to add {form.header.data} please try again', 'danger')

    return render_template('reg.html', form=form)
