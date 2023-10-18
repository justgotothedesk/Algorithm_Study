import string
import operator
import requests

# 암호 키 초기화
key = {}

# 암호문 정의
ciphertext1 = "Uz qso vuohxmopv gpozpevsg zwsz opfpesx udbmetsx aiz vuephz hmdzshzo wsfp appd tsvp quzw ymxuzuhsx epyepopdzszufpo mb zwp fupz hmdj ud tmohmq.".upper()
ciphertext2 = "Zbzvepiz uaywpaz upa pbxpah nboarbuv upyu taxyuaz upa xqoz yto hybzaz hqwcz. Pa uqq wqtwrioaz upyu yrr bz larr. Upbz itbmahza tql lbupqiu y jyzuah zaajz uq pbj tabupah zuahbra tqh nahubra. Aywp yuqj qn upyu zuqta, aywp jbtahyr nryca qn upbz jqituybt nirr qn tbxpu, yrqta nqhjz y lqhro. Upa zuhixxra buzarn uq upa pabxpuz bz atqixp uq nbrr y jyt'z payhu. Qta jizu bjyxbta Zbzvepiz pyeev.".upper()

# 텍스트 입력 및 정제 함수
def Input(t):
   text = t
   for i in ["\"", ".", ",", "'", "-"]:
      text = text.replace(i, "")
   return text

# 기본적인 전처리 함수
def BasicProcess(text):
   table = []
   # 각 알파벳 빈도수 카운트
   for alphabet in string.ascii_uppercase:
      table.append([alphabet, text.count(alphabet)])
   table.sort(key=lambda x: x[1], reverse=True)
   print("\n< Frequency Count Table >")
   for i in range(len(table)):
      print("[" + table[i][0] + " : " + str(table[i][1]) + "]", end=" ")
      if (i + 1) % 4 == 0:
         print("")

   # 가장 많이 나타나는 알파벳 치환
   text = text.replace(table[0][0], 'e')
   key[table[0][0]] = 'e'

   # 'the' 및 'that'과 같은 일부 일반적인 단어 치환
   for word in ["the", "that"]:
      wordList = text.split(' ')
      words = {}
      for i in wordList:
         if len(i) == len(word) and i[-1] == word[-1]:
            if word == "that" and i[:2] != "th":
               continue
            if i not in words:
               words[i] = 1
            else:
               words[i] += 1
      if words == {}:
         continue
      words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
      text = Substitution(text, words[0][0], word)

   return text

# 자동 복호화 함수
def AutoProcess(text):
   wordList = text.split(" ")
   words = {}

   # 각 단어의 알파벳 개수 카운트
   for i in wordList:
      if i in words:
         continue
      else:
         words[i] = 0
      for j in i:
         if j in string.ascii_lowercase:
               words[i] += 1
      if words[i] == len(i):
         del words[i]
   words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
   
   possible = []
   for i in words:
      possible = SearchWord(i[0])
      if len(possible) == 1:
         text = Substitution(text, i[0], possible[0])
         print("복호화한 단어: " + possible[0])
         break
   return text

# 치환 함수
def Substitution(text, oldWord, newWord):
   for i in range(len(newWord)):
      if oldWord[i] in string.ascii_uppercase:
         text = text.replace(oldWord[i], newWord[i])
         key[oldWord[i]] = newWord[i]
   return text

# 단어 검색 함수
def SearchWord(word):
   URL = "https://www.onelook.com"
   words = []
   result = ""

   # 알파벳의 위치 마스킹
   for i in range(len(word)):
      if word[i] in string.ascii_uppercase:
         word = word[:i] + '*' + word[i+1:]

   params = {'w': word, "scwo": 1, "sswo": 1, "ssbp": 1}
   res = requests.get(URL, params=params)
   if "Sorry, there are no words matching" not in res.text:
      for num in range(res.text.count(". <a href")):
         start = res.text.index(str(num+1) + ". ") + 15 + len(str(num+1))
         end = res.text[start:].index("\"")
         result = res.text[start:start+end]
         if len(result) == len(word):
            words.append(result)

   for i in words:
      for j in range(len(word)):
         if word[j] != '*' and word[j] != i[j]:
            words.remove(i)
            break

   return words

# 암호문 입력
print("\nInput Ciphertext")
print("----------------")
print(ciphertext1.lower())
ciphertext = BasicProcess(Input(ciphertext1))
plaintext = ciphertext

# 자동 복호화 진행
print("\n\n복호화 중입니다. 시간이 조금 걸릴 수 있습니다.")
for i in range(10):
    complete=0
    plaintext = AutoProcess(plaintext)
    for i in string.ascii_uppercase:
        if i in plaintext:
            complete=-1
    if complete==0:
        break
 
print("\n< Plaintext >")
print(plaintext)
print("\n< Key Table >")
key = sorted(key.items(), key=operator.itemgetter(0))
for k,v in key:
   print("["+k+" : "+v+"]", end=" ")

key = {}

# 암호문 입력
print("\nInput Ciphertext")
print("----------------")
print(ciphertext2.lower())
ciphertext = BasicProcess(Input(ciphertext2))
plaintext = ciphertext

# 자동 복호화 진행
print("\n\n복호화 중입니다. 시간이 조금 걸릴 수 있습니다.")
while(True):
   complete = 0
   plaintext = AutoProcess(plaintext)
   for i in string.ascii_uppercase:
      if i in plaintext:
         complete = -1
   if complete == 0:
      break

# 복호문 출력
print("\n< Plaintext >")
print(plaintext)
print("\n< Key Table >")
key = sorted(key.items(), key=operator.itemgetter(0))
for k, v in key:
   print("[" + k + " : " + v + "]", end=" ")
