while True:
    word = input()
    if word == '0':
        break
    
    word_list = list(word)    
    
    for i in range(len(word_list)):
        if word_list[i] != word_list[len(word_list)-1-i]:
            print('no')
            break
    else:
        print('yes')
    