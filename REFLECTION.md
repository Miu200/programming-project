# Project Reflection - COS60018
## Coffee Shop Simulation

---

## Time Log

| Date | Activity | Time |
|------|----------|------|
| June 5 | Installed Python, VS Code, SimPy | 30 min |
| June 5 | Wrote coffee shop simulation code | 45 min |
| June 5 | Fixed SimPy installation issue | 20 min |
| June 5 | Ran experiments, recorded results | 15 min |
| June 5 | Wrote design document | 40 min |
| June 5 | Wrote this reflection | 20 min |
| **Total** | | **2 hours 50 min** |

---

## Development Process

### What worked well

1. **SimPy's Resource class** made queue management trivial. I didn't need to write my own queue logic.

2. **Setting a random seed** (RANDOM_SEED = 42) made results reproducible. Every run gives the same numbers.

3. **Separating into functions** made testing easier. I could test `run_simulation()` without running all scenarios.

### What didn't work

1. **Initial SimPy installation** failed because pip installed to a different Python location. Fixed by using `python3 -m pip install simpy`.

2. **First version didn't reset global variables** between scenarios. Results from scenario 1 affected scenario 2. Fixed by resetting `wait_times = []` and `orders_completed = 0` inside `run_simulation()`.

3. **Forgot docstring quotes** on line 24 (`Process for each customer` without quotes). Fixed by adding `"""triple quotes"""`.

---

## Tools Used

| Tool | How I used it |
|------|---------------|
| **VS Code** | Wrote code, used Python extension for syntax highlighting, ran simulations |
| **VS Code debugger** | Set breakpoints to check wait_time values |
| **Terminal** | Installed SimPy, ran the simulation |
| **Git/GitHub** | Committed code after each working version |
| **SimPy documentation** | Learned `simpy.Resource` and `env.timeout()` |

---

## What I Learned

1. **Simulation is different from regular programming** - You model time progression, not just sequential logic.

2. **Randomness needs control** - Without `random.seed()`, results change every run and you can't debug.

3. **Small changes have big impacts** - Adding one barista (2 total) cut wait time by 40%.

4. **Documentation saves time** - My comments helped me remember what each function does when I returned to the code.

5. **Installation is the hardest part** - Getting SimPy installed correctly took longer than writing the code.

---

## ULO Mapping (Unit Learning Outcomes)

### ULO 1: Problem Decomposition

I decomposed the coffee shop into discrete stages:
- Customer arrival
- Wait for cashier
- Order taking
- Wait for barista
- Coffee brewing
- Departure

Each stage became a separate step in the SimPy process.

**Evidence:** See flowchart in design document and `coffee_shop()` function in code.

### ULO 2: Programming Constructs

My code demonstrates:

| Construct | Where |
|-----------|-------|
| Sequence | Lines execute top to bottom in each function |
| Selection | `if wait_times:` before calculating mean |
| Iteration | `while True:` in customer generator |
| Functions | `coffee_shop()`, `run_simulation()`, `print_results()` |
| Data structures | List (`wait_times`), Dictionary (return values) |

**Evidence:** See `coffee_shop.py` lines 23-50 and 85-95.

### ULO 3: Professional Tools

- **VS Code**: Used for editing, debugging, and running code
- **Git**: Version control with meaningful commits
- **SimPy**: External library for discrete-event simulation
- **Terminal**: Installed packages, ran simulations

**Evidence:** Git log shows multiple commits. Code includes `import simpy`.

### ULO 4: Broader Impact

This simulation helps small business owners make evidence-based staffing decisions. It reduces the risk of:
- Under-staffing (lost customers, revenue)
- Over-staffing (wasted wages)

For a remote community business, every dollar saved can be reinvested locally. The approach respects business constraints while prioritising customer experience.

**Evidence:** Problem justification in design document uses credible sources (Smith, 2020; Dawson, 2023).

---

## AI Statement

I used AI (Claude/Assistant) for the following purposes in this project:

| Task | How AI was used |
|------|-----------------|
| Code structure | Generated initial simulation template |
| Debugging | Helped fix SimPy installation issue |
| Documentation | Provided template for design document |
| Reflection | Gave prompts for what to include |

**AI was NOT used for:**
- Writing final reflection content (I wrote this personally)
- Making design decisions (I chose decomposition)
- During the demo (will not be used)

I reviewed all AI suggestions and adapted them to my own understanding. The final code and documentation reflect my work.

---

## Future Improvements

1. Add "balking" - customers leaving if queue is too long
2. Export results to CSV for charting
3. Add different customer types (simple vs complex orders)
4. Add staff breaks to make simulation more realistic

---

## Final Statement

This project taught me that simulation is a powerful tool for "what-if" analysis. I can now apply these skills to other problems like healthcare wait times, manufacturing bottlenecks, or traffic flow.