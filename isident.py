var="booby"
print(var.isidentifier())
var="bobb12"
print(var.isidentifier())
var="bobby@22"
print(var.isidentifier())
var="44bobby"
print(var.isidentifier())
print("===================================")
a="bobby    bobby "
print(a.isspace())
a="               "
print(a.isspace())
print("===================================")
a="I am a student"
print(a.istitle())
a="I Am A Student"
print(a.istitle())
print("===================================")
a="I AM A STUDENT"
print(a.isupper())
a="am a student"
print(a.islower())
print("===================================")
