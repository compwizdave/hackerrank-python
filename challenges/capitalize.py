def capitalize(string):
    output = list(string)
    
    capit=True
    for p in range(len(string)):        
        if output[p].isspace():
            capit = True
            continue
        if output[p].isalnum() and capit:
            output[p]=output[p].capitalize()
            capit=False

    return ''.join(output)

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
