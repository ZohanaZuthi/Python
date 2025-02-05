# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
import json
# if you have json string you can parse it by using json.loads( )method
# the result will be a pyhton dictionary
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
print(x)
# parse x:
y = json.loads(x)
print(x)
# the result is a Python dictionary:
print(y["age"])
# again to convert into json we can use json.dunps()
k=json.dumps(y)
print(k)
# to define the parameters or space
print(json.dumps(y,indent=1))
print(json.dumps(y, indent=4, separators=(". ", " = ")))
print(json.dumps(y, indent=4, sort_keys=True))