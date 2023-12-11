#!/usr/bin/python3
"""Base module"""
import json
import csv
import turtle


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """Draws with the turtle module"""
        turtle.bgcolor("black")
        t = turtle.Turtle()
        colors = ["red", "dark red"]
        for rec in list_rectangles:
            t.penup()
            t.goto(rec.x, rec.y)
            t.pendown()
            t.pencolor(colors[1])
            t.forward(rec.width)
            t.right(90)
            t.forward(rec.height)
            t.right(90)
            t.forward(rec.width)
            t.right(90)
            t.forward(rec.height)
            t.right(90)

        # t.penup()
        # t.goto(20, 100)
        for sq in list_squares:
            t.penup()
            t.goto(sq.x, sq.y)
            t.pendown()
            t.pencolor(colors[1])
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.right(90)
            t.forward(sq.size)
            t.right(90)
        turtle.done()

    @classmethod
    def load_from_file_csv(cls):
        """Reads a list of dicts or Base objects into a csv file"""
        try:
            with open(cls.__name__ + ".csv", mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames is None:  # file is empty
                    return []
                dicts = []
                for row in reader:
                    for key, value in row.items():
                        if value.isdigit():
                            row[key] = int(value)
                    dicts.append(row)
        except (FileNotFoundError):  # file does not exists
            return []
        return [cls.create(**dict_) for dict_ in dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs: list):
        """Saves a list of dicts or Base objects into a csv file"""
        dicts, data = [], []

        if type(list_objs) is list:
            dicts = [d.to_dictionary() if isinstance(d, Base) else d
                     for d in list_objs]

        if cls.__name__ == "Square":
            data = [["id", "size", "x", "y"]]  # header
            data += [
                [dic["id"], dic["size"], dic["x"], dic["y"]] for dic in dicts]
        elif cls.__name__ == "Rectangle":
            data = [["id", "width", "height", "x", "y"]]  # header
            data += [
                [dic["id"], dic["width"], dic["height"], dic["x"], dic["y"]]
                for dic in dicts]

        with open(cls.__name__ + ".csv", mode="w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances:"""
        filename = cls.__name__+".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                arr = Base.from_json_string(f.read())
                instances = [cls.create(**info) for info in arr]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        instance = None
        if cls.__name__ == "Rectangle":
            instance = cls(width=5, height=5, x=0, y=0, id=0)
        elif cls.__name__ == "Square":
            instance = cls(size=5, x=0, y=0, id=0)

        if isinstance(instance, Base):
            instance.update(**dictionary)
        return instance

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file_:
            if not list_objs:
                file_.write("[]")
            else:
                file_.write(Base.to_json_string(list_objs))

    @staticmethod
    def to_json_string(list_dictionaries: list) -> str:
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps([
            rect.to_dictionary() if isinstance(rect, Base) else rect
            for rect in list_dictionaries
        ])
