from flask import Flask, render_template, request
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

#FLASK_APP=app.py flask run     to run via bash/terminal

app = Flask(__name__)           # placeholder for current module (app.py)
                                #instance of flask app
#app.debug = True                #entering debug mode so that we can see changes made in this code without rerunning the web server

#status of sensor
ledRedSts = "ON"                #heater
wavemakerSts = "ON"
filterSts = 'ON'
fanSts = 'ON'


@app.route('/')                 #default route
def index():

    templateData = { 'ledRed' : ledRedSts,
    'wavemaker' : wavemakerSts,
    'filter' : filterSts,
    'fan' : fanSts}
    return render_template('home.html',**templateData)            #rendering a template called index.html
                                                                  #need to include the templatedata parameter to grab the data in this method

@app.route('/<deviceName>/<action>')                        #put command in address bar
def do(deviceName, action):                                 #deviceName and action values will come from user buttonclick--> described in home.html
    global ledRedSts                            # we must declare these variables as global within the function or initialize within function
    global wavemakerSts                         #if we initilialize these status variables outside of this function ONLY, then we get an error ....
    filterSts = 'OFF'                            #using both methods here just to see what the difference is...
    fanSts = 'OFF'                               #both methods seem valid and work
    nine_amSts = 'OFF'                              #variables must not beign with a name. They must begin with underscore or letter
    noonSts = 'OFF'
    four_pmSts = 'OFF'
    sunsetSts = 'OFF'
    nightSts = 'OFF'
    lightTime = False

    if (deviceName == 'ledRed') and (action == 'on'):
        ledRedSts = "ON"
        #insert rpi/arduino command here
    elif (deviceName == 'ledRed') and (action == 'off'):
        ledRedSts = "OFF"
    elif (deviceName == 'wavemaker') and (action == 'on'):
        wavemakerSts = 'ON'
    elif (deviceName == 'wavemaker') and (action == 'off'):
        wavemakerSts = 'OFF'
    elif (deviceName == 'filter') and (action == 'on'):
        filterSts = 'ON'
    elif (deviceName == 'filter') and (action == 'off'):
        filterSts = 'OFF'
    elif (deviceName == 'fan') and (action == 'on'):
        fanSts = 'ON'
    elif (deviceName == 'fan') and (action == 'off'):
        fanSts = 'OFF'

#only one type of light shall be on at one time
    #working propoerly but how????
    while lightTime == False:
        if (deviceName == '_9am') and (action == 'on'):                                   #light strip commands
            lightTime = True
            nine_amSts = "ON"
            #insert rpi/arduino command here
        elif (deviceName == '_9am') and (action == 'off'):
            lightTime = True
            nine_amSts = "OFF"
        elif (deviceName == 'noon') and (action == 'on'):
            lightTime = True
            noonSts = 'ON'
        elif (deviceName == 'noon') and (action == 'off'):
            lightTime = True
            noonSts = 'OFF'
        elif (deviceName == '_4pm') and (action == 'on'):
            lightTime = True
            four_pmSts = 'ON'
        elif (deviceName == '_4pm') and (action == 'off'):
            lightTime = True
            four_pmSts = 'OFF'
        elif (deviceName == 'sunset') and (action == 'on'):
            lightTime = True
            sunsetSts = 'ON'
        elif (deviceName == 'sunset') and (action == 'off'):
            lightTime = True
            sunsetSts = 'OFF'
        elif (deviceName == 'night') and (action == 'on'):
            lightTime = True
            nightSts = 'ON'
        elif (deviceName == 'night') and (action == 'off'):
            lightTime = True
            nightSts = 'OFF'

    #passing 'ledRedSts' value to 'ledRed' then 'ledRed' is passed to home.html
    templateData = { 'ledRed' : ledRedSts,
                     'wavemaker' : wavemakerSts,
                     'filter' : filterSts,
                     'fan' : fanSts,
                     '_9am' : nine_amSts,
                     'noon' : noonSts,
                     '_4pm' : four_pmSts,
                     'sunset' : sunsetSts,
                     'night' : nightSts
                     }

    return render_template('home.html', **templateData )

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 80,debug = True)

