import gym
import universe
import random

#Her laves Reinforcement miljø'et
def determine_turn(turn, obsevation_n, j, total_sum, previous_total_sum, reward_n):
	#For hver 15 iteration, tag der summen af obsevationer og beregn gennemsnittet
	#Hvis summer er mindre end 0 så ændre retning!
	#så hvis man kan tage 15+ iterationer hvor man får en beløning på hvert step så ved man at man gør noget rigtigt
	if(j >= 15):

		if(total_sum / j == 0):
			turn = True
		else:
			turn = False

		#eftersom vi her allerede nu ved om der skal drejes eller om der ikke skal kan vi resette vores variabler.
		total_sum = 0
		j = 0
		#der gemmes den tidligere score
		previous_total_sum = total_sum	
	else:
		turn = False
	if(obsevation_n != None):
		j+=1
		total_sum += reward_n
	return(turn, j, total_sum, previous_total_sum)  



	

#lav en main metode som beskrivet hvilket miljø vi er i
def main():
	#i hvilket miljø?


	env = gym.make('flashgames.CoasterRacer-v0')
	#Jeg initialicere mit miljø  
	env.configure(remotes=1)
	#klienten er en 'vnc' som er vores AI-Agent
	#remote er min (local-docker kontainer)

	obsevation_n = env.reset()


	#tilføj de variabler du har behov for
	#antal af spil iterationer

	n=0
	j=0

	#summen af antal spil

	total_sum = 0
	previous_total_sum = 0
	turn = False
	#Definer de forskellige slage turns eller de actioner tastaturet laver.

	left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
	right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
	forward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]

	#Hoved logik
	while True:
		#lav en counter som tæller antallet af iterationer
		n += 1

		if(n > 1):
		#hvis der skal bruges mere end ét træk så undersøg om der er behov for et "turn"
			if(obsevation_n[0] != None):
				#gem "beløningen" i den tidligere score
				previous_total_sum = reward_n[0]

				#hvis der er behov for et turn
				if(turn):
					#vælge en random handling
					#hvor skal den så dreje hen?
					event = random.choise([left,right])
					#ud fra det event der lige er sket skal der så laves en handling?
					action_n = [event for obsevation in obsevation_n]
					turn = False
		#så i tilfælde af der ikke skal drejes
		elif(~turn):
			#hvis der ikke skal drejes så kør ligeud

			action_n = [forward for obsevation in obsevation_n]
			#hvis der er en obsevation betyder det at spillet er startet om der skal tjekkes om der skal drejes

		if(obsevation_n[0] != None):
			turn, j, total_sum, previous_total_sum = determine_turn(turn, obsevation_n, j, total_sum, previous_total_sum, reward_n[0])


		#gem variablerne for hver iteration
		obsevation_n, reward_n, done_n, info = env.step(action_n)
		#husk at miljøet har behov for at "render" efter hvert step
		env.render()

if __name__ == "__main__":
	main()






