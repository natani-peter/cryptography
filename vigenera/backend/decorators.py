def display(action):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result, _text, key = function(*args, **kwargs)
            task = "DECRYPTION " if action else "ENCRYPTION "
            text = " ".join(_text)
            text_type = "CIPHER TEXT" if task[0] == "D" else "PLAIN TEXT "
            output = "CIPHER TEXT" if task[0] == "E" else "PLAIN TEXT "

            print(
                f"\nTask{" " * 7} : {task}\n"
                f"{text_type} : {text}\n"
                f"KEY{" " * 8} : {key}\n"
                f"{'_' * 80}\n"
                f"{output} : {result}"
            )

        return wrapper

    return decorator

