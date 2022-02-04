import os
import json
from datetime import datetime

from todoListItem import TodolistItem


class JsonReadWrite:
    def __init__(self, file_name):
        folder_location = os.path.dirname(os.path.abspath(__file__))
        self.__file = os.path.join(folder_location, file_name)

    def delete_item(self, items_uuid):
        json_dict_array = self.__read_json()
        counter = 0
        while counter < len(json_dict_array):
            item = json_dict_array[counter]
            if item["uuid"] == items_uuid:
                json_dict_array.pop(counter)
                updated_json_file = json.dumps(json_dict_array)
                with open(self.__file, 'w') as outfile:
                    outfile.write(updated_json_file)
                    outfile.close()
                break
            else:
                counter = counter + 1

    def change_toggle(self, items_uuid):
        json_dict_array = self.__read_json()

        for item in json_dict_array:
            if items_uuid == item["uuid"]:
                if item["itemStared"]:
                    item["itemStared"] = False
                else:
                    item["itemStared"] = True
                updated_json_file = json.dumps(json_dict_array)

                with open(self.__file, 'w') as outfile:
                    outfile.write(updated_json_file)
                    outfile.close()
                break

    def add_item(self, todolist_item):

        item_to_add = {
            "uuid": todolist_item.get_unique_id(),
            "item_name": todolist_item.todo_item,
            "itemStared": todolist_item.item_stared,
            "date": todolist_item.completion_date_string(),
        }
        self.__write_json(item_to_add)

    def __write_json(self, write_dict):
        json_dict_array = self.__read_json()

        json_dict_array.append(write_dict)
        updated_json_file = json.dumps(json_dict_array)

        with open(self.__file, 'w') as outfile:
            outfile.write(updated_json_file)
            outfile.close()

    def get_list(self):
        dict_list_of_items = self.__read_json()
        todo_list_item_list_of_items = []
        if len(dict_list_of_items) > 0:
            for dict_item in dict_list_of_items:
                date_as_datetime = datetime.strptime(dict_item["date"], "%d/%m/%Y at %H:%M")
                todo_item = TodolistItem(dict_item["uuid"], dict_item["item_name"], dict_item["itemStared"],
                                         date_as_datetime)
                todo_list_item_list_of_items.append(todo_item)
        return todo_list_item_list_of_items

    def __read_json(self):
        try:
            with open(self.__file) as json_file:
                json_dict_array = json.load(json_file)
                json_file.close()
                if isinstance(json_dict_array, list):
                    return json_dict_array
                return []
        except FileNotFoundError:
            with open(self.__file, "x") as json_file:
                json_file.close()
                return []
        except json.JSONDecodeError:
            return []
