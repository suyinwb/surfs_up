import datetime as dt
import numpy as np
import pandas as pd

#sqlLite DB dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Access DB
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect SB
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#session link
session = Session(engine)

# Set up Flask app
app = Flask(__name__)

#Define root route
@app.route("/")

#Root route information
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#Precipitation route
@app.route("/api/v1.0/precipitation")

#Precipitation route information
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#Stations route
@app.route("/api/v1.0/stations")

#Stations route information
def stations():
   results = session.query(Station.station).all()
   # Unravel results into a one-dimensional array and convert to a list
   stations = list(np.ravel(results))
   return jsonify(stations=stations)

#Temperation Observations route
@app.route("/api/v1.0/tobs")

#Temperation Observations route information
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
