import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv <source> <destination>")
    source_path = parts[1]
    dest_path = parts[2]
    if dest_path.endswith("/"):
        filename = os.path.basename(source_path)
        dest_path = os.path.join(dest_path, filename)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        path_parts = dest_dir.split("/")
        current_path = ""
        for part in path_parts:
            if not part:
                continue
            if current_path:
                current_path = os.path.join(current_path, part)
            else:
                current_path = part
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
