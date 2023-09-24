from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from projekt import szukarka
class FirstWindow(Screen):
    pass





class SecondWindow(Screen):
    pass

class GuestApp(Screen,Widget):
    def GuestPress(self):
        ingredients= self.ids.guest_ingredients.text
        self.ids.guest_space.text=getRecipe(ingredients)
    pass

class ThirdWindow(Screen,Widget):
    def press(self):
        ingredients= self.ids.ingredients.text
        self.ids.recipe.text=getRecipe(ingredients)
    pass


def getRecipe(id):
    recipe=szukarka(id)
    final_recipe=""
    for item in recipe:
        final_recipe=final_recipe+item+"\n"+"\n"
    return final_recipe




class WindowManager(ScreenManager):
    pass

class Widgets(Widget): 
    pass



kv = Builder.load_file("proto.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
