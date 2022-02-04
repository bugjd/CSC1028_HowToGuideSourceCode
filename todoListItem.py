import uuid
import datetime


class TodolistItem:

    def __init__(self, unique_id, todo_item, item_stared, completion_date):
        if unique_id is None:
            self.__unique_id = str(uuid.uuid4())
        else:
            self.__unique_id = unique_id
        self.todo_item = todo_item
        self.item_stared = item_stared
        self.completion_date = completion_date

    def completion_date_string(self):
        return self.completion_date.strftime("%d/%m/%Y at %H:%M")

    def has_completion_time_passed(self):
        sysdate = datetime.datetime.now()
        due_date = self.completion_date
        if due_date > sysdate:
            return False
        else:
            return True

    def get_unique_id(self):
        return self.__unique_id



