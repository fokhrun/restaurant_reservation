
import os
from datetime import date
from calendar import monthrange
from itertools import product
from flask_migrate import Migrate, upgrade
from app import db, create_app
from app.models import User, Role, Table, Reservation, ReservationSlot


app = create_app(os.getenv("FLASK_CONFIG"))
migrate = Migrate(app, db)

"""
Migration commands

flask db init
flask db migrate -m "message"
flask db upgrade
flask db stamp head
flask db downgrade
"""

with app.app_context():
    print (db)
    upgrade()

    db.drop_all()
    db.create_all()

    admin_role = Role(name='Admin')
    guest_role = Role(name='Guest')

    users = [
        User(username='john', role=admin_role, email='john@gmail.com', password='123'),
        User(username='sobhani', role=guest_role, email='sobhani@gmail.com', password='123'),
        User(username='aatif', role=guest_role, email='aatif@gmail.com', password='123')
    ]

    tables = [
        Table(table_capacity="two"),
        Table(table_capacity="four"),
        Table(table_capacity="six"),
        Table(table_capacity="two"),
        Table(table_capacity="four"),
        Table(table_capacity="six")
    ]

    db.session.add_all([admin_role, guest_role, *users, *tables])

    year = 2023
    month = 11
    _, num_days = monthrange(year, month)
    days = [date(year, month, day) for day in range(1, num_days + 1)]
    for date_slot, reservation_slot, table in product(days, ReservationSlot, tables):
        db.session.add(
            Reservation(
                reservation_time_slot=reservation_slot,
                table=table,
                reservation_date=date_slot,
                reservation_status=False
            )
        )

    db.session.commit()

    for _ in Role.query.all():
        print(_)

    for _ in User.query.all():
        print(_)

    for _ in Table.query.all():
        print(_)

    for _ in Reservation.query.all():
        print(_)
