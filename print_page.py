from constants import all_text
from constants import replace_symbol
from create_pdf import create_pdf

def single_character_count(input_text):
    input_text = input_text.replace(" ", "")
    for symbol in replace_symbol:
        input_text = input_text.replace(symbol, "")
    
    characters = {} 
    character_set = []
    for i in range(0, len(input_text)):
        if input_text[i] not in character_set:
            character_set.append(input_text[i])
            characters[input_text[i]] = 1
        else:
            characters[input_text[i]] += 1

    return characters

def calc_page(iIndex):
    iPage = iIndex // 6 
    iPage += 1

    iRow = iIndex % 6
    if iRow == 0:
        iRow = 6
        iPage -= 1
    return iPage, iRow


def gen_from_text(input_text):
    if not input_text:
        return []

    if type(input_text) is not list:
        input_text = input_text.replace(" ", "")
        for symbol in replace_symbol:
            input_text = input_text.replace(symbol, "")

    output_list = []
    for i in range(0, len(input_text)):
        show_i = i + 1
        indexText = input_text[i:i+1]
        if input_text[i:i+1] in all_text:
            matchIndex = all_text.index(indexText)
            matchPage, matchRow = calc_page(matchIndex+1)
            #print(f'{show_i:2d}:{indexText}, page:{matchPage} row:{matchRow}, index:{matchIndex}')
            #print(f'{show_i:2d}:{indexText}, page:{matchPage} row:{matchRow}')
            #print(f'{show_i:2d}:{indexText}, 第 {matchPage} 頁 第 {matchRow} 個字')
            output_list.append(f'{show_i:2d}:{indexText}, 第 {matchPage} 頁 第 {matchRow} 個字')
        else:
            #print(f'{show_i:2d}:{indexText}, not found')
            output_list.append(f'{show_i:2d}:{indexText}, not found')

    return output_list

def make_character_info(characters):
    iCount = 0
    output_list = []
    for key, value in characters.items():
        iCount += 1
        output_list.append(f'{iCount:2d} {key} 出現 {value} 次')

    return output_list

def print_lines(lines):
    for line in lines:
        print(line)

if __name__ == "__main__":
    #input_text = "人生到處知何似應似飛鴻踏雪泥泥上偶然留指爪鴻飛哪復計東西老僧已死成新塔壞壁無由見舊題往日崎嶇還記否路長人困蹇驢嘶"

    #input_text = "天門中斷楚江開碧水東流至此回兩岸青山相對出孤帆一片日邊來"
    #print_one(input_text)

    #input_text = "朝辭白帝彩雲間千里江陵一日還兩岸猿聲啼不住輕舟已過萬重山"
    #print_one(input_text)

    input_text = "道可道，非常道。名可名，非常名。無名天地之始；有名萬物之母。故常無欲，以觀其妙；常有欲，以觀其徼。此兩者，同出而異名，同謂之玄。玄之又玄，眾妙之門。"
    gen_lines = gen_from_text(input_text)
    print_lines(gen_lines)
    create_pdf(input_text, gen_lines, "./output/output.pdf")

    single_char = single_character_count(input_text)
    single_char_list = make_character_info(single_char)
    print_lines(single_char_list)
