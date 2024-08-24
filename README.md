# Payment Processing System

## Design Patterns and Principles

### Overview
This document briefly explains the design decisions for the payment processing system, highlighting the application of SOLID principles and the Strategy pattern.

### SOLID Principles

- **Single Responsibility Principle (SRP)**:
  Each class has one responsibility, e.g., `CreditCardPayment` handles credit card transactions, `TransactionLogger` manages logging.

- **Open/Closed Principle (OCP)**:
  The system can be extended (e.g., new payment methods) without modifying existing code.

- **Liskov Substitution Principle (LSP)**:
  Subclasses (`CreditCardPayment`, `PayPalPayment`) can replace their base class without altering the correctness of the program.

- **Interface Segregation Principle (ISP)**:
  Interfaces are kept focused; e.g., `PaymentMethod` interface includes only essential methods.

- **Dependency Inversion Principle (DIP)**:
  High-level modules depend on abstractions, not concrete implementations, e.g., `PaymentProcessor` relies on `PaymentMethod` interface.

### Strategy Pattern

- **Purpose**: Encapsulates payment algorithms and makes them interchangeable.

- **Application**:
  `PaymentProcessor` uses the Strategy pattern to handle different payment methods by delegating to the `PaymentMethod` implementations.

- **Benefits**:
  - **Flexibility**: Easily switch or add new payment methods.
  - **Maintainability**: Isolated classes for each payment method simplify changes.
