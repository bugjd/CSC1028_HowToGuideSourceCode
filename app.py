import datetime
from flask import Flask, render_template, request
from todoListItem import TodolistItem
from jsonReadWrite import JsonReadWrite

app = Flask(__name__)
reader = JsonReadWrite("todolist.json")


@app.route('/', methods=['POST', 'GET'])
def main_method():
    if request.method == 'POST':
        reader.change_toggle((request.form.get("toggle")))
        return render_template('redirect.html')
    else:
        return render_template('todo.html', Items=reader.get_list())


@app.route('/addNewItem', methods=['POST', 'GET'])
def add_new_item():
    if request.method == 'POST':
        date_to_complete = datetime.datetime.strptime(request.form.get("allocatedTime"), "%Y-%m-%dT%H:%M")
        reader.add_item(TodolistItem(None, (request.form.get("todo_item")), False, date_to_complete))
        return render_template('redirect.html')
    else:
        return render_template('additem.html')


@app.route('/delete', methods=['POST'])
def delete_item():
    reader.delete_item(request.form.get("delete"))
    print((request.form.get("delete")))
    return render_template('redirect.html')


if __name__ == '__main__':
    app.run()
