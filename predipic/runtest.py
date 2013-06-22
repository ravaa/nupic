#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""A simple client to create a CLA model for hotgym."""

import csv
import datetime

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.data.inference_shifter import InferenceShifter

import model_params


DATA_PATH = "/nupic/predipic/data/test.csv"

def createModel():
    return ModelFactory.create(model_params.MODEL_PARAMS)

def runSensorSweep():
    results = []
    model = createModel()
    model.enableInference({'predictionSteps': [1],
                           'predictedField': 'active_sensor',
                           'numRecords': 4000})

    with open (DATA_PATH) as fin:
        reader = csv.reader(fin)
        headers = reader.next()
        print headers
        print reader.next()
        print reader.next()
        inf_shift = InferenceShifter()
        for record in reader:
            modelInput = dict(zip(headers, record))
            modelInput["active_sensor"] = modelInput["active_sensor"]
            result = inf_shift.shift(model.run(modelInput))
            results.append(result)
    return results

def print_report(records):
    report_row = "Sensor: {0} | Prediction: {1}"
    for record in records:
        inferred = record.inferences['multiStepPredictions'][1]
        if inferred:
            inferred = sorted(inferred.items(), key=lambda x: x[1])[-1][0]
        print report_row.format(record.rawInput['active_sensor'],
                                inferred)
                

if __name__ == "__main__":
    records = runSensorSweep()
    print_report(records)
