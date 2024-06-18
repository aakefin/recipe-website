from recipeWeb import my_app
from recipeWeb.config import Config

app = my_app(Config)

if __name__ == '__main__':
    app.run(debug=True)