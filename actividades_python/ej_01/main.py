#se importan LED y button del GPIOZero, asi como el pause y el signal 
from gpiozero import LED, Button
from signal import pause
#se referencia al LED al pin GPIO 19, se conecta a button al pin GPIO 18 
led = LED(19)
button = Button(18)
#Se establecen las acciones a realizar cuado se presione o se suelte el boton

button.when_pressed = led.on
button.when_released = led.off
#se llama a la funcion pause que evita que el script termine inmediatamente 
pause()
