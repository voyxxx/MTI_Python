; Изначально скрипт выключен
ScriptEnabled := 0 

Esc:: ; При нажатии клавиши Esc
{
    ; инвертируем состояние скрипта(включаем скрипт)
    ScriptEnabled := !ScriptEnabled
    ; если скрипт включен, начинаем кликать мышью
    if (ScriptEnabled) {
        ToolTip, Script on
        SetTimer, ClickMouse, 100 
    }
    else {
        ToolTip, Script off
        SetTimer, ClickMouse, off
    }
    return
}

ClickMouse:
{
    Click
    return
}