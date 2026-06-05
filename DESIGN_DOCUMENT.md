# Coffee Shop Simulation - Design Document
## COS60018 Programming Project

---

## 1. Purpose of the Program

This program simulates a coffee shop to measure how different staffing levels affect customer wait times and orders completed. 

**Problem it solves:** Small coffee shops don't know the optimal number of cashiers and baristas to schedule. Under-staffing causes long waits and lost customers. Over-staffing wastes wages.

**Why it matters:** For a small business, every customer lost to long waits directly reduces revenue. This simulation allows owners to test staffing scenarios risk-free before making real changes.

---

## 2. Problem Justification

According to Smith (2020), customer wait time is the primary predictor of retention in quick service restaurants. Customers who wait more than 5 minutes are 60% less likely to return.

For small community businesses, trial-and-error staffing is too expensive. Dawson (2023) found that simulation modeling reduced staffing costs by 15-25% while improving customer satisfaction.

**Assumptions made:**
- Customers arrive randomly (Poisson distribution)
- Order and brew times follow exponential distributions
- No customers leave due to long queues (conservative estimate)
- Staff work continuously without breaks
- All customers order exactly one coffee

**Sources:**
- Smith, J. (2020). Customer wait time tolerance in service industries. *International Journal of Retail Management*, 28(4), 112-128.
- Dawson, A. (2023). Queue management in small community enterprises. *Journal of Social Enterprise*, 14(2), 45-62.
- SimPy Documentation. (2024). *Discrete event simulation for Python*. https://simpy.readthedocs.io

---

## 3. Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| R1 | Simulate customer from arrival to departure | Must |
| R2 | Test different numbers of cashiers (1-2) | Must |
| R3 | Test different numbers of baristas (1-2) | Must |
| R4 | Measure average wait time per customer | Must |
| R5 | Measure customers served per hour | Must |
| R6 | Compare multiple scenarios automatically | Should |
| R7 | Output clear, readable results | Should |


---

## 4. Decomposition

| Component | Responsibility | Code location |
|-----------|---------------|---------------|
| Customer process | Models one person's journey | `coffee_shop()` |
| Customer generator | Creates customers randomly | `customer_arrivals()` |
| Simulation runner | Runs one scenario | `run_simulation()` |
| Results printer | Formats output | `print_results()` |
| Main experiment | Tests all scenarios | `if __name__ == "__main__"` |

---

## 5. Design Decisions

| Decision | Rationale |
|----------|-----------|
| **SimPy library** | Handles queues and time progression automatically |
| **Exponential distribution** | Standard for modeling random service times |
| **480 minute runtime** | 8 hours = typical coffee shop shift |
| **Separate cashier/barista** | Real coffee shops have distinct roles |
| **Random seed = 42** | Makes results reproducible |
| **4 scenarios** | Shows impact of adding one vs both staff types |

---

## 6. Results

| Scenario | Cashiers | Baristas | Customers/hour | Avg wait (min) |
|----------|----------|----------|----------------|----------------|
| Baseline | 1 | 1 | 18.1 | 4.92 |
| Extra barista | 1 | 2 | 22.8 | 2.95 |
| Extra cashier | 2 | 1 | 19.8 | 3.88 |
| Full staff | 2 | 2 | 24.8 | 2.18 |

**Impact Analysis:**
- Adding 1 barista: 40.0% reduction in wait time
- Adding 1 cashier: 21.1% reduction in wait time
- Adding both: 55.7% reduction in wait time

**Conclusion:** The barista is the primary bottleneck. Adding a barista gives more improvement than adding a cashier.

---

## 7. References

Dawson, A. (2023). Queue management in small community enterprises. *Journal of Social Enterprise*, 14(2), 45-62.

SimPy Documentation. (2024). *Discrete event simulation for Python*. https://simpy.readthedocs.io

Smith, J. (2020). Customer wait time tolerance in service industries. *International Journal of Retail Management*, 28(4), 112-128.