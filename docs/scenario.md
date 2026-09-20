
# Cybersecurity Simulation Scenario

## 1. Organization

Name: Asterix Financial Services

Asterix Financial Services is a fictional financial services company. Employees use corporate devices and internal applications to perform daily business activities.

The organization handles sensitive financial reports and customer records.

## 2. Organization Size

- Employees: 15
- Corporate devices: 18
- Applications: 3
- Simulation duration: 36 hours
- Target dataset size: 750 events

## 3. Applications

1. Identity Provider: Handles employee authentication.
2. Document Portal: Stores and manages company documents.
3. Internal Web Application: Supports everyday business operations.

## 4. Security Incident

An external attacker compromises an employee's credentials.

Using the compromised account, the attacker authenticates to the company's systems, accesses sensitive documents, and exfiltrates company data.

The incident must appear within normal employee activity rather than as an isolated sequence of malicious events.

## 5. Simulation Objective

Generate an OCSF 1.9-aligned dataset containing realistic normal business activity and a connected, multi-step cybersecurity incident.

The dataset must preserve consistent relationships between users, devices, applications, sessions, and events.
