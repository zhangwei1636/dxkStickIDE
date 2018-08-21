from microbit import *
from mb import get_type
ta,tb=0,0
display.clear()
while 1:
    ta=get_type(22)
    if ta:
        for i in (0,1):
            for j in range(5):
                display.set_pixel(i,j,9)
    else:
        for i in (0,1):
            for j in range(5):
                display.set_pixel(i,j,0)
    tb=get_type(23)
    if tb:
        for i in (0,1):
            for j in range(5):
                display.set_pixel(i+3,j,9)
    else:
        for i in (0,1):
            for j in range(5):
                display.set_pixel(i+3,j,0)
    if ta==None or tb==None:
        continue
    if ta>tb:
        ta,tb=tb,ta
    if ta==1 and tb==2:
        # 测试OLED、温湿度、拨码
        import oled,temp_humi
        display.clear()
        while not (button_a.get_presses()+button_b.get_presses()):
            chn=i2c.read(0x20,1)[0]
            ptr=1
            for i in range(10):
                display.set_pixel(i%4,i//4,9*bool(chn&ptr))
                ptr*=2
            oled.clear()
            temp,humi=temp_humi.temp_humi()
            oled.show(0,0,b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6'%temp)
            oled.show(2,0,b'\xca\xaa\xb6\xc8\xa3\xba%s%%'%humi)
            temp,humi=temp_humi.temp(),temp_humi.humi()
            oled.show(4,0,b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6'%temp)
            oled.show(6,0,b'\xca\xaa\xb6\xc8\xa3\xba%s%%'%humi)
            sleep(500)
        break
    elif ta==3 and tb==4:
        # 测试LED、电位器
        display.show(Image.HAPPY)
        import led,poten
        led.off()
        flag,counter=0,0
        while not (button_a.get_presses()+button_b.get_presses()):
            counter+=poten.value()
            if counter>=4096:
                counter-=4096
                if flag:
                    led.off()
                    flag=0
                else:
                    led.on()
                    flag=1
        break
    else:
        sleep(10)
display.clear()