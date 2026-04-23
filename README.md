# Acme Data Platform

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10-blue)]()
[![License](https://img.shields.io/badge/license-internal-lightgrey)]()

---

## Overview

The Acme Data Platform is an internal data processing system responsible for ingesting, transforming, and loading operational data from multiple upstream systems into analytics storage (BigQuery).

This platform supports reporting, internal dashboards, and data-driven workflows across teams.

---

## Key Features

- Multi-source data ingestion (Salesforce, Zendesk, GitHub)
- Data transformation and normalization
- Schema validation
- Environment-based configurations (dev / prod)
- Structured logging and error handling

---

## Architecture
             +----------------------+
             |  External Sources    |
             |----------------------|
             | Salesforce           |
             | Zendesk              |
             | GitHub               |
             +----------+-----------+
                        |
                        v
             +----------------------+
             |  Extraction Layer    |
             +----------+-----------+
                        |
                        v
             +----------------------+
             | Transformation Layer |
             +----------+-----------+
                        |
                        v
             +----------------------+
             |  Validation Layer    |
             +----------+-----------+
                        |
                        v
             +----------------------+
             |      BigQuery        |
             | (Analytics Storage)  |
             +----------------------+

