# Author: Yongyuth "First" Chaunkhuntod (Yothgewalt)
import os
from typing import Union
 
void: str = ' '
heroes: list[str] = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
method_message: str = """
Hero Operation - v1.0.0
 
[1] Display Heroes
[2] Append hero by Name
[3] Insert hero with specify index by Name
[4] Remove hero by Name
[5] Display Heroes with Sorting
"""
 
def display_heroes() -> str:
    global heroes
    prefix: str = '\nHeroes:'
    aggregate_hero: str = ''
    for hero_name in heroes:
        aggregate_hero += (void + hero_name)
 
    return print(prefix + aggregate_hero)
 
def append_hero(object_h: Union[str, list[str]]) -> None:
    global heroes
 
    if type(object_h) is list:
        for hero_name in object_h:
            heroes.append(hero_name)
 
    else:
        return heroes.append(object_h)
 
def insert_hero(object_i: Union[int, list[int]], object_h: Union[str, list[str]]) -> None:
    global heroes
 
    if type(object_h) is list and type(object_i) is list:
        index_value: int = 0
        for position in object_i:
            for hero_name in object_h:
                heroes.insert(position, hero_name[index_value])
                index_value += 1
                continue
 
    elif type(object_i) is list:
        for position in object_i:
            heroes.insert(position, object_h)
 
    elif type(object_h) is list:
        for hero_name in object_h:
            heroes.insert(object_i, hero_name)
 
    else:
        return heroes.insert(object_i, object_h)
 
    return None
 
def remove_hero(object_h: Union[str, list[str]]) -> None:
    global heroes
 
    if type(object_h) is list:
        for hero_name in object_h:
            heroes.remove(hero_name)
 
    else:
        return heroes.remove(object_h)
 
    return None
 
def display_sorted_heroes(descending=False) -> str:
    global heroes
 
    aggregate_hero: str = ''
    prefix_ascending: str = '\nAscending Heroes:'
    prefix_descending: str = '\nDescending Heroes:'
 
    if descending:
        heroes_descending_sorted = sorted(heroes, reverse=True)
        for hero in heroes_descending_sorted:
            aggregate_hero += (void + hero)
 
        return print(prefix_descending + aggregate_hero)
    else:
        heroes_ascending_sorted = sorted(heroes, reverse=False)
        for hero in heroes_ascending_sorted:
            aggregate_hero += (void + hero)
 
        return print(prefix_ascending + aggregate_hero)
    
