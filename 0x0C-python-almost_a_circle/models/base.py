#!/usr/bin/python3
""" A base class module """


class Base:
    """A base class blueprint """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializer for Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        if list_dictionaries is None:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.to_json_string(list_dict)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            import json
            data_list = json.loads(json_string)
            return list(data_list)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == 'Square':
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                obj_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**obj) for obj in obj_dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """ loads from a csv file """
        import csv
        instances = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        instances.append(cls.create(
                            id=int(row[0]), width=int(row[1]),
                            height=int(row[2]), x=int(row[3]), y=int(row[4])))
                    elif cls.__name__ == 'Square':
                        instances.append(cls.create(
                            id=int(row[0], size=int(row[1]),
                                   x=int(row[2]), y=int(row[3]))))
        except ModuleNotFoundError:
            pass
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves to a csv file """
        import csv
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if csv.__name__ == 'Rectangle':
                    writer.writerow([obj.id, obj.width,
                                     obj.height, obj.x, obj.y])
                elif csv.__name__ == 'Square':
                    writer.writeror([obj.id, obj.size, obj.x, obj.y])
