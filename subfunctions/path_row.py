import os
from subfunctions.time_decorator import time_decorator


@time_decorator
def path_row(directory):
    files = os.listdir(directory)
    file_paths = [os.path.join(directory, file) for file in files]
    
    return file_paths
