import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv <source> <destination>")
    _, source_path, dest_path = parts
    if dest_path.endswith("/"):
        filename = os.path.basename(source_path)
        dest_path = os.path.join(dest_path, filename)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        norm_dest_dir = os.path.normpath(dest_dir)
        path_parts = norm_dest_dir.split(os.sep)
        current_path = ""
        for part in path_parts:
            if not part:
                if not current_path and dest_dir.startswith(os.sep):
                    current_path = os.sep
                continue
            if current_path and current_path != os.sep:
                current_path = os.path.join(current_path, part)
            else:
                current_path = os.path.join(current_path, part) \
                    if current_path else part
            if not os.path.exists(current_path):
                os.mkdir(current_path)
    try:
        with open(source_path, "r") as f_src:
            content = f_src.read()
        with open(dest_path, "w") as f_dest:
            f_dest.write(content)
        os.remove(source_path)
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
