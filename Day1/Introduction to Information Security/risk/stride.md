# STRIDE Threat Modeling with Risk Assessment: A Software Architect's Perspective

## Introduction

STRIDE is a threat modeling methodology used to identify and prioritize potential threats in a system. In this 
presentation, we will walk through the STRIDE model step-by-step as a software architect performs threat modeling
on an interesting example project.

## Example Project: A Banking Application

Our hypothetical banking application is a web-based platform that allows users to view their account balances, 
transfer funds between accounts, and make bill payments online.

## Step 1: Identify the Assets

Assets are the components of our system that have value or can be exploited if compromised. In our banking 
application:

1. User accounts and sensitive data (e.g., names, addresses, account balances)
2. Application codebase and configuration files
3. External APIs and services
4. Network infrastructure (e.g., firewalls, load balancers)
5. Physical servers and storage devices

## Step 2: Identify the Adversaries

Adversaries are entities that could potentially exploit our system for malicious purposes. In a banking 
application, adversaries might include:

1. Hackers seeking financial gain or to disrupt services
2. Insiders with authorized access but ill intentions
3. Social engineering attackers (e.g., phishing emails)

## Step 3: Identify the Threat Agents

Threat agents are the specific methods or techniques that adversaries can use to target our assets. Using STRIDE,
we consider:

- **Spoofing:** Impersonating a user or system (e.g., phishing emails)
- **Tampering:** Modifying data (e.g., changing account balances)
- **Repudiation:** Denying actions performed (e.g., claiming not to have made a transaction)
- **Information Disclosure:** Exposing confidential information (e.g., user credentials)
- **Denial of Service:** Making the system unavailable (e.g., flooding it with traffic)
- **Elevation of Privilege:** Gaining unauthorized access to higher levels (e.g., exploiting vulnerabilities)

## Step 4: Perform a Risk Assessment

For each threat agent identified, we assess the risk level based on the likelihood of occurrence and impact. Our 
goal is to prioritize threats for remediation.

### Spoofing

- Likelihood: Moderate (Social engineering attacks are common)
- Impact: High (Adversary can gain access to user accounts and sensitive data)
- Risk Level: Medium to High

### Tampering

- Likelihood: Low (Requires exploiting a vulnerability)
- Impact: Extremely High (Adversary can transfer funds or make unauthorized transactions)
- Risk Level: High

### Repudiation

- Likelihood: Low (Requires sophisticated attacks)
- Impact: High to Critical (Financial loss and potential regulatory repercussions)
- Risk Level: Medium to High

### Information Disclosure

- Likelihood: Moderate (Vulnerabilities or exploits may be discovered)
- Impact: High (Adversary can use the information for further attacks)
- Risk Level: Medium to High

### Denial of Service

- Likelihood: Moderate (Common attack vector)
- Impact: Moderate to High (Users cannot access the application)
- Risk Level: Moderate

### Elevation of Privilege

- Likelihood: Low (Requires exploiting a zero-day vulnerability)
- Impact: Extremely High (Adversary gains complete control over the system)
- Risk Level: Low to Medium

## Conclusion

Based on our risk assessment, we prioritize threats with high impact and medium to high likelihood. Our software 
architect now has a clear understanding of potential threats to the banking application and can allocate 
resources accordingly for mitigation efforts.
