def run():
    my_list = [1, True]
    my_dict = {'Hello':'Mundo','Hola':'World'}

    super_list = [{'alola':'pokemon'}, {'Fork':'Spoon'}, {'A':2}]
    super_dict = {'A':['B','C'], 'King':['D','D','D']}

    for key, value in super_dict.items():
        print(key, ':', value)
    
    for elem in super_list:
        print(elem)

if __name__ == '__main__':
    run()