# A serializable model for python 2/3
# WIP
import json

class SimpleSerializableModel(object):
    def serialize_json(self):
        result = {}
        for k, value in vars(self).items():
            # Check that the value is of a type we can handle.
            valtype = type(value)

            try:
                result[k] = json.dumps(value)
            except TypeError as e:
                if valtype in [list, tuple]:
                    return  

                if hasattr(value, 'serialize_json'):
                    result[k] = json.dumps(value)
                else:
                    # We'll skip this.
                    pass

        return result

    @classmethod
    def deserialize_json(clss):
        print(clss)



class TestModel(SimpleSerializableModel):
    def __init__(self):
        self.friends = []
        self.dictt = {"hi": 1}

if __name__ == "__main__":
    m = TestModel()

    print(m.serialize_json())
