from base64 import *

(a,b,c,d) = (70979532922714726005950999456852628059532311148206783766093435787123197232647457984708147232760389536909544842840637467696937247459692963867502414810678283883,\
		 410160563951884215575048454512643924110754613022033438323252774235720751108752406710922147713801605550783526394303466164956199373182495367988753890137739783998143,\
		 9705303629766926756962115878153448813784738656130121062206508648548600939875290939376784022191357893940268634609309770116427301779332901287292278132375644469,\
		 72146675268984268926692535405591086289578472817949676001189738433298612151131667956807702171430844914392838506834908686053308289180788419151330429940895945011)

def F(x):
	return (a*x*x + b*x + c)%d

def G(message):
	n = len(message)
	L = message[0:(n/2)]
	R = message[(n/2):n]

	L = int(L.encode("hex"), 16)
	R = int(R.encode("hex"), 16)

	return (L,R)

def Encode(L, R):
	rounds = 0xbeef
	for i in xrange(rounds):
		(L,R) = (R, L^F(R))

	L = hex(L).replace("0x", "").replace("L", "")
	R = hex(R).replace("0x", "").replace("L", "")

	return R+L

FLAG = r"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

(L, R) = G(FLAG)
print b64encode(Encode(L, R).decode("hex"))

# G2MXNZJsXBMWIbKI45ztcVlXZnYAk/UNPsuo0vI6tidpVEwlxtK6vGCVZ4JxS4jqTPCZCA1I8Ji6KVhpwzBbRhtWVZo1rPk5yVupnOiGtp+mzncHNe5Su+jazP7+c3yIygXm1POM0TzD8vesaIZLxZy5kbNMV7GrNLlS0iG2qfQV3cE=