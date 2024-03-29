
def counter(file_name, word_count, word_list_and_counts):
    inputfile = open(file_name,'r')
    line = inputfile.readline()
    line = line.rstrip()
    while line != '':
        #將沒有出現在dict裡面的key預設為0
        word_list_and_counts.setdefault(line, 0)
        #如果key為0代表這個字還沒有出現，key設為1
        if word_list_and_counts[line] == False:
            word_list_and_counts[line] = 1
            word_count += 1
        #已經在dict裡面的字key直接加1
        else:
            word_list_and_counts[line] += 1   
        #換讀下一行
        line = inputfile.readline()
        line = line.rstrip()
    #輸出結果(出現不同英文名詞的數目, 各英文名詞出現的次數)
    return word_count, word_list_and_counts


def print_results(word_count, word_list_and_counts):
    print('總共有{}個不重複的英文字'.format(word_count))
    print('每一個英文字出現次數:')
    for i in word_list_and_counts:
        print(i, word_list_and_counts[i])
        

def main():
    #建一個dict
    my_dict = {}
    #紀錄不同字個數，預設為0
    word_count = 0
    #讀檔案
    result = counter('hw2_data.txt', word_count, my_dict)
    #印結果
    print_results(result[0], result[1])
    
if __name__== main():
    main()
    
    