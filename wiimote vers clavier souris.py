def sign(val):# sign - Returns -1 for negatives, 0 for zero and 1 for positives
	return (1 * (val > 0)) + (-1 * (val < 0))

	
def dz(a): #deadzone
	return ScaledDeadzone(a, -jsRange,jsRange,0.03)

def ScaledDeadzone(val, mini, maxi, dz): #Paremeters are Value, Minimum, Maximum and Deadzone Size.
	scaled = filters.mapRange(val,mini,maxi, -1.0,1.0)
	output = 0.0
	if abs(scaled) > dz:
		output = filters.mapRange(abs(scaled), dz, 1.0, 0.0, 1.0) * sign(val)
	return filters.mapRange(output,-1.0,1.0, mini,maxi)

def map_wiimote_to_key(wiimote_button, key):#wiimote_button c'est le bouton de la manette ( voir tout en bas les différent boutons ),key c'est la touche du clavier, écrire Key."la touche que tu veux"
    if wm.button_down(wiimote_button):#si bouton wiimote appuyé alors appuyer sur touche clavier, si relâché alors relâcher touche clavier
        keyboard.setKeyDown(key)
    else:
        keyboard.setKeyUp(key)

def map_wiimote_to_mouse(wiimote_button,MouseButtonIndex):#wiimote_button c'est le bouton de la manette ( voir tout en bas les différent boutons ),MouseButtonIndex c'est les click souris ( 0=click gauche,1=click droit )
	if wm.button_down(wiimote_button):#si bouton wiimote appuyé alors appuyer sur click souris, si relâché alors relâcher click souris
		mouse.setButton(MouseButtonIndex,True)
	else:
		mouse.setButton(MouseButtonIndex,False)

############Assignement des touches et souris############
#########################################################

def UpdateInputs():#definition de la fonction UpdateInputs

#événements souris

	mouse.deltaX = dz(nchk.stick.x)*0.02#mouse.deltaX est la valeur renvoyé par la souris (souris qui:	-va vers la gauche=valeur négative	-est immobile=0		-va vers la gauche=valeur positive)
	mouse.deltaY = -dz(nchk.stick.y)*0.02#mouse.deltaX est la valeur renvoyé par la souris (souris qui:	-va vers le bas=valeur négative		-est immobile=0		-va vers le haut=valeur positive)
		#note: rajouter ou enlever le "-" devant la fonction"dz" pour inverser l'axe X ou l'axe Y
		#note 2: changer le "0.02" pour changer les sensibilités X et Y de la souris
	map_wiimote_to_mouse(WiimoteButtons.A,0)#assigne le bouton A de la manette au clic gauche
	map_wiimote_to_mouse(WiimoteButtons.B,1)#assigne le bouton B de la manette au clic droit

#événements clavier
	map_wiimote_to_key(WiimoteButtons.DPadUp, Key.W)#assigne le bouton haut de la croix directionnelle de la manette a la touche Z
	map_wiimote_to_key(WiimoteButtons.DPadLeft, Key.A)#assigne le bouton gauche de la croix directionnelle de la manette a la touche Q
	map_wiimote_to_key(WiimoteButtons.DPadDown, Key.S)#assigne le bouton bas de la croix directionnelle de la manette a la touche S
	map_wiimote_to_key(WiimoteButtons.DPadRight, Key.D)#assigne le bouton droite de la croix directionnelle de la manette a la touche D
	keyboard.setKey(Key.Space, nchk.buttons.button_down(NunchuckButtons.Z))#assigne le bouton Z du nunchuck a la touche espace
	#note: reconnait le clavier anglais, il faut donc mettre l'équivalent anglais des touches ( ex: W=Z, Q=A )

#########################################################

if starting:#dès que le script est démarré
	jsRange = 100#étalonner le joystick
	wm = wiimote[0].buttons#dès que "wm" est écrit dans le script, c'est comme si on écrivait "wiimote[0].buttons"
	wm.update += UpdateInputs#appeler la fonction UpdateInputs dès qu'il se passe quelque chose sur la wiimote
	nchk = wiimote[0].nunchuck#dès que "nchk" est écrit dans le script, c'est comme si on écrivait "wiimote[0].nunchuck"
	nchk.update += UpdateInputs#appeler la fonction UpdateInputs dès qu'il se passe quelque chose sur le nunchuck


############Boutons Wiimote et Nunchuck############
###################################################
#WiimoteButtons.A
#WiimoteButtons.B
#WiimoteButtons.DPadUp
#WiimoteButtons.DPadDown
#WiimoteButtons.DPadLeft
#WiimoteButtons.DPadRight
#WiimoteButtons.Minus
#WiimoteButtons.Home
#WiimoteButtons.Plus
#WiimoteButtons.One
#WiimoteButtons.Two
#NunchuckButtons.Z
#NunchuckButtons.C
