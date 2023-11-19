# Spice Magic

[Spice Magic](https://restaurant-binita-99be9591d7d4.herokuapp.com/) is a full stack restaurant website. The site provides 
- the site guests to see the restaurant menu
- the site owner to manage reservations for its restaurant guests through a centrally managed reservation database
- The site provides a role-based management of reservation database
zzzz
# Requirements

## Functional requirements

The site supports three types of users:
- `visitor`: can visit publicly available pages, anyone who landed in the site
- `guest`: can reserve tables in the restaurant on his own
- `admin`: 
    - can create reservation slots 
    - can cancel anyone's reservation (to handle unforeseeable situations)
    - can book reservation on behalf of any restaurant customer (offline booking)

The site has the following pages: 
1. `home`: provides information about the restaurant, such as cousine, menu, serving hours, contact, etc., for any site visitors
2. `registration`: registration for new guest users
3. `login`: login for both `guest` and `admin` users
    a. any user can log in using his credentials
    b. `user` who cannot be authenticated are redirected to the login page with an error message 
4. `reserve`: 
    1. `guest` can 
        - view available reservations within the next two weeks from today 
        - can see his resevations 
        - make reservations for any available time for any number of guests within the next two weeks from today
            - can add a remark about reservations
        - cancel already made reservations
        - cannot reserve table reserved by someone else

    2. `admin` can 
        - view any reservations status of any table made by anyone
        - make reservations for anyone
            - can add a remark about reservations
        - cancel anyone's reservation
    3. `reservation_admin` can
        - create new type of tables 
        - remove any existing type of tables
        - create any new reservation slot
        - remove any existing reservation slot


## Tecnical Design

### High-level tech stack

- Front End: [Bootstrap Framework](https://getbootstrap.com/docs/5.3/getting-started/introduction/) (HTML, CSS, Javascript)
- Back End: [Flask Framework](https://flask.palletsprojects.com/en/3.0.x/) (Python)
- Database: [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)

### High-level architecture

### Data model

![Data Model]("https://github.com/fokhrun/restaurant_reservation/docs/images/data_model.png")


#### Password Management

#### Current User

# Future improvements

## Model
- must
    - User
        - validation for `email` to be actual email address
- should
    - User
        - make `role` non-nullable
- could
    - User

    -   
