class Teachers:
    common_rooms = {}

    def __init__(self, file):
        self.file = file
        self.read_file(file)

    def read_file(self, file):
        with open(file) as f:
            for line in f:
                rooms = line.split()
                if len(rooms) > 1:
                    self.find_common_cabinet(int(rooms[0]), int(rooms[1]))

    def find_common_cabinet(self, room1, room2):
        self.common_rooms.setdefault(room1, [])
        self.common_rooms.setdefault(room2, [])

        if room1 not in self.common_rooms[room2]:
            self.common_rooms[room2].append(room1)
        if room2 not in self.common_rooms[room1]:
            self.common_rooms[room1].append(room2)

    def find_min_common_room(self):
        is_set = False
        min1 = 0
        for key, value in self.common_rooms.items():
            if not is_set:
                min1 = len(value)
                key_min_item = key
                is_set = True
            elif len(value) < min1:
                min1 = len(value)
                key_min_item = key
        return key_min_item

    def print_optimized(self):
        print(self.common_rooms)


def main():
    a1 = Teachers('Кабинеты/test1.txt')
    a1.print_optimized()
    print(a1.find_min_common_room())


if __name__ == '__main__':
    main()