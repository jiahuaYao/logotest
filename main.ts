input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (input.logoIsPressed()) {
        basic.showIcon(IconNames.TShirt)
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showIcon(IconNames.House)
})
