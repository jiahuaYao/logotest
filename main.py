def on_button_pressed_a():
    if input.logo_is_pressed():
        basic.show_icon(IconNames.TSHIRT)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    basic.show_icon(IconNames.HOUSE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
