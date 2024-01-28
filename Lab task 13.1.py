#Q1: Attribute Validation Metaclass
class AttributeValidationMeta(type):
    def __new__(cls, name, bases, dct):
        # Perform custom validation on attributes here
        for key, value in dct.items():
            if isinstance(value, int) and value < 0:
                raise ValueError(f"Invalid value for attribute '{key}'")

        return super().__new__(cls, name, bases, dct)

# Example usage:
class MyClass(metaclass=AttributeValidationMeta):
    positive_value = 42
    negative_value = -10  # Raises ValueError during class creation
