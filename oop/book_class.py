class Book:
    def __call__(self, *title: str, *author: str, year: int):
        self.titlt = title
        self.author = author
        self.year = year
    def __delattr__(self, name):
        "Deleting (title of the book)"
    def __str__(self):
        "(title) by (author), published in (year)"
        
    def __repr__(self):
        f"Book('{self.title}', '{self.author}"
        