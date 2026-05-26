from flask import Blueprint
from app.controllers.authcontrollers import AuthController
class Authroutes:
   def __init__(self):
      self.bp=Blueprint("auth",__name__)
      self.controller=AuthController()

   def login(self):
   
     
      self.bp.route("/login", methods=["GET", "POST"])(
            self.controller.login
      )
      self.bp.route("/register", methods=["GET", "POST"])(
            self.controller.register
      )
       
      self.bp.route("/settings", methods=["GET", "POST"])(
            self.controller.settings
      )
      self.bp.route("/base", methods=["GET", "POST"])(
            self.controller.base
      )
      return self.bp    