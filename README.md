# Customer Lifetime Value Project

## 1. Installation
  1. install docker and docker-compose
  1. enter the project directory `cd /lesara_test`
  1. `docker-compose build`
  1. in new terminal execute `docker-compose exec web bash`
     - `flask fill_db orders.csv`
     - wait a few minutes to insert dataset to database
  1. `docker-compose up`
  1. Now application is running on `localhost:8000`
## 2. API
  1. `/` - main page
  1. `/predict/<customer_id>` - get predicted CLV value for given customer id

## 3. Author
  Marcin Nozynski

  marcin.nozynski@gmail.com

  www.linkedin.com/in/marcin-nozynski/