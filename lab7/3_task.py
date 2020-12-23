class Teachers:
    common_rooms = {}
    result = []
    key_min_item = 0

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
        if not self.is_circle(self.common_rooms):
            is_set = False
            min1 = 0
            for key, value in self.common_rooms.items():
                if not is_set:
                    min1 = len(value)
                    self.key_min_item = key
                    is_set = True
                elif len(value) < min1:
                    min1 = len(value)
                    self.key_min_item = key
                if len(value) == 1:
                    if self.common_rooms[self.key_min_item][0] not in self.common_rooms:
                        self.result.append(str(self.common_rooms[self.key_min_item][0]))
                        self.common_rooms.pop(self.key_min_item)
                    break
            if self.key_min_item in self.common_rooms:
                self.find_common_key(self.key_min_item)
        else:
            if len(self.common_rooms) % 2 == 0:
                self.if_even_count_room_in_circle()
            else:
                self.if_odd_count_room_in_circle()

    def if_even_count_room_in_circle(self):
        while len(self.common_rooms) > 0:
            if len(self.result) == 0:
                min_key = min(list(self.common_rooms.keys()))
                self.result.append(str(min_key))
                self.common_rooms.pop(max(self.common_rooms[min_key]))
                self.common_rooms.pop(min_key)
            else:
                min_key = min((list(self.common_rooms.keys()))) + 1
                self.result.append(str(min_key))
                try:
                    self.common_rooms.pop(self.common_rooms[min_key][0])
                    self.common_rooms.pop(self.common_rooms[min_key][1])
                    self.common_rooms.pop(min_key)
                except KeyError:
                    pass

    def if_odd_count_room_in_circle(self):
        while len(self.common_rooms) > 0:
            if len(self.result) == 0:
                min_key = min(list(self.common_rooms.keys()))
                self.result.append(str(min_key))
                self.common_rooms.pop(self.common_rooms[min_key][0])
                self.common_rooms.pop(self.common_rooms[min_key][1])
                self.common_rooms.pop(min_key)
            else:
                min_key = min((list(self.common_rooms.keys()))) + 1
                self.result.append(str(min_key))
                self.common_rooms.pop(self.common_rooms[min_key][0])
                self.common_rooms.pop(self.common_rooms[min_key][1])
                self.common_rooms.pop(min_key)

    def find_common_key(self, key):
        common_key = self.common_rooms[key]
        if len(common_key) == 1:
            self.result.append(str(common_key[0]))
        else:
            self.result.append(str(key))
        for key1 in common_key:
            if key1 in self.common_rooms:
                self.delete_item(key1)

    def delete_item(self, key):
        for k in self.common_rooms[key]:
            try:
                self.common_rooms.pop(k)
            except KeyError:
                continue
        self.common_rooms.pop(key)

    def is_circle(self, dict1: dict):
        len_val = 0
        is_set = False
        for value in dict1.values():
            if not is_set:
                len_val = len(value)
                is_set = True
            else:
                if len(value) != len_val:
                    return False
        return True

    def print_optimized(self):
        if not self.is_circle(self.common_rooms):
            while len(self.common_rooms) > 0:
                self.find_min_common_room()
        else:
            self.find_min_common_room()
        print('Teachers: {}\nRooms: {}'.format(len(self.result), ','.join(sorted(self.result))))


def main():
    a1 = Teachers('Кабинеты/test6.txt')
    a1.print_optimized()


if __name__ == '__main__':
    main()
