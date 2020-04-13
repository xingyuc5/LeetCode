import sys
import time

q = "%20".join(sys.argv[1:])
q_num = int(sys.argv[1].rstrip('.'))
q_name = " ".join(sys.argv[2:])
final_name = "{:0>4d}. {}".format(q_num, q_name)
curr_date = time.strftime("%d/%m/%Y", time.localtime())

# By Difficulty
by_difficulty = "[{}](./problems/{}.md) <small>{}</small>".format(
    final_name, q, curr_date)


# By Dates
by_date = "[{}](./problems/{}.md)".format(
    final_name, q)


print(by_difficulty)
print(by_date)
# print()
