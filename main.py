import random
from flask import Flask

with open("pages/index.html") as data:
    main_page_html=data.read()

with open("pages/win_page.html") as data:
    win_page_html=data.read()

with open("pages/too_low.html") as data:
    low_page_html=data.read()

with open("pages/too_high.html") as data:
    high_page_html=data.read()

app=Flask(__name__)
random_number=random.randint(0,9)

def check_number(function):
    def wrapper(number,):
        if number>random_number:
            return high_page_html
        elif number<random_number:
            return low_page_html
        else:
            return win_page_html
    return wrapper


@app.route("/")
def main_page():
    return str(main_page_html)

@app.route(f"/<int:number>")
@check_number
def final_page(number):
    return number


if __name__=="__main__":
    app.run(debug=True)