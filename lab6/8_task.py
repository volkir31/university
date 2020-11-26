class SocialNetwork:
    def __init__(self, file):
        self.file = file

    def recommend(self, user_id):
        with open(self.file, 'r') as f:
            friend_dict = {}
            for line in f:
                formatted_line = line.split()
                if len(formatted_line) == 2:
                    if formatted_line[0] not in friend_dict:
                        friend_dict[formatted_line[0]] = formatted_line[1] + ' '
                    else:
                        friend_dict[formatted_line[0]] += formatted_line[1] + ' '
                    if formatted_line[1] not in friend_dict:
                        friend_dict[formatted_line[1]] = formatted_line[0] + ' '
                    else:
                        friend_dict[formatted_line[1]] += formatted_line[0] + ' '

        user_friend = friend_dict[str(user_id)].split()
        count, max_count, friend_id = 0, 0, ''
        for user, friends in friend_dict.items():
            count = 0
            for friend in friends.split():
                for user_f in user_friend:
                    if int(user_f) == int(friend):
                        count += 1
            if int(count) > int(max_count) and int(user) != int(user_id) and user not in friend_dict[str(user_id)]:
                max_count = count
                friend_id = user
        return friend_id

        # str_user_id = str(user_id)
        # for friend in friend_dict[str_user_id].split():
        #     if friend in friend_dict:
        #         for fr in friend_dict[friend].split():
        #             if fr not in mutual_friends:
        #                 mutual_friends[fr] = 1
        #             else:
        #                 mutual_friends[fr] += 1
        # mutual_friends_list = list(mutual_friends.items())
        # mutual_friends_list.sort(key=lambda list1: (-list1[1], list1[0]))


if __name__ == '__main__':
    sn = SocialNetwork('files/small_net_win_line_end.txt')
    print(sn.recommend(0))
    print(sn.recommend(1))
    print(sn.recommend(2))
