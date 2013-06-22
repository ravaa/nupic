#!/usr/bin/env python
from flask import Flask, render_template, request
from runtest import runSensorSweep
try:
    import json
except ImportError, e:
    import simplejson as json

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        records = []
        results = runSensorSweep()
        for record in results:
            sensor = record.rawInput['active_sensor']
            predicted = record.inferences['multiStepPredictions'].get(1, None)

            if not predicted:
                predicted = {'sensor': 0}

            predicted = sorted(predicted.items(), key=lambda x: x[1])[-1][0]

            r = dict(active_sensor=sensor,
                     prediction=predicted)
            records.append(r)

        return render_template('main.html', records=records)

    if request.method == 'GET':
        return render_template('main.html')



