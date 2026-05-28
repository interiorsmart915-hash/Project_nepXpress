from flask import render_template
class DashboardController:  
    
    def dashboard(self):
        return render_template('dashboard.html')
    
    def admin_dashboard(self):
        return render_template('admin-dashboard.html')
    