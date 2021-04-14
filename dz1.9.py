# 3 варианта решение 
# def depos(user, user_want):
#     month = 1 
#     while user < user_want:
#         cash = 0.12 * user + user
#         user = int(cash)
#         print(user)
#         month += 1
#     else:
#         return("your money: " + str(month) + 'month')
# print(depos(int(input('wich many input yuor money:? ')), int(input(' How many get money?  '))))



# credit = 1000000
# credit_rate = 12
# final = credit
# for i in range(6):
#     final = credit_rate /  100 / 12 * final + final
#     print(f' {final} mounth')


# def func(dep, month, year):
#     final_sum = dep
#     for i in range(month):
#         final_sum = year/100/12*final_sum + final_sum
#         print(f' {final_sum} каждый месяц')
#     return final_sum
# func(1000000, 6, 12)