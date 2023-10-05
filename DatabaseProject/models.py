from DatabaseProject import db
from datetime import datetime
class Driver(db.Model):

    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(16), unique=True, index=True)
    name = db.Column(db.String(100), index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    carPlate = db.Column(db.String(16), unique=True, index=True)
    phoneNumber = db.Column(db.String(16), unique=True)
    CEP = db.Column(db.String(32))
    birthDate = db.Column(db.DateTime)
    paymentMethod = db.Column(db.String)
    soleOccupation = db.Column(db.Boolean)
    appDriverMonths = db.Column(db.Integer)
    otherApps = db.Column(db.ARRAY(str))
    uberCategory = db.Column(db.String)
    rentalCar = db.Column(db.Boolean)
    dailyWorkTime = db.Column(db.Integer)
    weekDays = db.Column(db.ARRAY(str))
    uberRating = db.Column(db.Float)
    totalTrips = db.Column(db.Integer)
    carModel = db.Column(db.String(64))
    workArea = db.Column(db.String(100))
    workInterest = db.Column(db.Boolean)


class Anuncio(db.Model):

    __tablename__ = 'anuncios'

    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String)
    createDate = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    updateDate = db.Column(db.DateTime, nullable = False)
    #contractId = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable = False)
    #driverId = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable = False)
