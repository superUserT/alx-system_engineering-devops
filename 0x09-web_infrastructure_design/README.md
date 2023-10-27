# Project: Web Infrastructure Design

**Captain's Log Due:** 2023-10-29 (in 3 days) - Log it now!

**Author:** Sylvain Kalache, co-founder at Holberton School

**Project Weight:** 1

**Project Start Date:** Oct 26, 2023 6:00 AM

**Project End Date:** Oct 30, 2023 6:00 AM

**Manual QA Review:** Must be done upon project completion

## Concepts

For this project, you are expected to explore the following concepts:

- DNS
- Monitoring
- Web Server
- Network basics
- Load balancer
- Server

## Resources

Read or watch the following resources to prepare for this project:

- Network basics concept page
- Server concept page
- Web server concept page
- DNS concept page
- Load balancer concept page
- Monitoring concept page
- What is a database
- What's the difference between a web server and an app server?
- DNS record types
- Single point of failure
- How to avoid downtime when deploying new code
- High availability cluster (active-active/active-passive)
- What is HTTPS
- What is a firewall

## Learning Objectives

By the end of this project, you should be able to:

- Draw a diagram of the web stack you build with sysadmin/devops track projects
- Explain the function of each component in your infrastructure
- Understand system redundancy
- Know key acronyms such as LAMP, SPOF, and QPS

## Requirements

**General:**

- A README.md file is mandatory at the root of the project folder.
- For each task, whiteboard your solution and take a picture/screenshot of your diagram.
- This project will be manually reviewed.
- Focus on what the requirements mention; explore details in later projects.
- Avoid plagiarism; create solutions independently.
- All content must be written in English to enhance your technical skills in diverse settings.

## Tasks

### 0. Simple Web Stack

Design a single-server web infrastructure that hosts a website reachable via www.foobar.com. 

Requirements:

- Use 1 server, 1 web server (Nginx), 1 application server, 1 application code base, 1 MySQL database, and a domain name foobar.com with a www record pointing to server IP 8.8.8.8.
- Explain the role of each component, domain names, DNS records, and the issues with this setup.

### 1. Distributed Web Infrastructure

Design a three-server web infrastructure hosting www.foobar.com.

Requirements:

- Use 2 servers, 1 web server (Nginx), 1 application server, 1 load balancer (HAproxy), 1 application code base, and 1 MySQL database.
- Explain the purpose of each added element, distribution algorithm, Active-Active or Active-Passive setup, and the issues with this infrastructure.

### 2. Secured and Monitored Web Infrastructure

Design a three-server web infrastructure for www.foobar.com that is secured, serves encrypted traffic, and is monitored.

Requirements:

- Add 3 firewalls, 1 SSL certificate for HTTPS, and 3 monitoring clients.
- Explain the addition of each element, the role of firewalls, HTTPS traffic, monitoring, and the issues with this setup.

**Note:** After completing each task, you should insert the necessary links and documentation into the README.md file in your project directory.

**Copyright © 2023 ALX, All rights reserved.**
