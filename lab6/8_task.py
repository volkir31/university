class SocialNetwork:
    friendship = {}
    user_count = 0

    def __init__(self, file):
        f = open(file)
        while True:
            line = f.readline()
            if not line:
                break
            numbers = line.split()
            if len(numbers) == 1:
                self.user_count = int(numbers[0])
                continue
            user_id = int(numbers[0])
            friend_id = int(numbers[1])
            self.add_friendship(user_id, friend_id)

    def add_friendship(self, user1, user2):
        self.friendship.setdefault(user1, [])
        if user2 not in self.friendship[user1]:
            self.friendship[user1].append(user2)

        self.friendship.setdefault(user2, [])
        if user1 not in self.friendship[user2]:
            self.friendship[user2].append(user1)

    def is_friends(self, user1, user2):
        if user1 in self.friendship:
            return user2 in self.friendship[user1]
        return False

    def get_common_friends_count(self, user1, user2):
        friends1 = self.friendship[user1]
        if user2 in friends1:
            friends1.remove(user2)

        friends2 = self.friendship[user2]
        if user1 in friends2:
            friends2.remove(user1)

        count = 0
        for i in friends1:
            if i in friends2:
                count += 1
        return count

    def recommend(self, user_id):
        friend_id = -1
        may_be_common_friends_count = 0
        for user in self.friendship:
            if user_id == user:
                continue
            if self.is_friends(user_id, user):
                continue

            friends_count = self.get_common_friends_count(user_id, user)
            if friend_id == -1:
                friend_id = user
                may_be_common_friends_count = friends_count
            elif friends_count > may_be_common_friends_count:
                friend_id = user
                may_be_common_friends_count = friends_count
            elif friends_count == may_be_common_friends_count:
                if user < friend_id:
                    friend_id = user
                    may_be_common_friends_count = friends_count

        return friend_id

if __name__ == '__main__':
    sn = SocialNetwork('files/small_net_win_line_end.txt')
    print(sn.recommend(0))
    print(sn.recommend(1))
    print(sn.recommend(2))
