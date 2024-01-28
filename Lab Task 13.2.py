#Q2: Hooking Class Creation
class CustomLogicMeta(type):
    def __init__(cls, name, bases, dct):
        # Custom logic during class creation (e.g., attribute addition, method creation)
        cls.custom_attribute = 'Added during class creation'

        def custom_method(self):
            return f"Custom method in {name}"

        cls.custom_method = custom_method

        super().__init__(name, bases, dct)

# Example usage:
class AnotherClass(metaclass=CustomLogicMeta):
    pass

obj = AnotherClass()
print(obj.custom_attribute)  # Output: 'Added during class creation'
print(obj.custom_method())   # Output: 'Custom method in AnotherClass'
