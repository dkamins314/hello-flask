from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label for="new-movie">
            I want to add
            <input type="text" id="new-movie" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

# a form for crossing off watched movies
crossoff_form = """
<form action='/crossoff' method='post'>
    <select name="crossed-off-movie">
        {dropdown_items}
    </select>
    <button type="submit">Crossoff movie</button>
</form>
"""

@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']    
    crossed_off_movie_html = "<strike>"+crossed_off_movie+"</strike> has been crossed off your watchlist"
    return page_header + "<p>" + crossed_off_movie_html + "</p>" + page_footer
    
@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']
    movies.append(new_movie)
    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # build the response string
    content = page_header + edit_header + add_form + crossoff_form.format(dropdown_items = get_dropdown_options()) + page_footer

    return content

movies = []

def get_dropdown_options():
    dropdown = ""
    option_html = "<option>{movie}</option>"
    for movie in movies:
        dropdown += option_html.format(movie=movie)
    return dropdown

app.run()