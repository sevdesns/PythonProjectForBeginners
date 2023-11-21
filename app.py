from tkinter import Label
import kivy
from kivy.app import App
from  kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooser
class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout =BoxLayout(orientation = 'vertical', padding= 30, spacing =10)
        
        head_label = Label(text="Python User Registration App",font_size=26,bold=True,height=40)
        
        
        name_label = Label(text="Name:",font_size=18)
        self.name_input = TextInput(multiline=False, font_size =18)
        
        email_label = Label(text="Email:",font_size=18)
        self.email_input = TextInput(multiline=False, font_size =18)
        password_label = Label(text="Password:",font_size=18)
        self.password_input = TextInput(multiline=False, font_size =18,password=True)
        confirm_label = Label(text="Confirm Password:",font_size=18)
        self.confirm_input = TextInput(multiline=False, font_size =18,password = True)
        
        submit_button= Button(text='Register',font_size=18, on_press=self.register)
        
        
        
        
        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(submit_button)

        
        return layout
    
    def register(self,instance):
       name = self.name_input.text
       email = self.email_input.text
       password = self.password_input.text
       confirm_password = self.confirm_input.text

       if name.strip() == '' or email.strip()== '' or password.strip == '' or confirm_password.strip=='':
           message = "Please fill in the fields"
       elif    password != confirm_password:
          message = "Password do not match "

       else:
          new_var = '.txt'
          filename: name + new_var
          with open(filename,"w") as file:
            file.write('Name: {}\n'.format(name))
            file.write('Email: {}\n'.format(name))
            file.write('Password: {}\n'.format(name))
          message = "Registration successfull! \nName: {}\nEmail: {}".format(name,email)

       popup = Popup(title = "Registration Status",content=Label(text=message),size_hint=(None,None),size=(400,200)) 
       popup.open()
       
if __name__ == '__main__':
 RegistrationApp().run()
