def multi_table(num):
    for i in range(1,11):
        res=num*i
        
    return res

def main():
    num=int(input("enter a number:"))
    res=multi_table(num)
    print(res)
main()