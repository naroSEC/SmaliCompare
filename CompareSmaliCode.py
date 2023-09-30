import os
import re

def search_in_directory(directory):
    file_list = []

    for root, dirs, files in os.walk(directory):

        for file in files:
            file_path = os.path.join(root, file)
            
            parshing_file = file_path.replace(directory, '')
            
            file_list.append(parshing_file)

    return file_list

def compare_smali(compare_1, compare_2):
    tmp_compare_2 = compare_2.copy()

    for smali in compare_1:
        if smali in tmp_compare_2:
            tmp_compare_2.remove(smali)
        else:
            tmp_compare_2.append(smali)

    return tmp_compare_2

def read_smali_Files(smali_list, front_path):
    r = re.compile('^.method')
    func_dic = {}

    for smali in smali_list:
        func_list = []
        
        try:
            with open(f'{front_path+smali}', 'r', encoding='utf-8') as file:
                file_contents = file.readlines()

                for read in file_contents:
                    if read == '\n':
                        continue
                    if r.match(read.strip()):
                        func_list.append(read.strip())
        
        except FileNotFoundError:
            print(f"파일 '{smali}'을(를) 찾을 수 없습니다.")
        except Exception as e:
            print(f"파일을 읽어오는 중 오류 발생: {str(e)}")

        func_dic[smali] = func_list

    return func_dic

def compare_funcs(cmp_dic_1, cmp_dic_2):
    change_results = {}

    for key in cmp_dic_1.keys():
        if key in cmp_dic_2:
            result = compare_smali(cmp_dic_1[key], cmp_dic_2[key])
            if result:
                change_results[key] = result

    return change_results

def write_reporting(rev_or_add_file, funcs_name):
    try:
        with open('REPORTING.txt', 'w', encoding='utf-8') as file:
            file.write("[ 새로 추가되거나 삭제된 smali 파일 ]\n")
            for str in rev_or_add_file:
                file.write(str + "\n")

            file.write("\n[ 새로 추가되거나 삭제된 함수 ]\n")
            for _class, _funcs in funcs_name.items():
                file.write(f"[*] 클래스 위치 : {_class}\n")

                for i in _funcs:
                    file.write(f"\t=> {i}\n")

                file.write("\n")

    except Exception as e:
        print(f"파일을 저장하는 중 오류 발생: {str(e)}")
