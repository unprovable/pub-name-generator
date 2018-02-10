import random

def read_pubs(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('The','').replace('\n\n',' ').replace('\n',' ') # remove all line breaks
                     # remove all the 'The's... Add them back in later
    return contents

def build_Markov_chain(in_data, chain = {}):
    words = in_data.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index-1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    return chain

def generate_pub_name(chain, leng=random.choice([3,4,5])):
    w1 = random.choice(list(chain.keys())).capitalize() # get a word, add a capital letter
    text = w1
    while len(text.split(' ')) < leng:
        try:
            w2 = random.choice(chain[w1])
            w1 = w2
            text += ' '+ w2
        except:
            pubname = ""
            break
    pubname = "The "+text
    if pubname.endswith("and") or pubname.endswith("the"):
        pubname += " "
        pubname += random.choice(chain["and"])
    return pubname

if __name__ == "__main__":
    print("[i] loading data...")
    fileread = read_pubs("pub-list.txt")
    print("[*] generating chain...")
    chain = build_Markov_chain(fileread)
    print("[i] Done! Here are some random names:")
    for i in range(1,25):
        print(generate_pub_name(chain))
