from dataclasses import dataclass
from pathlib import Path
from typing import List, Union

import csv
import os

@dataclass
class AuthorObject:
    id: int
    first_name: str
    last_name: str
    birth_date: int
    death_date: int


    def values_to_list(self):
        return [self.id, self.first_name, self.last_name, self.birth_date, self.death_date]

def export_to_csv(authors: List[AuthorObject], f_name: str = None) -> Path:
    """zapisuje książki do csv o nazwie f_name albo books.csv i zwraca ściężkę do pliku"""

    if not f_name:
        f_name = "data/data.csv"

    path = Path(f_name)
    books = [b.values_to_list() for b in authors]

    with path.open('w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(books)

    return path