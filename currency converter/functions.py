#functions.py

import json
import os
from json import JSONDecodeError


def file_manager(file_path,mode,data_to_save = None):
    if mode == "r":
        if os.path.exists(file_path):
            try:
                with open(file_path,"r") as json_file:
                    data = json.load(json_file)
            except JSONDecodeError:
                data = {}
        else:
            with open(file_path,"w") as json_file:
                data = {}
        return data

    if mode == "w":
        with open(file_path,"w") as json_file:
            json.dump(data_to_save,json_file)


def btext_inputer_v(question,valid_inputs = [],transform = None):
        while True:
            try:
                if transform is not None:
                    answer = transform(input(question))
                else:
                    answer = input(question)

            except TypeError:
                print(f"Plz enter a valid input anyone in this list, {valid_inputs}")


            if answer in valid_inputs:
                return answer
            else:
                print(f"Please enter a valid input anyone in this list {valid_inputs}")


def btext_inputer_t(question,data_type):
    while True:
            try:
               data = data_type(input(question))
               return data

            except ValueError:
                print(f"Please enter a valid input anyone in this {data_type} format")

def converter(data,from_cur,to_cur,amount):
     rate_from = data["conversion_rates"][from_cur]
     rate_to = data["conversion_rates"][to_cur]

     return amount * rate_to / rate_from

