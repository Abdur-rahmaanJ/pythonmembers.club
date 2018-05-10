string = '''
def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()
 def adapt_datetime(val):
     return val.isoformat(" ")
'''

# single-char keywords
symbols = ['(', ')', '.', '"', '*', '\n', ':', ',', ' ']
# multi-char keywords
keywords = ['def', 'return']
KEYWORDS = symbols + keywords

white_space = ' '
lexeme = ''
last_lexeme = ''

indent_on = False
indent_space_count = 0
indent_level = 0
first_pass_on = True

line_count = 1 # as we start counting from one

for i,char in enumerate(string):
    if char == '\n':
        line_count += 1
        
    if char != white_space: 
        lexeme += char      # adding a char each time
        
    if (i+1 < len(string)): # prevents error
        next_char = string[i+1]      # added for readability
            
        if indent_on and char == white_space:
            indent_space_count += 1
            
        if char == white_space and indent_on and next_char != white_space:
            indent_on = False
            if first_pass_on == True:
                indent_level = indent_space_count
                first_pass_on = False
            # prevents div by zero error on indent_level
            if indent_level != 0: 
                if indent_space_count%indent_level == 0:
                    print('good indentation level detected')
                else:
                    print('bad indentation on line {}'.format(line_count))
                    break
                
        if char == '\n' and next_char == ' ':
            indent_space_count = 0
            indent_on = True
        
        if next_char == white_space or next_char in KEYWORDS or lexeme in KEYWORDS:
            if lexeme != '':
                # print(lexeme.replace('\n', '**newline**'))
                last_lexeme = lexeme # before clearing
                lexeme = ''
                print( '{} level: {} | count: {} | indent_on: {} | first_pass: {}'.format(
                ' '*10, indent_level, indent_space_count, indent_on, first_pass_on) )
