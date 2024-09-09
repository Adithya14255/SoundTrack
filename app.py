"""
    Eltrack - prototype
    by - Adithya G

"""


from flask import Flask, render_template, request
import folium
import math
import random
from opencage.geocoder import OpenCageGeocode

# initiaizing app
app = Flask(__name__)


#home route
@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        #get the phone number from user
        phone_number = request.form['phone']

        key = "35fe7e54863942898334ae1ccc9d1757"
        geocoder = OpenCageGeocode(key)
        
        #create the map using folium acc to coordinates
        myMap = folium.Map(location = [1,1],zoom_start=9)

        #adding the icons for the elephant and the train
        icon1 = folium.features.CustomIcon("static/train.png", icon_size=(70,70))
        
        #using random to determine the location of the train 
        #this is done only as example, supposed to be retrived from real time train data
        x= random.randrange(-100,100,3)/3000
        y= random.randrange(-100,100,3)/3000
        
        
        #save the map to templates
        myMap.save("templates/mylocation.html")
        
        #return data for zone and distance
        return render_template('home.html')
    return render_template('home.html')

#route for map
@app.route('/mylocation',methods=['GET', 'POST'])
def mylocation():
    return render_template('mylocation.html')

#Flask app run 
if __name__ == '__main__':
    app.run(debug=True)

