from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from projekt import szukarka 
from projekt import check_user_existence 
from projekt import add_user


class MyPopup(Popup):

    pass



<<<<<<< HEAD
class FirstWindow(Screen):
    
=======


class SecondWindow(Screen):
>>>>>>> 26147764cb2fa6c363c846f2889028e5e6de83d2
    pass

class GuestApp(Screen,Widget):
    def GuestPress(self):
        ingredients= self.ids.guest_ingredients.text
        self.ids.guest_space.text=getRecipe(ingredients)
    pass

<<<<<<< HEAD
def open_pop_up(self):
    pops = MyPopup()
    pops.open()




class SecondWindow(Screen):
         
            

         def verification(self):
            login = self.ids.login.text
            password = self.ids.password.text
            if check_user_existence(login):
                App.get_running_app().root.current='third'
                App.get_running_app().root.transition.direction = "up"
            else:
                App.get_running_app().root.current='second'
                open_pop_up(self)
                


class ThirdWindow(Screen):
    def press(self):
        ingredients= self.ids.ingredients.text
        recipe=szukarka(ingredients)
        final_recipe=""
        for item in recipe:
            final_recipe=final_recipe+item+"\n"+"\n"
        
        self.ids.recipe.text=final_recipe
        
    pass

class RegisterWindow(Screen):
    def verification(self):
        name=self.ids.name.text
        surname=self.ids.surname.text
        passw=self.ids.register_passw.text
        email= self.ids.email.text
        if check_user_existence(email):
            App.get_running_app().root.current='second'
        
        elif name==""or surname==""or passw==""or email=="":
            open_pop_up(self)
        else:
            add_user(email,passw,name,surname)
            App.get_running_app().root.current='second'
         
=======
class ThirdWindow(Screen,Widget):
    def press(self):
        ingredients= self.ids.ingredients.text
        self.ids.recipe.text=getRecipe(ingredients)
>>>>>>> 26147764cb2fa6c363c846f2889028e5e6de83d2
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


