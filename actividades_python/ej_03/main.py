from gpiozero import LED, Buzzer
from signal import pause

buzzer = Buzzer(22)
led_rojo = LED(19)
led_verde = LED(26)
led_azul = LED(13)
while True:
	comando = input
("Activa segun lo que se ingrese:  buzzer o colores:")
		if comando == " colores ":
		opcion = input
("Ingrese opcion: r(rojo), v(verde) o a(azul): ")
		elif comando == "buzzer":
		opcion = input
("Ingrese opcion: on u off: ")

		if comando == "buzzer":
		if opcion == "encendido":
			buzzer.on()
		elif opcion == "apagado":
			buzzer.off()

	elif comando == "colores":
		if opcion == "r":
			led_r.toggle()
		elif opcion == "v":
			led_v.toggle()
		elif opcion == "a":
			led_a.toggle()

pause()
