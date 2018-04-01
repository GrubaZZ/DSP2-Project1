import math

PI = 3.14159265
SAMPLE_RATE = 16000

# ime fajla u koji smestam vrednosti koeficijenata
default_filename = "vrednosti.txt"

def calculate_alpha(freq):
	
	alpha = (1 + math.sin(freq))/math.cos(freq)

	if not(alpha >= -1 and alpha <= 1):
		alpha = (1 - math.sin(freq))/math.cos(freq)

	return alpha


def calculate_beta(omega):

	beta = math.cos(omega)

	return beta


# granicna ucestanost za Bass (LP)
f0 = 200 / SAMPLE_RATE
w0 = 2*PI*f0

# centralna ucestanost (f1, w1) i sirina opsega za Middle1 (Peek1) 
f1 = 550 / SAMPLE_RATE
df1 = 310 / SAMPLE_RATE

w1 = 2*PI*f1
dw1 = 2*PI*df1

# centralna ucestanost (f2, w2) i sirina opsega za Middle2 (Peek2)
f2 = 2830 / SAMPLE_RATE
df2 = 1220 / SAMPLE_RATE

w2 = 2*PI*f2
dw2 = 2*PI*df2

# granicna ucestanost za Trebble (HP)
f3 = 4800 / SAMPLE_RATE
w3 = 2*PI*f3

# koeficijenti alpha i beta za custom_shelving_filtere u zadatku
alpha0 = calculate_alpha(w0)
alpha1 = calculate_alpha(dw1)
beta1 = calculate_beta(w1)
alpha2 = calculate_alpha(dw2)
beta2 = calculate_beta(w2)
alpha3 = calculate_alpha(w3)

file = open(default_filename, "w")

file.write("alpha0 = " + str(alpha0) + "\n")
file.write("alpha1 = " + str(alpha1) + "\n")
file.write("alpha2 = " + str(alpha2) + "\n")
file.write("alpha3 = " + str(alpha3) + "\n")
file.write("beta1 = " + str(beta1) + "\n")
file.write("beta2 = " + str(beta2))

file.close()
