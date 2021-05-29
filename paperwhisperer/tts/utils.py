def save_file(save_path, binary_object):
    with open(save_path, "wb") as f:
        f.write(binary_object)