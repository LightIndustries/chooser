from typing import List, Union
import numpy as np

def choose_list_element(item_list: List[Union[str, int, float]]):
    return np.random.choice(item_list)

if __name__ == "__main__":
    choose_list_element([])