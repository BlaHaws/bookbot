def num_of_words(contents):
    words = contents.strip().split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def num_of_chars(contents):
    strp_contents = "".join(contents.strip().lower().split())
    alpha_unique = []
    for char in list(set(list(strp_contents))):
        if char.isalpha():
            alpha_unique.append(char)
    alpha_count = dict.fromkeys(alpha_unique, 0)
    for x in list(strp_contents):
        if x.isalpha():
            alpha_count[x] += 1
    return alpha_count

def sort_on(items):
    return items["count"]

def order_list(contents):
    def sort_on(dict_item):
        return dict_item['count']
    word_dict = num_of_chars(contents)
    word_list = []
    for set in word_dict:
        name = set
        count = word_dict[set]
        word_list.append({"name": name, "count": count})
    word_list.sort(reverse=True, key=sort_on)
    for item in word_list:
        print(f"{item['name']}: {item['count']}")
    