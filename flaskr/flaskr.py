import plivo, plivoxml
from flask import Flask, request


app = Flask(__name__)

@app.route("/receive_sms/", methods=['GET','POST'])
def receive_sms():

    # Sender's phone numer
    from_number = request.values.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')

    # The text which was received
    text = request.values.get('Text')

    # Print the message
    print 'Text received: %s - From: %s' % (text, from_number)
    return "Text received"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    # Sample successful output
    # Text received: Hello, from Plivo - From: 2222222222








(40.714224,-73.961452,5554342345)

#/register/<lat>/<long>/<tel>    /events?lat=23324324&long=3324324&tel=24324      /events  {"tel": "43534", "long":"2432"}

#register
def post(self):
    e = Event(key=Key(Event, tel), lat=self.POST.get('lat'), long=self.POST.get('long'))
    e.put()


#/events/<tel>

# events
def get(self, tel):
    e = Events.find_by_id(tel).get()
    self.render_template('events.html', event=e)








