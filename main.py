from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from helpers import screen_helper
from kivy.core.window import Window

Window.size = (400,500)


class HomeScreen(Screen):
   pass

class NOOScreen(Screen):
   pass

class SOSScreen(Screen):
   pass

class FireScreen(Screen):
   pass

class FirstAidScreen(Screen):
   pass

class StrangerScreen(Screen):
   pass

class WeatherScreen(Screen):
   pass

class PowerOutScreen(Screen):
   pass

class LockedOutScreen(Screen):
   pass

class ContactInfoScreen(Screen):
   pass

class ParentScreen(Screen):
   pass

class EditFireScreen(Screen):
   pass

class EditFirstAidScreen(Screen):
   pass

class EditStrangerScreen(Screen):
   pass

class EditWeatherScreen(Screen):
   pass

class EditPowerOutScreen(Screen):
   pass

class EditLockedOutScreen(Screen):
   pass

class EditContactInfoScreen(Screen):
   pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(NOOScreen(name="noo"))
sm.add_widget(SOSScreen(name="sos"))
sm.add_widget(FireScreen(name="fire"))
sm.add_widget(FirstAidScreen(name="first_aid"))
sm.add_widget(StrangerScreen(name="stranger"))
sm.add_widget(WeatherScreen(name="weather"))
sm.add_widget(PowerOutScreen(name="power_out"))
sm.add_widget(LockedOutScreen(name="locked_out"))
sm.add_widget(ContactInfoScreen(name="contact_info"))
sm.add_widget(ParentScreen(name="parent"))
sm.add_widget(EditFireScreen(name="edit_fire"))
sm.add_widget(EditFirstAidScreen(name="edit_first_aid"))
sm.add_widget(EditStrangerScreen(name="edit_stranger"))
sm.add_widget(EditWeatherScreen(name="edit_weather"))
sm.add_widget(EditPowerOutScreen(name="edit_power_out"))
sm.add_widget(EditLockedOutScreen(name="edit_locked_out"))
sm.add_widget(EditContactInfoScreen(name="edit_contact_info"))

class KidSafeApp(MDApp):
  def build(self):
      self.theme_cls.primary_palette = "Gray"
      self.theme_cls.primary_hue = "A700"
      self.theme_cls.theme_style = "Light"

      screen = Builder.load_string(screen_helper)
      return screen

  def get_fire_data(self):
      print(self.root.ids.scr_mngr.get_screen("fire").ids.fire_label.text)
      #self.root.ids.
      #print(self.root.ids.scr_mngr.edit_fire.fire_input.text)
      #self.root.



KidSafeApp().run()
