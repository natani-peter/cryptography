from typing import List


class Validator:
    @staticmethod
    def verify(my_property: str):
        def decorator(function):
            def wrapper(*args, **kwargs):
                property_to_be_set = "Key" if my_property[0].lower() == "k" else "Text"
                key = args[1]
                if not isinstance(key, List):
                    raise ValueError(f"{property_to_be_set} must be a string")

                if not map(lambda x: x.isalpha(), key):
                    raise ValueError(f"{property_to_be_set} must contain only alphanumeric characters")

                return function(*args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def clean_text(function):
        def wrapper(*args, **kwargs):

            user_text = (args[1].upper().
                         replace(".", "").
                         replace(",", "").
                         replace("!", "").
                         replace("?", "").
                         replace("'", ""))

            cleaned_text: List = [word for word in user_text.split(" ") if word.isalpha() and not word.isspace()]
            return function(args[0], cleaned_text, **kwargs)

        return wrapper
