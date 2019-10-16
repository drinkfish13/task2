ids = [['user1', [213, 213, 213, 15, 213]], ['user2', [54, 54, 119, 119, 119]], ['user3', [213, 98, 98, 35]]]
new_list = []
reoid = []
for i in range(len(ids)):
    new_list += ids[i][1]
n= new_list[0]
for i in range(len(new_list)):
    if new_list[i] not in reoid:
        reoid.append(new_list[i])
print(reoid)
