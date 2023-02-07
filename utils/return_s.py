def ret_success(correct_words,incorrect_words,r1,r5,r10):
    success = {}
    for i in range (len(correct_words)):
        if (correct_words[i] in r1[i] ):
            success[incorrect_words[i]] = {'success_1':1, 'success_5':1, 'success_10':1}
        elif(correct_words[i] in r5[i]):
            success[incorrect_words[i]] = {'success_1':0, 'success_5':1, 'success_10':1}
        elif(correct_words[i] in r10[i]):
            success[incorrect_words[i]] = {'success_1':0, 'success_5':0, 'success_10':1}
        else:
            success[incorrect_words[i]] = {'success_1':0, 'success_5':0, 'success_10':0}       
    return success

def ret_success1(correct_words,incorrect_words,r1,r5,r10):
    success = {}
    for i in range (len(correct_words)):
        if (correct_words[i] in r1 ):
            success[incorrect_words[i]] = {'success_1':1, 'success_5':1, 'success_10':1}
        elif(correct_words[i] in r5):
            success[incorrect_words[i]] = {'success_1':0, 'success_5':1, 'success_10':1}
        elif(correct_words[i] in r10):
            success[incorrect_words[i]] = {'success_1':0, 'success_5':0, 'success_10':1}
        else:
            success[incorrect_words[i]] = {'success_1':0, 'success_5':0, 'success_10':0}       
    return success
