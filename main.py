with open('new.py', 'r', encoding='utf-8') as py:
    lines = py.readlines()
    new_lines = []
    for line in lines:
        if '#' in line:
            new_line=''
            for symb in line:
                if symb!='#':
                    new_line+=symb
                else:
                    new_line+='\n'
                    break
            new_lines.append(new_line)
        else:
            new_lines.append(line)
with open('test.py','w',encoding='utf-8') as py2:
    py2.writelines(new_lines)
