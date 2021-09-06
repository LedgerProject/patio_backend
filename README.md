
# Patio Smart Community Brain - Backend Django App

This repository contains the django app in charge of managing the energy data saved to the SaaS backend [Supervecina](https://www.supervecina.com) relating them to a community of users and, optionally, their users. For instance, a building and its neighbours.

We have background commands and functions for invoice generation, although we haven't included any payment gateway yet.

A Django REST project is needed, where this app would be plugged.

## Brief code organization overview:
- The app follows the structure of a common django app.
- The easiest way to browse the code is to explore the urls.py file, and from those urls follow the calls to the views.py file.  Database models are under models.py.

## SaaS

Our SaaS [Supervecina](https://app.supervecina.com) (demo/demo) provides access to the Energy Metering section under the sidebar item "PATIO" -> "PHOTOVOLTAIC SELF-CONSUMPTION".  
There, we can see:
- The generation of energy from the solar photovoltaic panels.
- The consumption of energy by the community conformed by the homes, shops or buildings connected to the electrical circuit.

