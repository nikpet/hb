def reduce_file_path(path):
    elements = path.split("/")
    result = ['']
    for index in range(len(elements)):
        if elements[index] == '..' and len(elements) > 2:
            if result[len(result) - 1] == '':
                continue
            else:
                del result[len(result) - 1]
        elif elements[index] == "." or elements[index] == "":
            continue
        else:
            result.append(elements[index])
    result = '/'.join(result)
    if result[0:1] != '/':
        result = '/' + result
    return result


if __name__ == '__main__':
    print(reduce_file_path("/"))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))
    # print('/../'.split('/'))
