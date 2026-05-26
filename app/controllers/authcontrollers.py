from flask import render_template
class AuthController:
 
    def login(self):
        return render_template('login.html')
    
    def register(self):
        return render_template('register.html')

    def settings(self):
        return render_template('settings.html')
    
    def base(self):
        return render_template('base.html')

    
 
