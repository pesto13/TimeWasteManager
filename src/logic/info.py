from dataclasses import dataclass

@dataclass
class Info():
    name: str
    cathegory: str
    seconds: int


    def __add__(self, other: int):
        if isinstance(other, int):
            r = self
            r.seconds+=other
            return r
    #i nodi nell'albero vengono ordinati per nome dell'applicazione, per poi fare una ricerca più veloce
    """ def __lt__(self, other: object|str):
        if type(other) is Info:
            return self.name<other.name
        else:
            return self.name<other
    
    def __gt__(self, other: object|str):
        if type(other) is Info:
            return self.name>other.name
        else:
            return self.name>other

    def __eq__(self, __o: object|str) -> bool:
        if type(__o) is Info:
            return self.name==__o.name
        else:
            return self.name==__o """