def main():
    keep_going: str = 'Y'
 
    expect_value_error_message: str = '\nError: The value cannot be alphabet or special character (integer only)'
    incorrect_range_error_message: str = '\nError: The method cannot be less than 1 or greater than 5.'
 
    hero_name: str = ''
    hero_name_list: list[str] = []
 
    index: int = 0
    index_list: list[int] = []
 
    while keep_going.__eq__('Y'):
        hero_name_list: list[str] = []
        index_list: list[int] = []
 
        if os.name.__eq__('nt'):
            os.system('cls')
        else:
            os.system('clear')
 
        print(method_message)
 
        method: int = 0
        try:
            method = int(input("What do you want to do? [1-5]: "))
            while method < 1 or method > 5:
                print(incorrect_range_error_message)
                method = int(input("What do you want to do? [1-5]: "))
 
        except ValueError:
            print(expect_value_error_message)
 
        if method.__eq__(0):
            exit()
 
        if method.__eq__(1):
            display_heroes()
 
        elif method.__eq__(2):
            add_again: str = 'Y'
            verify_add_method: str = ''
            want_multiple_add = str(input("Do you want to add multiple names? [Y]: ")).upper()
 
            if want_multiple_add.__eq__('Y'):
                while add_again.__eq__('Y'):
                    verify_add_method = 'list'
                    hero_name = str(input("\nWhat is name that do you want to append [<name>]: "))
                    hero_name_list.append(hero_name)
 
                    add_again = str(input("Do you want to add more hero? [Y]: ")).upper()
            else:
                verify_add_method = 'single'
                hero_name = str(input("\nWhat is name that do you want to append [<name>]: "))
 
            if verify_add_method.__eq__('list'):
                append_hero(hero_name_list)
 
            elif verify_add_method.__eq__('single'):
                append_hero(hero_name)
 
            display_heroes()
 
        elif method.__eq__(3):
            add_index_again: str = 'Y'
            insert_again: str = 'Y'
            verify_insert_method: str = ''
            want_multiple_index = str(input("Do you want to insert with multiple indexes? [Y]: ")).upper()
            want_multiple_insert = str(input("Do you want to mutiple insert by following index? [Y]: ")).upper()
 
            if want_multiple_index.__eq__('Y') and want_multiple_insert.__eq__('Y'):
                verify_insert_method = 'hybrid-list'
                while add_index_again.__eq__('Y'):
                    index = int(input("What is number of index that do you want to insert [<integer>]: "))
                    index_list.append(index)
 
                    add_index_again = str(input("Do you want to add more index? [Y]: ")).upper()
 
                while insert_again.__eq__('Y'):
                    hero_name = str(input("\nWhat is name that do you want to insert [<name>]: "))
                    hero_name_list.append(hero_name)
 
                    insert_again = str(input("Do you want to add more name? [Y]: ")).upper()
 
            elif want_multiple_index.__eq__('Y'):
                verify_insert_method = 'position-list'
                while add_index_again.__eq__('Y'):
                    index = int(input("What is number of index that do you want to insert [<integer>]: "))
                    index_list.append(index)
 
                    add_index_again = str(input("Do you want to add more index? [Y]: ")).upper()
 
                hero_name = str(input("\nWhat is name that do you want to insert [<name>]: "))
 
            elif want_multiple_insert.__eq__('Y'):
                verify_insert_method = 'hero-list'
                index = int(input("What is number of index that do you want to insert [<integer>]: "))
 
                while insert_again.__eq__('Y'):
                    hero_name = str(input("\nWhat is name that do you want to insert [<name>]: "))
                    hero_name_list.append(hero_name)
 
                    insert_again = str(input("Do you want to add more name? [Y]: ")).upper()
 
            else:
                verify_insert_method = 'standard'
                index = int(input("What is number of index that do you want to insert [<integer>]: "))
                hero_name = str(input("\nWhat is name that do you want to insert [<name>]: "))
 
            if verify_insert_method.__eq__('hybrid-list'):
                insert_hero(index_list, hero_name_list)
 
            elif verify_insert_method.__eq__('position-list'):
                insert_hero(index_list, hero_name)
 
            elif verify_insert_method.__eq__('hero-list'):
                insert_hero(index, hero_name_list)
 
            else:
                insert_hero(index, hero_name)
 
            display_heroes()
 
        elif method.__eq__(4):
            remove_again: str = 'Y'
            verify_remove_method: str = ''
            want_multiple_delete = str(input("Do you want to remove multiple names? [Y]: ")).upper()
 
            if want_multiple_delete.__eq__('Y'):
                while remove_again.__eq__('Y'):
                    verify_remove_method = 'list'
                    hero_name = str(input("\nWhat is name that do you want to remove [<name>]: "))
                    hero_name_list.append(hero_name)
 
                    remove_again = str(input("Do you want to remove again? [Y]: ")).upper()
 
            else:
                verify_remove_method = 'single'
                hero_name = str(input("\nWhat is name that do you want to remove [<name>]: "))
 
            if verify_remove_method.__eq__('list'):
                for hero_name_to_remove in hero_name_list:
                    remove_hero(hero_name_to_remove)
 
            elif verify_remove_method.__eq__('single'):
                remove_hero(hero_name)
 
            display_heroes()
 
        elif method.__eq__(5):
            want_descending = str(input("Do you want to descending? [Y]: ")).upper()
 
            if want_descending.__eq__('Y'):
                display_sorted_heroes(descending=True)
 
            else:
                display_sorted_heroes()
 
        keep_going = str(input("\nDo you want to do again? [Y]: ")).upper()
 
if __name__ == '__main__':
    main()