#from collections import defaultdict

def read_args():
    first_arg = int(input())
    second_arg = int(input())
    operator =  input()
    
    return first_arg, second_arg, operator

def pprint(dictionary):
    for keys, values in dictionary.items():
        print(keys, values)

def count_with_history():
    history = {"+":[],
               "-":[],
               "/":[],
               "*":[]
               }

    def inner(*args):
        nonlocal history
        
        res = f"{args[0]}{args[-1]}{args[1]}"
        res += "=" + str(eval(res))
        history[args[-1]].append(res)
        
        print(res)
        pprint(history)
        return res

    return inner
    
def main():
    count = count_with_history()
    
    while True:
        count(*read_args())

if __name__ == "__main__":
    main()
        