Schema -- What data in and out?
Models -- Defines database structure, How is data stored permanately
Service -- Contains the business logic, should this be allowed?
Repository -- Talks to the database. Fetch or persist data.
Controller -- Handles the HTTP behavior, eg User asked fo X --> call service.
Router -- Maps endpoint --> controller, where should this request go?



Schema validates input
    ↓
Controller receives request
    ↓
Service decides if allowed
    ↓
Repository saves it
    ↓
Model maps to DB
