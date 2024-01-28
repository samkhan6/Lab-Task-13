#Q3: Mixin Classes
# Mixin class for logging functionality
class LoggingMixin:
    def log(self, message):
        print(f"[Log] {message}")

# Mixin class for serialization functionality
class SerializationMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

# Example usage:
class MyCombinedClass(LoggingMixin, SerializationMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of MyCombinedClass
obj = MyCombinedClass("Sameer", 23)

# Use mixin functionalities
obj.log("Instance created.")
json_data = obj.to_json()
print(json_data)
