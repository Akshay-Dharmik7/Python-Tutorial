text = "968-Maria, ( D@t@ Engineer ) ;; 27y  "

# output = "Name: maria | role: data engineer | age: 27"

print(text)
print("Name:", text[4:9], "|", "role:", text[13:26].replace("@", "a"), "|","age:",  text.rstrip()[-4:-1])
