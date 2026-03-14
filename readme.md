#Mosa Platform

Overview

#Mosa is a location-aware donation platform that connects individuals with nearby schools in need of resources. The platform enables donors to discover schools, view their needs, and contribute items or resources that can be delivered through coordinated courier services.

The goal of Mosa is to simplify the process of giving while ensuring donations reach schools that need them most.

## Problem

Many schools lack basic resources, while many individuals and organizations are willing to help but do not know where or how to contribute effectively. Traditional donation processes are fragmented and lack transparency.

## Solution

Mosa provides a centralized platform where:

* Schools can create profiles and list their needs.
* Donors can discover nearby schools using geolocation.
* Donations can be matched to real needs.
* Deliveries can be coordinated through courier services.

## Key Features

### School Discovery

Users can find nearby schools based on geographic location.

### School Profiles

Each school can create and maintain a profile that lists their needs and priorities.

### Donation Matching

Donors can view listed needs and commit to fulfilling specific items or resources.

### Courier Coordination

The platform supports coordination with courier services for delivery of donated items.

## Architecture

The backend follows a modular architecture to support scalability and maintainability.

Example structure:

```
app/
  api/
  services/
  models/
  schemas/
  repository/
  core/
```

## Tech Stack

**Backend**

* Python
* FastAPI

**Database**

* PostgreSQL

**Infrastructure / DevOps**

* Docker
* GitHub

**Integrations**

* Google Maps API for geolocation

## Example Core Entities

* Users
* Schools
* SchoolNeeds
* Donations
* CourierDeliveries

## Getting Started

### Prerequisites

* Python 3.10+
* PostgreSQL
* Docker (optional)

### Installation

Clone the repository:

```
git clone https://github.com/devchalatse/Mosa-V1.git
```

Navigate to the project directory:

```
cd Mosa-V1
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
uvicorn app.main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

Interactive API docs:

```
http://localhost:8000/docs
```

## Roadmap

* User authentication and authorization
* School verification process
* Donation tracking
* Courier integration
* Mobile application integration

## Project Status

This project is currently in active development.

## Author

Thabo Kenneth Chalatse

GitHub: [https://github.com/devchalatse](https://github.com/devchalatse)

## License

This project is open-source and available for learning and experimentation.

